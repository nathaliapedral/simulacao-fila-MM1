from event import Event
from customer import Customer

events_list = []
customers_list = []
wait_queue = []

first_customer = Customer()
customers_list.append(first_customer)

first_arrival = Event('CH', 1, 0)
events_list.append(first_arrival)

#events_list[0].queue_arrival(customers_list, events_list, wait_queue)

# for x in xrange(0, 9):
# 	events_list[x].queue_arrival(customers_list, events_list)
i = 0
while len(events_list) > 0:
	if (events_list[i].event_type == "CH"):		
		events_list[i].queue_arrival(customers_list, events_list, wait_queue)
	elif (events_list[i].event_type == "ES"):
		events_list[i].service_entry(events_list, wait_queue)
	elif (events_list[i].event_type == "SS"):
		events_list[i].service_exit(events_list, wait_queue)
	print events_list[i].event_type, i, wait_queue
	print '========================='
	i += 1
	if i == 10:
		break
	

for x in events_list:
	print x.time, x.event_type, x.customer_index
	