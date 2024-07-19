# Customer Service Chatbot with AWS Lex and AWS Lambda

## Overview

This project demonstrates how to create a customer service chatbot using AWS Lex and AWS Lambda. The chatbot is designed to handle customer service requests by collecting essential information such as the user's first name, last name, and date of birth. The data used for training the chatbot is from the **Training Dataset for chatbots/Virtual Assistants** provided by Youdata.ai for the **HumanAIze Hackathon <FinTech Edition>** by Hack2Skill.

## Features

- Collects user information (First Name, Last Name, Date of Birth)
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
4. Add slots for `FirstName`, `LastName`, and `DOB`.
   - `FirstName`: Slot type `AMAZON.Person`
   - `LastName`: Slot type `AMAZON.Person`
   - `DOB`: Slot type `AMAZON.DATE`
5. Configure the intent to use a Lambda function for fulfillment.

### 2. Create an AWS Lambda Function

1. Log in to the [AWS Lambda console](https://console.aws.amazon.com/lambda/).
2. Create a new Lambda function.
3. Copy and paste the following code into the Lambda function:

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




Certainly! Here is the README.md content formatted as code:

markdown
Copy code
# Customer Service Chatbot with AWS Lex and AWS Lambda

## Overview

This project demonstrates how to create a customer service chatbot using AWS Lex and AWS Lambda. The chatbot is designed to handle customer service requests by collecting essential information such as the user's first name, last name, and date of birth. The data used for training the chatbot is from the **Training Dataset for chatbots/Virtual Assistants** provided by Youdata.ai for the **HumanAIze Hackathon <FinTech Edition>** by Hack2Skill.

## Features

- Collects user information (First Name, Last Name, Date of Birth)
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
4. Add slots for `FirstName`, `LastName`, and `DOB`.
   - `FirstName`: Slot type `AMAZON.Person`
   - `LastName`: Slot type `AMAZON.Person`
   - `DOB`: Slot type `AMAZON.DATE`
5. Configure the intent to use a Lambda function for fulfillment.

### 2. Create an AWS Lambda Function

1. Log in to the [AWS Lambda console](https://console.aws.amazon.com/lambda/).
2. Create a new Lambda function.
3. Copy and paste the following code into the Lambda function:

```python
import json
import datetime
import time

def validate(slots):
    if not slots['FirstName']:
        return {
            'isValid': False,
            'violatedSlot': 'FirstName',
            'message': 'Please provide your first name.'
        }
        
    if not slots['LastName']:
        return {
            'isValid': False,
            'violatedSlot': 'LastName',
            'message': 'Please provide your last name.'
        }

    if not slots['DOB']:
        return {
            'isValid': False,
            'violatedSlot': 'DOB',
            'message': 'Please provide your date of birth.'
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
                        "content": validation_result['message']
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
        
        # Example of backend integration for account creation
        # result = create_account(first_name, last_name, dob)
        #
        # if result['status'] == 'success':
        #     message = "Thanks, your account has been created successfully."
        # else:
        #     message = "There was an issue creating your account. Please try again later."

        # For the sake of this example, we will assume the account creation is successful
        message = "Thanks, your account has been created successfully."
        
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

Configure your Lambda function to be triggered by AWS Lex.
Deploy the Lambda function.
 Train Your Lex Bot
Go back to the AWS Lex console.
Build your bot to apply the changes.
Test the bot using the test window in the Lex console.

Creating the Lex Bot

Adding Intents and Slots

Configuring AWS Lambda

Training Data
The training data used for this project is sourced from the Training Dataset for chatbots/Virtual Assistants provided by Youdata.ai for the HumanAIze Hackathon <FinTech Edition> by Hack2Skill. You can access the dataset here.

Conclusion
This project showcases the integration of AWS Lex and AWS Lambda to create a functional customer service chatbot.

For Future:

We will add more intents for like "payment issue address", "account recovery" and integrating with Generative Ai

