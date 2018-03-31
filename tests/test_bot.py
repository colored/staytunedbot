import unittest

from bot import Bot


class testBot(unittest.TestCase):
    def setUp(self):
        user_id = "test_user_id"
        self.bot = Bot(user_id)

    def test_ping(self):
        self.assertEquals(self.bot.ping(), "pong")

    def test_add_subscription_artist(self):
        artist_name = "Run The Jewels"
        follow_id = "gdagaga"

        self.bot.follow(follow_id)
        self.bot.get_follows()
        self.assertTrue(follow_id in self.bot.get_follows(), msg="Attempt to follow " + follow_id + " failed")