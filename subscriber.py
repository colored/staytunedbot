from subscriptions import Subscriptions


class Subscriber:
    def __init__(self, subscriber_id):
        self.subscriber_id = subscriber_id;
        self.subscriptions = Subscriptions.get_subscriptions(subscriber_id)

    def subscribe_to(self, subscription):
        self.subscriptions.add(subscription)

    def unsubscribe_from(self, subscription):
        self.subscriptions.remove(subscription)
