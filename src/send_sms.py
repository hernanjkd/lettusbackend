from twilio.rest import Client

def send_msg(number, msg):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.environ.get('TWILIO_ACCOUN')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Lettus Notification: Water your crop and turn on the lights!",
                        from_='+16198212180',
                        to='+13053324995'
                    )

    print(message.sid)