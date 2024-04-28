import requests


def send_code(self,code,phonenumber):
    url = 'https://api.oursms.com/msgs/sms'
    headers = {
        'Authorization': 'Bearer my_token',
        'Content-Type': 'application/json',
    }
    data = {
            "src": "oursms",
            "body": f'رمز التحقق الخاص بك هو {code}',
            "dests": [phonenumber]
    }
    requests.post(url , headers=headers , json=data)



def send_password(self,phonenumber,password):
    url = 'https://api.oursms.com/msgs/sms'
    headers = {
        'Authorization': 'Bearer my_token',
        'Content-Type': 'application/json',
    }
    data = {
            "src": "oursms",
            "body": f'رمز التحقق الخاص بك هو {password}',
            "dests": [phonenumber]
    }
    requests.post(url , headers=headers , json=data)
