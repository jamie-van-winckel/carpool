import os
from collections import defaultdict
import json
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

cache = defaultdict(list)

with open('user_zips.json', 'r') as userZips_fp:
    cache = json.load(userZips_fp)


@app.command("/carpool1")
def carpool1_handler(ack, body, say):
    ack()
    say("Hello " + body['user_name'] + '!')


    cache[body['text']].append(body['user_name']) 
    #save the users to a file
    with open('user_zips.json', 'w') as userZips_fp:
        json.dump(cache, userZips_fp, sort_keys=True, indent=4)


    if (len(cache[body['text']]) < 2):
        say("You are the only person carpooling in " + body['text'])
    else:
        say('You are close to:')
        for u in cache[body['text']]:
            if (u != body['user_name']):
                say(u)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()




