# import packages

import simpy
import random
import numpy

# Initialize variables and lists
NO_OF_ORDERS = 10
NO_OF_MACHINES = 2

order_wait_time = []
order_time = []

# List of Products and their productions time
products = {"A": 20, "B": 30, "C": 15, "D": 40}
products_keys = products.keys()
keys_list = list(products_keys)
times = products.values()
times_list = list(times)

"""for key in products:
    print(key)"""


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
        product_name = keys_list[product_item]
        yield env.timeout(time_to_produce)
        print("#### Order %s finished in %.1f second" % (order_id, env.now - start_production))
        order_time.append(env.now - start_production)


env = simpy.Environment()
machine = simpy.Resource(env, NO_OF_MACHINES)

env.process(generate_order(env, machine))
env.run(until=400)

print("\n\nAverage wait time for orders: %.1f seconds." % (numpy.mean(order_wait_time)))
print("Average time until order is finished: %.1f seconds." % (numpy.mean(order_time)))
