# Customer Service Chatbot with AWS Lex and AWS Lambda

## Overview

This project demonstrates how to create a customer service chatbot using AWS Lex and AWS Lambda. The chatbot is designed to handle customer service like Account Creation requests by collecting essential information such as the user's first name, last name, date of birth and Country. The data used for training the chatbot is from the [**Training Dataset for chatbots/Virtual Assistants**](https://datalink.youdata.ai/yc4e3kx3) provided by Youdata.ai for the [**HumanAIze Hackathon <FinTech Edition>**](https://hack2skill.com/hack/humanaize-fintech/) by Hack2Skill.

## Features

- Collects user information (First Name, Last Name, Date of Birth,Country)
- Validates user inputs
- Integrates with AWS Lambda for backend processing
- Trained with real-world data from Youdata.ai

## Architecture

1. **AWS Lex**: Used to create and manage the chatbot.
2. **AWS Lambda**: Used to handle backend logic and validation.
3. **Training Data**: Sourced from Youdata.ai for realistic and robust training.

## Prerequisites

- AWS Account
- Access to AWS Management Console
- Basic knowledge of AWS Lex and AWS Lambda

## Setup Instructions

### 1. Create an AWS Lex Bot

1. Log in to the [AWS Lex console](https://console.aws.amazon.com/lex/).
2. Create a new bot or open an existing bot.
3. Add an intent named `CreateAccountIntent`.
4. Add slots for `FirstName`, `LastName`, `DOB` and `Country`.
   - `FirstName`: Slot type `AMAZON.Person`
   - `LastName`: Slot type `AMAZON.Person`
   - `DOB`: Slot type `AMAZON.DATE`
   - `Country`:Slot type `AMAZON.Country`
5. Configure the intent to use a Lambda function for fulfillment.

### 2. Create an AWS Lambda Function

1. Log in to the [AWS Lambda console](https://console.aws.amazon.com/lambda/).
2. Create a new Lambda function.
3. Use this code  into the Lambda function:

```python
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
```
## Training Data
The training data used for this project is sourced from the Training Dataset for chatbots/Virtual Assistants provided by Youdata.ai for the [HumanAIze Hackathon](https://hack2skill.com/hack/humanaize-fintech/) <FinTech Edition> by Hack2Skill. You can access the dataset [here](https://datalink.youdata.ai/yc4e3kx3).

## Conclusion
This project showcases the integration of AWS Lex and AWS Lambda to create a functional customer service chatbot.This is how ConvoCloud, powered by AWS Lex, can revolutionize customer service for small startups. By leveraging scalable cloud services, advanced AI capabilities, and seamless integration with AWS, ConvoCloud offers a cost-effective, secure, and efficient solution for managing customer interactions. You can read my [Blog](https://medium.com/@22cd3034/why-small-businesses-should-use-cloud-services-for-chatbot-development-365c8ce7f3a1) on Medium like how Small sStartup can get help from AWS Lex Services for their Customer Services

## For Future:

We will add more intents for like "payment issue address", "account recovery" and integrating with Generative Ai.


