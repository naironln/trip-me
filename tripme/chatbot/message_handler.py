import socket
from .utils import post_facebook_message
from django.conf import settings
from iata_codes import IATACodesClient
from .watson import Conversation

users = {}

class MessageHandler:
    def __init__(self, context):
        self.context = context
        print("Context", context)
        self.wt_conversation = Conversation()
        
    def handle(self, message):

        # self.socket_connection()
        args = [message['message']['text']]
        if self.context:
            args.append(self.context.get('context'))

        wt_response = self.wt_conversation.send_message(*args)
        print("Response",wt_response)

        trip_data = self.context.get('trip_data', {})

        if wt_response['entities']:
            trip_data = self.generate_trip_data(wt_response['entities'], trip_data)

        
        post_facebook_message(message['sender']['id'],
                              wt_response['output']['text'][0])

        print("user:", message['message']['text'])
        print("Watson:", wt_response['output']['text'][0])


        
        if self.is_complete(trip_data, message['sender']['id']):
            trip_data = {}
        
        context = {'context': wt_response['context'],
                    'trip_data': trip_data}
        print("Response", context)
        
        return context

    def get_iata_code(self,name):
        from .cities import cities
        print("Name",name)
        for city in cities:
            if city['name'].lower() == name.lower():
                return city['code']


    def get_entity(self, entities):
        # import operator
        # entity = sorted(entities, key=operator.itemgetter('confidence'))
        # print("Entity: ",entities)
        entity_ = None
        confidence = 0
        for i, entity in enumerate(entities):
            if entity['confidence'] > confidence:
                confidence = entity['confidence']
                entity_ = entity
        return entity_

    def generate_trip_data(self, entities, trip_data):
        entity = self.get_entity(entities)

        if entity['entity'] == 'City':
            if 'to' in trip_data:
                trip_data['from'] = self.get_iata_code(entity.get('value'))
            else:
                trip_data['to'] = self.get_iata_code(entity.get('value'))
        
        elif entity['entity'] == 'sys-date':
            if 'departure' in trip_data:
                trip_data['arrival'] = entity.get('value')
            else:
                trip_data['departure'] = entity.get('value')
        print(trip_data)
        return trip_data

    def is_complete(self, trip_data, sender_id):
        trip_keys = ['from', 'to', 'departure', 'arrival']
        if all(key in trip_data for key in trip_keys):
            url = "https://www.google.com/flights/#search;f={};t={};d={};r={}".format(trip_data['from'], 
                                                                                      trip_data['to'],
                                                                                      trip_data['departure'],
                                                                                      trip_data['arrival'])

            message = "Veja o que encontrei para você: {}".format(url)

            post_facebook_message(sender_id, message)

            return True
