import os
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token="xoxb-2538212706071-2566324247489-uD06b3SlceDo675fWb4k1NiP")

if __name__ == "__main__":
    SocketModeHandler(app, "xapp-1-A02GB9DJ5PW-2576821471776-4f5a3c562bee463a5c85caf44e9823b89a023476dfe931b1542bf7f7e6f53e9f").start()