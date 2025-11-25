#include <Adafruit_Sensor.h>
#include <WiFi.h> 
#include <ArduinoJson.h>
#include "DHT.h"
#include <HTTPClient.h>

#define DHTPIN 4   
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Definindo a URL da API onde os dados seram enviados:
const char *dataUrl = "http://10.37.0.191:8000/data";

// Executado ao iniciar o sistema.
void setup() {
  Serial.begin(9600);
  dht.begin();
  // Se conecta ao Wi-Fi da FAG.
  // "" seria a senha, 
  // mas está vazio porque não tem senha no Wi-Fi.
  WiFi.begin("FAG-ENG", "");
  Serial.print("Conectando ao WiFi");
  // Continua tentando cada 0.5 segundos até conseguir conectar.
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado.");
}

// Executado continuamente.
void loop() {
  // Lê umidade e temperatura.
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Se houve erro ao ler os valores, não faz nada 
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Falha na leitura do sensor!");
  } else {
    // Caso consiga lêr os valores de temperatura e umidade,
    // Verifica se está conectado ao Wi-Fi.
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      // Caso esteja, inicia requisição com a URL definida lá em cima.
      http.begin(dataUrl);
      // Diz que vai estar enviando um JSON ao Backend.
      http.addHeader("Content-Type", "application/json");
      // Monta o JSON.
      StaticJsonDocument<200> doc;
      doc["data"]["temperatura"] = temperature;
      doc["data"]["humidade"] = humidity;
      // Serializa ele.
      String body;
      serializeJson(doc, body);
      // Envia ao Backend. 
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
