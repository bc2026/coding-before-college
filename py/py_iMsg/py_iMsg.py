from py_imessage import imessage

phone = "4049530628"
msg = "hello"


guid = imessage.send(phone,"I love you")
# Let the recipient read the message
resp = imessage.status(guid)
print(f'Message was read at {resp.get("date_read")}')