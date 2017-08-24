import requests
import sys
import json
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Checks if an e-mail address exists or not ')

    parser.add_argument(
        'email',
        metavar='EMAIL',
        type=str,
        help='e-mail to check')

    return parser.parse_args()


def google_mail(email):
    data = {'Email': email}
    response = requests.post('https://accounts.google.com/_/signin/v1/lookup', data=data)
    text = json.loads(response.text)
    is_valid = text['action'] == 'ASK_PASSWORD'
    return is_valid


def validate(email):
    if email.endswith('@gmail.com'):
        is_valid = google_mail(email)
    else:
        is_valid = None
    return is_valid


def command_line():
    args = get_arguments()
    email = args.email

    is_valid = validate(email)

    if is_valid is True:
        result = email + ' is a valid e-mail address'
    elif is_valid is False:
        result = email + ' is not a valid e-mail address'
    else:
        result = 'This e-mail service is not supported currently. Please submit an issue on https://github.com/ritiek/email-validator/issues and thank you!'

    print(result)


if __name__ == '__main__':

    command_line()
