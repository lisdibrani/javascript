#include <Ethernet.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; 
IPAddress ip(192,168,1, 177);
EthernetServer server(80);

void setup()
{
  Ethernet.begin(mac, ip);
  server.begin();
}

void loop()
{
  EthernetClient client = server.available();
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n') {
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          client.println("<h1>Hello World!</h1>");
          client.println("</html>");
          break;
        }
      }
    }
    delay(1);
    client.stop();
  }
}