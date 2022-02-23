import requests, time
import skhst_tkinter_try
threshold_temp = 30.0
while(True):
    msg=requests.get("https://thingspeak.com/channels/1361501/field/1")
    msg=msg.json()['feeds'][-1]['field1']
    temp_reading = float(str(msg).strip())
    print(temp_reading)
    if(temp_reading>threshold_temp):
        skhst_tkinter_try.main(temp_reading)
        break
print('Restart the service..')