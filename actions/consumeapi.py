import sys
from st2common.runners.base_action import Action
import requests

class MyAction(Action):
    def run(self):
        reqmsg = requests.get('https://github.com/timeline.json')
        print(reqmsg)
        return(True,reqmsg)