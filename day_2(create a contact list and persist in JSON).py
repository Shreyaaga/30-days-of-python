#CREATE A CONTACT LIST  AND PERSIST IN JSON FILE
import json
filename='new.json'

contact_dict={}
n= int(input("number of contacts u want to save:"))

for i in range(n):
    name=input("enter the name:")
    contact_number=int(input("enter the contact number"))
    contact_dict.update({name:contact_number})

records=json.dumps(contact_dict)
with open('new.json','w') as f:
    f.write(records)
    f.close()

with open("new.json", "w") as outfile:
    json.dump(contact_dict, outfile)
