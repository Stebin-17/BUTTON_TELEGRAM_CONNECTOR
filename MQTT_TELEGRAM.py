import time

import telegram
import paho.mqtt.client as mqtt

global flag
flag=True

from telegram.ext import Updater, MessageHandler, Filters

# Initialize the telegram bot
bot = telegram.Bot('588*********************VOPU55jeDQhiVj_ea8LGbA')

def message_handler(update, context):
    user_message = update.message.text[:200]
    print("USER_REPLIED: "+user_message)

    if  user_message.lower!="exit":
        flag=False;
    second_client = mqtt.Client()
    second_client.connect('54.87.92.106', 1883)
    second_client.subscribe("home/tel-reply")
    second_client.publish("home/tel-reply", user_message)
    second_client.loop_start()
    X=Updater.last_update_id
    if X==Updater.last_update_id:
        flag=False;

def first_mqtt_on_connect(client, userdata, flags, rc):
    client.subscribe("home/telegram")


def first_mqtt_on_message(client, userdata, msg):
    received_message = msg.payload.decode()
    print("DEVICED ENQUIRED: "+received_message)
    bot.send_message(chat_id='778996496', text=received_message)



def main(first_mqtt_host, first_mqtt_port, second_mqtt_host, second_mqtt_port):
    first_client = mqtt.Client()
    first_client.connect(first_mqtt_host, first_mqtt_port)
    first_client.on_connect = first_mqtt_on_connect
    first_client.on_message = first_mqtt_on_message
    first_client.loop_start()
    updater = Updater(token='5881496177:AAFkxzUugfC0qVOPU55jeDQhiVj_ea8LGbA', use_context=True)

    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(filters=Filters.all,callback=message_handler))
    updater.start_polling()
    # updater.idle

if __name__ == '__main__':
    main('54.87.92.106', 1883, '54.87.92.106', 1883)
