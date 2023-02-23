# BUTTON_TELEGRAM_CONNECTOR

**To establish a bi-directional connection between the IoT device and client app.**
 
## INTRODUCTION:

Create an IoT setup to send messages to the end client upon triggering. As mentioned earlier, the triggering activity will be a button similar to a doorbell. From the end client, the user should be able to send his response back to the IoT device, which will display the message in an 8*8 dot matrix led panel. The time for reconnecting and sending messages should be ideal. The end client chosen was a telegram bot.

## GROUNDWORKS DONE:
The initial days of the project were used to understand the working of the MQTT server. Studied the MQTT service, Brokers, Port Number, Host Address, etc. I also learned how to use the API, which can be used for endpoint communication with python. Initially, I was trying to use WhatsApp as the end client, but telegram gave me more access to the API than WhatsApp.

## HARDWARE USED:

•	PUSH BUTTON 

•	JUMPER WIRES

•	AURDINO IDE

•	BREADBOARD

•	8*8 DOT MATRIX

•	WIZNET-EVB-PICO 5100 Board

## SERVICES USED:

•	MQTT SERVER (HOST: 54.87.92.106, PORT:1883)

•	TELEGRAM API

## PROGRAMMING LANGUAGES:

•	PYTHON

•	C++

## FLOW CHART OF THE PROJECT:

![image](https://user-images.githubusercontent.com/114398468/220898884-dc1a2bce-a487-47a5-b821-2cdb071e53fd.png)

## WORKING:

The flow of the project starts with the user pressing the button. The button is programmed in the WIZNET-EVB-PICO 5100 ethernet board in such a way that it will publish a message "Emergency you have to exit" to the MQTT service. This project uses an online MQTT broker with a host and port number. The C program running in the Arduino IDE will send this message and wait for the message received from the client. The MQTT server is subscribed to a "home/telegram" topic. A python program running in the background in such a way that it will receive the MQTT message, and through the obtained API given, it will send a post request, and the message will be posted in the telegram bot. The program will ideally wait to receive the response from the user. Whenever the user sends a message in the bot, the response from the JSON object returned will be fetched by the telegram, and the reply text will be published to the MQTT server under the topic name "home/tel-reply." The C program will receive this message, and the response from the user will be displayed in the dot matrix attached. 

## OUTPUT:

The work of the project is included in the below drive link:

https://drive.google.com/file/d/1vEbjrrKSmHvfHqjELyZf71sIHURs_u5y/view?usp=sharing

## REFERENCES:

•	https://core.telegram.org/

•	https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/

•	https://docs.arduino.cc/built-in-examples/digital/Button

•	https://www.youtube.com/watch?v=a37BL0stIuM

