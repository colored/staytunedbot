from subscriber import Subscriber


class Bot():

    def __init__(self, user_id):
        self.user_id = user_id
        self.subscriber = Subscriber(self.user_id)

    #add_subscription
    def follow(self, id):
        self.subscriber.subscriptions.add(id)

    #remove subsription
    def unfollow(self, id):
        self.subscriber.subscriptions.remove(id)

    #gets list of follows
    def get_follows(self):
        return self.subscriber.subscriptions

    def ping(self):
        return "pong"


token = '185643667:AAEBf52dflMY761CHtKIUrPRDSvWXVDTmFw'

import time

import telepot
from telepot.loop import MessageLoop


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])


if __name__ == "__main__":
    TOKEN = '185643667:AAEBf52dflMY761CHtKIUrPRDSvWXVDTmFw'  # sys.argv[1]  # get token from command-line

    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    print('Listening ...')

    # Keep the program running.
    while 1:
        time.sleep(10)
