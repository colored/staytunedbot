from subscriptions import Subscriptions


class Subscriber:
    def __init__(self, subscriber_id):
        self.subscriber_id = subscriber_id;
        self._subscriptions = Subscriptions(subscriber_id)

    @property
    def subscriptions(self):
        return self._subscriptions
