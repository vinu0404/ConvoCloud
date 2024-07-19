import json
import datetime
import time

def validate(slots):
    if not slots['FirstName']:
        return {
            'isValid': False,
            'violatedSlot': 'FirstName',
            'message': 'Give your first name'
        }
       
    if not slots['LastName']:
        return {
            'isValid': False,
            'violatedSlot': 'LastName',
            'message': 'Give your last name.'
        }

    if not slots['DOB']:
        return {
            'isValid': False,
            'violatedSlot': 'DOB',
            'message': 'Give your Birth Date'
        }

    try:
        dob = datetime.datetime.strptime(slots['DOB']['value']['originalValue'], '%Y-%m-%d')
        if dob >= datetime.datetime.now():
            return {
                'isValid': False,
                'violatedSlot': 'DOB',
                'message': 'The date of birth must be in the past. Please provide a valid date of birth.'
            }
    except ValueError:
        return {
            'isValid': False,
            'violatedSlot': 'DOB',
            'message': 'The date of birth format is incorrect. Please provide the date in YYYY-MM-DD format.'
        }

    return {'isValid': True}


    if not slots['CountryName']:
        return {
            'isValid': False,
            'violatedSlot': 'CountryName',
            'message': 'Give your Country Name.'
        }
    


def lambda_handler(event, context):
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    validation_result = validate(slots)
   
    if event['invocationSource'] == 'DialogCodeHook':
        if not validation_result['isValid']:
            response = {
                "sessionState": {
                    "dialogAction": {
                        'slotToElicit': validation_result['violatedSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        'name': intent,
                        'slots': slots
                    }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": validation_result['Your account has been created ']
                    }
                ]
            }
            return response
        else:
            response = {
                "sessionState": {
                    "dialogAction": {
                        "type": "Delegate"
                    },
                    "intent": {
                        'name': intent,
                        'slots': slots
                    }
                }
            }
            return response

    if event['invocationSource'] == 'FulfillmentCodeHook':
        # Placeholder for account creation logic
        first_name = slots['FirstName']['value']['originalValue']
        last_name = slots['LastName']['value']['originalValue']
        dob = slots['DOB']['value']['originalValue']

        message = "Thanks"
       
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    'name': intent,
                    'slots': slots,
                    'state': 'Fulfilled'
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": message
                }
            ]
        }
       
        return response


