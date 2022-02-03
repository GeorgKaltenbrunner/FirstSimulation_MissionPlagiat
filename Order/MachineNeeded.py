import random


def machine_needed(max_number_machines):
    number_machines = random.randint(1, max_number_machines)

    list_machines = []

    if number_machines == 1:
        list_machines.append(number_machines)
        return list_machines

    else:
        for i in range(number_machines):
            machine = random.randint(1, max_number_machines)
            if machine not in list_machines:
                list_machines.append(machine)
        return list_machines

print(machine_needed(3))