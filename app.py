import os
import sys
import json
from twilio.rest import Client


class Twilio:
    @staticmethod
    def client():
        return Client(os.getenv('ACCOUNT'), os.getenv('TOKEN'))

    @staticmethod
    def sms(to, from_, body):
        message = Twilio.client().messages.create(
            to=to, from_=from_, body=body
        )

        message._properties.update({
            'date_created': str(message._properties['date_created']),
            'date_updated': str(message._properties['date_updated'])
        })

        return message._properties


if __name__ == '__main__':
    res = getattr(Twilio, sys.argv[1])(*sys.argv[2:])
    sys.stdout.write(json.dumps(res))
