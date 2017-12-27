from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa2d3c3bc3e5ff27f0e3fe04af739aa3a"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309", 
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
