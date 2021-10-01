import os
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

@app.command("/carpool1")
def handle_some_command(ack, body, logger, say):
    ack()
    logger.info(body)
    say('hello from carpool1')

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()



    