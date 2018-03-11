from subscription import Subscription


class Artist(Subscription):
    def __init__(self, artist_name):
        super(Artist, self).__init__(artist_name, "artist")
