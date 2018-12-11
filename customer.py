class Customer:

	'''
	Atributos do fregues: 
	 - id 
	 - arrival_time: tempo de chegada no sistema
	 - entry_server_time: tempo de entrada em servico
	 - exit_server_time: tempo de saida do servico
	 - arrival_round: rodada em que o fregues chega
	'''

	def __init__(self, id_, arrival_time, arrival_round):
		self.id = id_
		self.arrival_time = arrival_time
		self.arrival_round = arrival_round
		self.entry_server_time = 0
		self.exit_server_time = 0


	
