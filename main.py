from event import Event
from customer import Customer

events_list = []
customers_list = []
wait_queue = []

first_customer = Customer(0)
customers_list.append(first_customer)

first_arrival = Event('CH', 0, 0)
events_list.append(first_arrival)

#events_list[0].queue_arrival(customers_list, events_list, wait_queue)

# for x in xrange(0, 9):
# 	events_list[x].queue_arrival(customers_list, events_list)
i = 0
while len(events_list) > 0:
	current_event = events_list.pop(0)
	print current_event.time, current_event.event_type, current_event.customer_index
	if (current_event.event_type == "CH"):		
		current_event.queue_arrival(customers_list, events_list, wait_queue)
	elif (current_event.event_type == "ES"):
		current_event.service_entry(customers_list, events_list, wait_queue)
	elif (current_event.event_type == "SS"):
		current_event.service_exit(customers_list, events_list, wait_queue)
	i += 1
	if i == 20:
		break
	

#for x in events_list:
	#print x.time, x.event_type, x.customer_index

for x in customers_list:
	print x.arrival_time, x.entry_server_time, x.exit_server_time
	