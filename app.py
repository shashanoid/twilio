import os
import sys
import json
from twilio.rest import Client


def main():
    client = Client(
        os.getenv('ACCOUNT'),
        os.getenv('TOKEN')
    )

    message = client.messages.create(
        to=sys.argv[1],
        from_=sys.argv[2],
        body=sys.argv[3]
    )

    message._properties['date_created'] = str(message._properties['date_created'])
    message._properties['date_updated'] = str(message._properties['date_updated'])

    return message._properties


if __name__ == '__main__':
    sys.stdout.write(json.dumps(main()))
