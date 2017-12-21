from pyflights import PyFlight

flight = PyFlight(api_key='AIzaSyDtt43qqeiev2aQxsQIGexJccVuiqJNkfk')

search = flight.search(params={
        'adult_count': 1,
        'origin': 'DUB',
        'max_price': 'EUR500',
        'destination': 'GDN',
        'date': 'enter departure date here',
        'solutions': 1
})

for results in search:
    print('Sale total: %s' % results.sale_total())
    print('Flight carrier: %s' % results.flight_carrier())
    print('Origin: %s' % results.origin())
    print('Destination: %s' % results.destination())
    print('Deparure Time: %s' % results.departure_time())
    print('Arrival Time: %s' % results.arrival_time())