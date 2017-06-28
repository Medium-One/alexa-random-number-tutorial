import Alexa
import Analytics
import Filter
import json
import Store
import random

def build_response(title, output):
    return {
        'version': '1.0',
        'sessionAttributes': {},
            'response' : {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': output
                    },
               'card': {
                   'type': 'Simple',
                   'title': 'SessionSpeechlet - ' + title,
                   'content': 'SessionSpeechlet - ' + output
                  },
              'reprompt': {
                   'outputSpeech': {
                        'type': 'PlainText',
                        'text': ""
                        }
                 },
              'shouldEndSession': True
           }
       }
 
last_value = random.randint(0,1000)

event = IONode.get_event()
request = event['request']
uuid_marker = event.get("uuid", "")
 
response_txt = str(last_value)
 
response_json = build_response(request['intent']['name'], response_txt)
Alexa.response(uuid_marker, response_json)


