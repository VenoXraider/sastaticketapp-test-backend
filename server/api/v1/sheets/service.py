import gspread
import os

class AuthService():

    SAMPLE_SPREADSHEET_ID = "1Joyw5VXn3SJDwk_Cmnca_k-jyY-lijmrQGnCSYRz5wI"

    def __init__(self):
        self.googlePrivatekey = os.environ.get('GOOGLE_PRIVATE_KEY')
        self.clientEmail = os.environ.get('GOOGLE_CLIENT_EMAIL')
        self.emailTokenUri = os.environ.get('GOOGLE_TOKEN_URI')

    def getSheetsRouter(self, payload):
        try:

            service_account = gspread.service_account(filename="service_account.json")
            sheet = service_account.open('Testing')
            worksheet = sheet.worksheet('test')
            
            print(worksheet.get('A2:D'))

            return "OK"

        except Exception as e:
            print(e)
            return "ERROR"

    def sendEmail(self, payload):
        try:
            service = get_gmail_service()

            sender = 'muhammadmoiz0087@gmail.com'
            to = payload['Email']
            subject = payload['Subject']
            body = payload['Body']

            message = create_message(sender, to, subject, body)
            sent_message = service.users().messages().send(userId='me', body=message).execute()

            return f'Successfully sent email! Message ID: {sent_message["id"]}'

        except Exception as e:
            print(e)
            return "ERROR"