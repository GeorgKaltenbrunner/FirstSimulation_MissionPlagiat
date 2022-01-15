# import packages
import simpy
import random
import numpy

# Initialize variables
NO_OF_ORDERS = 20
NO_OF_MACHINES = 2

# Initialize lists for calculating average wait time for orders
order_wait_time = []
order_time = []

# List of Products and their productions time
products = {"A": 20, "B": 30, "C": 15, "D": 40}

# Save production times in list to have easier access for later procesing
times = products.values()
times_list = list(times)

# Gnerate the orders
def generate_order(env, machine):
    for i in range(NO_OF_ORDERS):
        yield env.timeout(random.randint(1, 20))
        env.process(order(env, i, machine))


def order(env, order_id, machine):
    print("Order %s was made at time %.1f" % (order_id, env.now))

    with machine.request() as req:
        start_production = env.now
        yield req
        order_wait_time.append(env.now - start_production)
        product_item = random.randint(0, 3)  # Hier kann noch schöner abgekürzt werden
        time_to_produce = times_list[product_item]
        yield env.timeout(time_to_produce)
        print("#### Order %s finished in %.1f seconds. Order was finished at time %.1f" % (order_id, env.now - start_production, env.now))
        order_time.append(env.now - start_production)

# Setup Environment
env = simpy.Environment()

# Initialize machine
machine = simpy.Resource(env, NO_OF_MACHINES)

# Run simulation
env.process(generate_order(env, machine))
env.run(until=200)

# Print the average waiting times from lists in lines 11-12
print("\n\nAverage wait time for orders: %.1f seconds." % (numpy.mean(order_wait_time)))
print("Average time until order is finished: %.1f seconds." % (numpy.mean(order_time)))
