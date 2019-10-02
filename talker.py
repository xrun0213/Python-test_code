import time

import roslibpy

client = roslibpy.Ros(host='10.1.1.3', port=9090)
talker = roslibpy.Topic(client, '/chatter', 'std_msgs/String')


def start_talking():
    while client.is_connected:
        talker.publish(roslibpy.Message({'data': 'talker form mac!'}))
        print('Sending message...')
        time.sleep(1)

    talker.unadvertise()


client.on_ready(start_talking)
client.run_forever()