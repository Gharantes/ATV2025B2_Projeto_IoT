#include <Adafruit_Sensor.h>
#include <WiFi.h> 
#include <ArduinoJson.h>
#include "DHT.h"
#include <HTTPClient.h>

#define DHTPIN 4   
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// http://127.0.0.1:8000/data

// http://192.168.1.100:8000/data
const char *dataUrl = "http://10.37.0.191:8000/data";

void setup()
{
  Serial.begin(9600);
  dht.begin();

  WiFi.begin("FAG-ENG", "");
  Serial.print("Conectando ao WiFi");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado.");
}

void loop()
{
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Falha na leitura do sensor!");
  } else {
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;

      http.begin(dataUrl);
      http.addHeader("Content-Type", "application/json");

      StaticJsonDocument<200> doc;
      doc["data"]["temperatura"] = temperature;
      doc["data"]["humidade"] = humidity;

      String body;
      serializeJson(doc, body);

      int code = http.POST(body);
      if (code > 0) {
        Serial.println("Dados enviados: " + http.getString());
      } else {
        Serial.println("Erro ao enviar os dados: " + String(code));
      }

      http.end();
    }
  }

  delay(3000);
}
