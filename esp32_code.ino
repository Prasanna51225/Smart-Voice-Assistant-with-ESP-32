#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Hello";
const char* password = "pk123456";
WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("ESP32 IP Address: ");
  Serial.println(WiFi.localIP());

  server.begin();
}

void loop() {
  WiFiClient client = server.available();  // Listen for incoming connections
  if (client) {
    String message = client.readStringUntil('\n');  // Read incoming command
    Serial.println("Received command: " + message);

    // Encode space to %20
    String encodedMessage = message;
    encodedMessage.replace(" ", "%20");  // Replace spaces with %20

    // Send received command to Python server via HTTP
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      String serverURL = "http://192.168.48.72:5000/command?cmd=" + encodedMessage;  // Your PC IP with the port used by Python server
      http.begin(serverURL);  // Initialize HTTP connection
      int httpResponseCode = http.GET();  // Send GET request with command

      if (httpResponseCode > 0) {
        Serial.println("Command sent successfully!");
      } else {
        Serial.println("Error sending command");
      }
      http.end();  // Close connection
    }
  }
}