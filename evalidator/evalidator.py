import requests
import sys
import json
import argparse


email = 'someone@email.com'

def google_mail(email):
    data = {'Email': email}
    response = requests.post('https://accounts.google.com/_/signin/v1/lookup', data=data)
    text = json.loads(response.text)
    is_valid = text['action'] == 'ASK_PASSWORD'
    return is_valid


def valididate(email):
    if email.endswith('@gmail.com'):
        is_valid = google_mail(email)
    else:
        raise()
    return is_valid


def command_line():
    is_valid = validate(email)

    if is_valid:
        result = email + ' is an invalid e-mail address'
    elif is_valid:
        result = email + ' is a valid e-mail address'
    else:
        result = 'This e-mail service is not supported currently. Please submit an issue on https://github.com/ritiek/email-validator/issues and thank you!'

    print(result)
