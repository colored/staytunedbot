from subscriptions import Subscriptions


class Subscriber:
    def __init__(self, subscriber_id):
        self.subscriber_id = subscriber_id;
        self.subscriptions = Subscriptions(subscriber_id)

    def subscribe_to(self, subscription):
        self.subscriptions.append(subscription)

    def unsubscribe_from(self, subscription):
        self.subscriptions.remove(subscription)
