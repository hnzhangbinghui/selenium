from twilio.rest import TwilioRestClient
accountSID='ACCOUNT SIDACd2a74fbc2fae25d1aa3cff39c78e42b2'
autoToken='0620d65a95d8e8d45bf3f3ee276e3d53'
twilioCli=TwilioRestClient(accountSID,autoToken)
myTwilioNumber='+15239687008'
myCellphone='+8613683087698'
message=twilioCli.messages.create(to=myCellphone,from_=myTwilioNumber,body='hello')
print(message.sid)