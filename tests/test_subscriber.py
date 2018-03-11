import unittest

from artist import Artist
from subscriber import Subscriber


class testSubscriber(unittest.TestCase):
    def setUp(self):
        self.subscriber = Subscriber("fake_id")

    def test_subscribe_to_artist(self):
        fake_artist_name = "fake_artist"
        self.subscriber.subscribe_to(Artist(fake_artist_name))
        self.assertEquals(self.subscriber.subscriptions.artists[0].artist_name, fake_artist_name)

    def test_unsubscribe_from_artist(self):
        fake_artist_name = "fake_artist"
        self.subscriber.subscribe_to(Artist(fake_artist_name))
        self.subscriber.unsubscribe_from(Artist(fake_artist_name))
        self.assertEquals(len(self.subscriber.subscriptions), 0)
