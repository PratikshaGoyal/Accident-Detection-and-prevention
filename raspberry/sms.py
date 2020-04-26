
from twilio.rest import Client 
import get_enum
import nearby_places

def sms(lat, lng):
    x = lat
    y = lng
	# Your Account Sid and Auth Token from twilio.com / console 
    account_sid = 'your account sid'
    auth_token = 'your auth token'
    client = Client(account_sid, auth_token) 

    contacts = nearby_places.contact()

    enum = '+91'+ get_enum.get_contact()
   
    number = [contacts[-2],contacts[-1], enum]
    for i in number:    
        message = client.messages.create( 
                                    body =f'\nNeed Help!!!\nLat: {x} \nLong: {y}',
                                    from_='your twilio number',
                                    to = i
                                  ) 
    print(message.sid) 

# sms()