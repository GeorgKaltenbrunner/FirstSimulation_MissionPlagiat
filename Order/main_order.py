import random
from datetime import datetime, timedelta
import DueDate
import ProductionTime
import MachineNeeded
import Capacity

d = {}


class Order:

    def __init__(self, date_start, date_end, date_format, production_time_start, production_time_end,
                 max_number_machines, capa_start, capa_end, max_number):
        self.date_start = date_start
        self.date_end = date_end
        self.date_format = date_format
        self.production_time_start = production_time_start
        self.production_time_end = production_time_end
        self.max_number_machines = max_number_machines
        self.capa_start = capa_start
        self.capa_end = capa_end
        self.max_number = max_number

    def generate_order(self):
        for i in range(self.max_number):
            d[i] = MachineNeeded.machine_needed(self.max_number_machines, self.capa_start, self.capa_end), DueDate.get_due_date(self.date_start, self.date_end, self.date_format)
        print(d)


order1 = Order("2021/02/01", "2022/03/01", "%Y/%m/%d", 1, 100, 3, 1, 100, 20)

order1.generate_order()
