import json
from django.conf import settings
from watson_developer_cloud import ConversationV1


class Conversation():
    def __init__(self):        
        self.conversation = ConversationV1(
            username=settings.WATSON_USERNAME,
            password=settings.WATSON_PASSWORD,
            version=settings.WATSON_VERSION
        )

    def send_message(self, message, context=None):
        message_input = {'text': message}
        
        kwargs = {"workspace_id": '8cc76f89-07a7-4f66-8f6f-4e8a6571cdf5',
                 "message_input": message_input}

        if context:
            kwargs['context'] = context

        print("**kwargs", kwargs)
        
        response = self.conversation.message(**kwargs)
        # print(response)
        return response

# print(json.dumps(response['output']['text'], indent=2))