from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "available after you signup on twilio"
# Your Auth Token from twilio.com/console
auth_token  = "authorization is given"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="enter your registered no. with country code", 
    from_="your twilio number",
    body="Hi there! This is Rajat.")

print(message.sid)
