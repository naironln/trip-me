import requests

class PyFlight:

    def search(self, params):

        endpoint = 'https://www.google.com/flights/#search;f=SAO;t=JFK;d=2018-01-05;r=2018-01-09'
        req = requests.get(endpoint)
        endpoint = "https://www.google.com/flights/#search;f={};t={};d={};r={}".format(params['origin'], params['destination'],params['date'],params['return_date'])
        print(endpoint)

        # url = self.endpoint + 'key=' + "AIzaSyDtt43qqeiev2aQxsQIGexJccVuiqJNkfk"
        # req = requests.post(url, json={
        #     'request': {
        #         'passengers': {
        #             'adultCount': params.get('adult_count',1)
        #         },
        #         'slice': [
        #             {
        #                 'origin': params['origin'],
        #                 'date': params['date'],
        #                 'destination': params['destination']
        #             },
        #             {
        #                 'origin': params['destination'],
        #                 'date': params['return_date'],
        #                 'destination': params['origin']
        #             }
        #         ],
        #         'maxPrice': params.get('max_price'),
        #         'solutions': params.get('solutions')
        #     }
        # })
        # print(req.json())

pf = PyFlight()
params = {"origin": "SAO", 'destination': 'NYC', 'date': '2018-01-05', 'return_date': '2018-01-25'}
pf.search(params)