import requests
my_token = '7ZiFvN6GbYu4ouUM7lcf'


def send_code(code,phonenumber):
    url = 'https://api.oursms.com/msgs/sms'
    headers = {
        'Authorization': f'Bearer {my_token}',
        'Content-Type': 'application/json',
    }
    data = {
            "src": "oursms",
            "body": f'رمز التحقق الخاص بك هو {code}',
            "dests": [phonenumber]
    }
    requests.post(url , headers=headers , json=data)



def send_password(phonenumber,password):
    url = 'https://api.oursms.com/msgs/sms'
    headers = {
        'Authorization': f'Bearer {my_token}',
        'Content-Type': 'application/json',
    }
    data = {
            "src": "oursms",
            "body": f'كلمة المرور الخاصة بك هي {password}',
            "dests": [phonenumber]
    }
    requests.post(url , headers=headers , json=data)
