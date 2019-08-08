from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Axx"
# Your Auth Token from twilio.com/console
auth_token  = "nono"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+gebe", 
    from_="+15017250604",
    body="Hello Berlin!")

print(message.sid)
