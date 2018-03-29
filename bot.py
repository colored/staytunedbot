class Bot():

    def __init__(self, user_id):
        self.user_id = user_id

    #add_subscription
    def follow(self, id):
        pass

    #remove subsription
    def unfollow(self, id):
        pass

    #gets list of follows
    def get_follows(self):
        return []


token = '185643667:AAEBf52dflMY761CHtKIUrPRDSvWXVDTmFw'

import time

import telepot
from telepot.loop import MessageLoop


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])


TOKEN = '185643667:AAEBf52dflMY761CHtKIUrPRDSvWXVDTmFw'  # sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
