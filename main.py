# import packages
import simpy
import random
import numpy

# Initialize variables
NUMBER_OF_ORDERS = 200
NUMBER_OF_MACHINES = 3

# Initialize lists for further information
orders_created = []
orders_produced = []
order_over_due_date = []

# Initialize lists for calculating average wait time for orders
order_wait_time = []
order_time = []
order_prio = []
#dict_order = {'': ['order_prio', 'order_time', 'order_finished']}

# List of Products and their productions time
products = {"A": 20, "B": 30, "C": 15, "D": 40}

# Save production times in list to have easier access for later procesing
times = products.values()
times_list = list(times)


# Generate the orders
def generate_order(env, machine):
    for i in range(NUMBER_OF_ORDERS):
        # The generation of the order can take between 1 until 20
        yield env.timeout(random.randint(1, 20))
        y = random.randint(0,10)
        env.process(order(env, i, machine, y))


def order(env, order_id, machine, prio):
    print("Order %s was made at time %.1f with prio %s" % (order_id, env.now, prio))
    order_time.append("Order %s with prio %s at  %.1f" % (order_id, prio, env.now))
    print(order_time)
    with machine.request() as req:
        start_production = env.now
        yield req
        order_wait_time.append(env.now - start_production)
        product_item = random.randint(0, len(products) - 1)
        time_to_produce = times_list[product_item]
        yield env.timeout(time_to_produce)
        print("#### Order %s finished in %.1f seconds. Order was finished at time %.1f" % (
            order_id, env.now - start_production, env.now))
        order_time.append(env.now - start_production)


# Setup Environment
env = simpy.Environment()

# Initialize machine
machine = simpy.Resource(env, NUMBER_OF_MACHINES)

# Run simulation
env.process(generate_order(env, machine))
env.run(until=200)

# Print the average waiting times from lists in lines 11-12
print("\n\nAverage wait time for orders: %.1f seconds." % (numpy.mean(order_wait_time)))
print("Average time until order is finished: %.1f seconds." % (numpy.mean(order_time)))
