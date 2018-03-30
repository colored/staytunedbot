import time

import telepot
from telepot.loop import MessageLoop


class Bot:
    def __init__(self):
        self.TOKEN = '185643667:AAEBf52dflMY761CHtKIUrPRDSvWXVDTmFw'  # sys.argv[1]  # get token from command-line
        self.bot = telepot.Bot(self.TOKEN)

    #add_subscription
    def follow(self, id):
        pass

    #remove subsription
    def unfollow(self, id):
        pass

    #gets list of follows
    def get_follows(self):
        return []

    def run(self):
        MessageLoop(self.bot, self.handle).run_as_thread()
        print('Listening ...')

        # Keep the program running.
        while 1:
            time.sleep(10)

    def handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)
        if content_type == 'text':
            self.bot.sendMessage(chat_id, msg['text'])


if __name__ == "__main__":
    bot = Bot()
    bot.run()
