import sys
from st2common.runners.base_action import Action
import requests

class MyAction(Action):
    def run(self):
        req = requests.get('https://github.com/timeline.json')
        print(req)
        return(True,req)