import json
from pprint import pprint
from django.views import generic
from django.http.response import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .message_handler import MessageHandler 

#  I've tried using django's session, but sessions was'nt working, then I set this global variable
session = {}
class TripmeBotView(generic.View):

    def get(self, request, *args, **kwargss):
        if self.request.GET.get(u'hub.verify_token') == settings.FACEBOOK_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
        return HttpResponse("It's Rock!")


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargss):
        return generic.View.dispatch(self, request, *args, **kwargss)

    def post(self, request, *args, **kwargss):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    sender_id = str(message['sender']['id'])

                    self.session_handler(sender_id)
                    print("Session", session)
                    self.message_handler = MessageHandler(session.get(sender_id))
                    context = self.message_handler.handle(message)
                    self.session_handler(sender_id, context)


                    # if sender_id not in session:
                    
        return HttpResponse()

    def session_handler(self, sender_id, context=None):
        if sender_id in session and context:
            print("salvando session=================")
            session[sender_id] = context
            print(session)
        elif sender_id not in session:
            session[sender_id] = {'context':context}

