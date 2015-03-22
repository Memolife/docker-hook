from docker import Client
import slack

c = Client(base_url='unix://var/run/docker.sock')
for event in c.events:
    msg = ""
    for key in event.keys():
        msg = "%s: %s\n".format(key, event[key])
    slack.msg(msg)
