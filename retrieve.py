import requests
import skhst_tkinter_try
msg=requests.get("https://thingspeak.com/channels/1361501/field/2")
msg=msg.json()['feeds'][-1]['field2']
print("The Message sent was: " + str(msg).strip())

skhst_tkinter_try.main