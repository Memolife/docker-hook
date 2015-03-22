import requests
import config

def msg(msg):
    url = config.SLACK_URL
    r = requests.post(url, msg)
