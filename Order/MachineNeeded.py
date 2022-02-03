import random


def machine_needed(max_number_machines):
    number_machines = random.randint(1, max_number_machines)
    list_machines = []

    for i in range(number_machines):
        machine = random.randint(1, max_number_machines)
        if machine not in list_machines:
            list_machines.append(machine)
    return list_machines


print(machine_needed(3))
