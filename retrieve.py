import requests, time
import skhst_tkinter_try
while(True):
    msg=requests.get("https://thingspeak.com/channels/1361501/field/1")
    msg=msg.json()['feeds'][-1]['field1']
    temp_reading = float(str(msg).strip())
    print(temp_reading)
    if(temp_reading>29.0):
        skhst_tkinter_try.main()
        break
print('Restart the service..')