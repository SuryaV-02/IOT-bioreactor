#define L_RED D2
#define L_BLUE D3
#define L_GREEN D4
#define BUZZER D8
#define DHTTYPE DHT11
#define DHTPORT 1
#define THRESHOLD_TEMP 30.0

#include "DHT.h"
#include <ESP8266WiFi.h>
String api_key = "QV4XH5MD76YRMA4J";     //  Enter your Write API key from ThingSpeak
const char *ssid =  "Skhst";     // replace with your wifi ssid and wpa2 key
const char *pass =  "test@12345";
const char* server = "api.thingspeak.com";

WiFiClient client;
DHT dht(5,DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  dht.begin();
  Serial.begin(115200);  
  pinMode(L_GREEN,OUTPUT);
  pinMode(L_RED,OUTPUT);
  pinMode(L_BLUE,OUTPUT);
  pinMode(BUZZER,OUTPUT);
  digitalWrite(L_GREEN,HIGH);
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) 
     {
            delay(500);
            Serial.print(".");
     }
      Serial.println("");
      Serial.println("WiFi connected");
  acknowledge(100,1,1);

}

void acknowledge(int freq, int count,int interval){
  for(int j = 0; j<count; ++j){
    for(int i= 0 ; i<2 ; ++i){
    digitalWrite(BUZZER,HIGH);
//    float delay_time = round(signals[i]*1000);
    delay(freq);
    digitalWrite(BUZZER,LOW);
    delay(50);
  }
  delay(interval*1000);
  }
//  digitalWrite();
}

void enterAlertingPhase(float humidity, float temperature){
  Serial.println("Entering Alert phase!!!");
  digitalWrite(L_GREEN,LOW);
  while(temperature>THRESHOLD_TEMP){
    humidity = dht.readHumidity();
    temperature = dht.readTemperature();
    digitalWrite(L_RED,HIGH);
    digitalWrite(BUZZER,HIGH);
    delay(100);
    digitalWrite(L_RED,LOW);
    digitalWrite(BUZZER,LOW);
    digitalWrite(L_BLUE,HIGH);
    delay(100);
    digitalWrite(L_BLUE,LOW);
    Serial.println(temperature);
    
  }
  digitalWrite(L_GREEN,HIGH);
  acknowledge(50,1,1);
  Serial.println("Entering Cooldown..");
}

void write_to_thingspeak(float h, float t){
                 if (client.connect(server,80))   //   "184.106.153.149" or api.thingspeak.com
            {  
                   String data_to_send = api_key;
                    data_to_send += "&field1=";
                    data_to_send += t;
                    data_to_send += "&field2=";
                    data_to_send += h;
                    data_to_send += "\r\n\r\n";

                   client.print("POST /update HTTP/1.1\n");
                   client.print("Host: api.thingspeak.com\n");
                   client.print("Connection: close\n");
                   client.print("X-THINGSPEAKAPIKEY: " + api_key + "\n");
                   client.print("Content-Type: application/x-www-form-urlencoded\n");
                   client.print("Content-Length: ");
                   client.print(data_to_send.length());
                   client.print("\n\n");
                   client.print(data_to_send);
                   delay(1000);
                   Serial.print("Temperature: ");
                   Serial.print(t);
                   Serial.print(" degrees Celcius, Humidity: ");
                   Serial.print(h);
                   Serial.println("%. Send to Thingspeak.");
              }
          client.stop();
 
          Serial.println("Waiting...");
  
  // thingspeak needs minimum 15 sec delay between updates, i've set it to 30 seconds
  delay(10000);
}

void loop() {
  // put your main code here, to run repeatedly:
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  Serial.print(temperature);
  Serial.println(humidity);
  write_to_thingspeak(humidity, temperature);
  if(temperature>THRESHOLD_TEMP){
    enterAlertingPhase(humidity,temperature);
    delay(500); 
    
  }
  delay(1000);
}
