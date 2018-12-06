from customer import *

class Statistics:

	def __init__(self):
		self.sample_index = 0
		self.mean_service_time = 0
		self.mean_queue_time = 0
		self.mean_system_time = 0


	#calculo tempo medio de servico 
	def mean_calculator (self, customer):
		self.sample_index += 1
		self.mean_service_time += (customer.exit_server_time - customer.entry_server_time)
		self.mean_queue_time += (customer.entry_server_time - customer.arrival_time)
		self.mean_system_time += (customer.exit_server_time - customer.arrival_time)