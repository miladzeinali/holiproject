import requests
import json



class SmsHandler:

    def __init__(self):
        self.secret_key = '###abbas%^987'
        self.api_key = '91ac6e7a6a16964dfe9f8cbd'
        self.line_number = '30004747472909'


    def get_token(self):
        body = {
            'SecretKey': self.secret_key,
            'UserApiKey': self.api_key,
        }
        header = {
            'Content-Type': 'application/json'
        }
        r = requests.post('https://RestfulSms.com/api/Token', data=json.dumps(body), headers=header)

        token = r.json().get('TokenKey')
        return token

    def send(self, text, mobile, token):
        body = {
            "Messages": [text],
            "MobileNumbers":[mobile],
            "LineNumber": self.line_number,
            "SendDateTime": "",
            "CanContinueInCaseOfError": "false"
        }
        header = {
            'Content-Type': 'application/json',
            "x-sms-ir-secure-token": token
        }

        r = requests.post("https://RestfulSms.com/api/MessageSend", data=json.dumps(body), headers=header).json()

        return r

    def send_verification_code(self, code, mobile, token):
        body = {
            "ParameterArray": [{ "Parameter": "code","ParameterValue": code + ""}],
            "Mobile":mobile,
            "TemplateId": "45518",
        }
        header = {
            'Content-Type': 'application/json',
            "x-sms-ir-secure-token": token
        }
        r = requests.post("https://RestfulSms.com/api/UltraFastSend", data=json.dumps(body), headers=header).json()
        return r

    def send_new_password(self, new_password, mobile, token):
        body = {
            "ParameterArray": [{ "Parameter": "password","ParameterValue": new_password + ""}],
            "Mobile":mobile,
            "TemplateId": "14052",
        }
        header = {
            'Content-Type': 'application/json',
            "x-sms-ir-secure-token": token
        }

        r = requests.post("https://RestfulSms.com/api/UltraFastSend", data=json.dumps(body), headers=header).json()

        return r

    def send_order_code(self, code, mobile, token):
        body = {
            "ParameterArray": [{ "Parameter": "code","ParameterValue": code + ""}],
            "Mobile":mobile,
            "TemplateId": "46182",
        }
        header = {
            'Content-Type': 'application/json',
            "x-sms-ir-secure-token": token
        }
        r = requests.post("https://RestfulSms.com/api/UltraFastSend", data=json.dumps(body), headers=header).json()
        return r

    def send_register_code(self, code, mobile, token):
        body = {
            "ParameterArray": [{ "Parameter": "code","ParameterValue": code + ""}],
            "Mobile":mobile,
            "TemplateId": "47456",
        }
        header = {
            'Content-Type': 'application/json',
            "x-sms-ir-secure-token": token
        }
        r = requests.post("https://RestfulSms.com/api/UltraFastSend", data=json.dumps(body), headers=header).json()
        return r

    def send_forget_code(self, code, mobile, token):
        body = {
            "ParameterArray": [{ "Parameter": "code","ParameterValue": code + ""}],
            "Mobile":mobile,
            "TemplateId": "47457",
        }
        header = {
            'Content-Type': 'application/json',
            "x-sms-ir-secure-token": token
        }
        r = requests.post("https://RestfulSms.com/api/UltraFastSend", data=json.dumps(body), headers=header).json()
        return r

