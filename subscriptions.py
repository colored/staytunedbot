class Subscriptions:
    def __init__(self, subscriber_id):
        self.subscriber_id = subscriber_id
        self.subscriptions = set()

    @property
    def artists(self):
        return [subscription for subscription in self.subscriptions if subscription.type == "artist"]

    def add(self, subscription):
        self.subscriptions.add(subscription)

    def remove(self, subscription):
        to_remove = set()
        for subscr in self.subscriptions:
            if subscr.name == subscription.name:
                to_remove.add(subscr)
        self.subscriptions = self.subscriptions.difference(to_remove)

    def __len__(self):
        return len(self.subscriptions)

    @classmethod
    def get_subscriptions(cls, subscriber_id):
        pass
