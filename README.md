<h1 align="center">BUTTON_TELEGRAM_CONNECTOR</h1>

**To establish a bi-directional connection between the IoT device and client app**
 
## INTRODUCTION:
<p style='text-align: justify;'> Create an IoT setup to send messages to the end client upon triggering. As mentioned earlier, the triggering activity will be a button similar to a doorbell. From the end client, the user should be able to send his response back to the IoT device, which will display the message in an 8*8 dot matrix led panel. The time for reconnecting and sending messages should be ideal. The end client chosen was a telegram bot.
 </p>

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

The flow of the project is mentioned below:

<p align="center">
  <img src="https://user-images.githubusercontent.com/114398468/220898884-dc1a2bce-a487-47a5-b821-2cdb071e53fd.png" />
</p>

## WORKING:

<p style='text-align: justify;'>The flow of the project starts with the user pressing the button. The button is programmed in the WIZNET-EVB-PICO 5100 ethernet board in such a way that it will publish a message "Emergency you have to exit" to the MQTT service. This project uses an online MQTT broker with a host and port number. The C program running in the Arduino IDE will send this message and wait for the message received from the client. The MQTT server is subscribed to a "home/telegram" topic. A python program running in the background in such a way that it will receive the MQTT message, and through the obtained API given, it will send a post request, and the message will be posted in the telegram bot. The program will ideally wait to receive the response from the user. Whenever the user sends a message in the bot, the response from the JSON object returned will be fetched by the telegram, and the reply text will be published to the MQTT server under the topic name "home/tel-reply." The C program will receive this message, and the response from the user will be displayed in the dot matrix attached. 
 </p>

## Telegram-API

- Open Telegram and search for the "BotFather" user.
- Start a conversation with "BotFather" and type "/newbot".
- Follow the prompts to give your bot a name and username.
- Once you've created your bot, "BotFather" will send you a message containing your bot's token. The token is a long string of characters that uniquely identifies your bot and is required to authenticate API requests.
- Save your bot's token in a secure place, as you will need to use it to interact with the Telegram Bot API.

For more information click the [link](https://core.telegram.org/api/obtaining_api_id).

## OUTPUT:

The work of the project is included in the below drive link:

https://drive.google.com/file/d/1vEbjrrKSmHvfHqjELyZf71sIHURs_u5y/view?usp=sharing

## REFERENCES:

•	https://core.telegram.org/

•	https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/

•	https://docs.arduino.cc/built-in-examples/digital/Button

•	https://www.youtube.com/watch?v=a37BL0stIuM

##  CONCLUSION:
In conclusion, this project successfully demonstrates the integration of multiple technologies to create an emergency alert system. The flow of the project, from the button press to the display of the user response on the dot matrix, is seamless and efficient. The MQTT service acts as the central messaging broker, while the WIZNET-EVB-PICO 5100 ethernet board, Python program, and Telegram bot API work together to enable quick and reliable communication. This project has the potential to be further developed and implemented in various emergency scenarios, providing a reliable and immediate means of communication.

