import pywhatkit
import json

contacts_path =  '/home/moustache/Documents/Donkey/app_pykit/contacts.json'

with open(contacts_path, 'r') as file:
            contact_data = json.load(file)
            
minutes = 00
for key  in contact_data:
    print(key['nom'])  
    
    pywhatkit.sendwhatmsg( key['numero'], 'Hello '+key['nom'], 15, minutes)
    minutes += 2
    
print('done')