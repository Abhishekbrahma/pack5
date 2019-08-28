import sys
from st2common.runners.base_action import Action
import requests

class MyAction(Action):
    def run(self):
        reqmsg = requests.get('http://api.open-notify.org/iss-now.json')
        print(reqmsg.status_code)
        return(True,reqmsg)