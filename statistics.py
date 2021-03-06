from customer import *

class Statistics:

	def __init__(self):
		self.sample_index = 0
		self.sample_service_time = 0
		self.sample_queue_time = 0
		self.sample_system_time = 0
		self.mean_queue_wait = 0

	'''
	Somatorio das estatisticas, sendo elas:
	- tempo de servico
	- tempo de espera na fila 
	- tempo total gasto no sistema
	'''
	def statistics_acumulator (self, customer):
		self.sample_index += 1
		self.sample_service_time += (customer.exit_server_time - customer.entry_server_time)
		self.sample_queue_time += (customer.entry_server_time - customer.arrival_time)
		self.sample_system_time += (customer.exit_server_time - customer.arrival_time)

	#Metodo responsavel pelo calculo da media do tempo de espera na fila
	def  mean_calculator(self):
		self.mean_queue_wait = self.sample_queue_time / self.sample_index