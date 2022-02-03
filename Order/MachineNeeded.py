import random
import Capacity


def machine_needed(max_number_machines, capa_start, capa_end):
    number_machines = random.randint(1, max_number_machines)
    list_machines = {}

    for i in range(number_machines):
        machine = random.randint(1, max_number_machines)
        if i not in list_machines:
            list_machines[machine] = Capacity.get_capacity(capa_start, capa_end)

    return list_machines


#print(machine_needed(3))
