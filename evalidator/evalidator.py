import requests
import sys
import json


email = 'someone@email.com'

if email.endswith('@gmail.com'):
    data = {'Email': email}
    response = requests.post('https://accounts.google.com/_/signin/v1/lookup', data=data)
    text = json.loads(response.text)
    is_valid = text['action'] == 'ASK_PASSWORD'
else:
    print('This e-mail service is not supported currently. Please submit an issue on https://github.com/ritiek/email-validator/issues and thank you!')
    sys.exit(1)

if is_valid:
    result = email + ' is a valid e-mail address'
else:
    result = email + ' is an invalid e-mail address'

print(result)
