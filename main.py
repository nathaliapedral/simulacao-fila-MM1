from event import Event
from customer import Customer

events_list = []
customers_list = []

first_customer = Customer()
customers_list.append(first_customer)

first_arrival = Event('CH', 1, len(customers_list)-1)
events_list.append(first_arrival)

for x in xrange(0, 9):
	events_list[x].queue_arrival(customers_list, events_list)

print len(events_list)
	
	