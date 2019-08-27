import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c,d,e,f,g,h):
        Dict = {}
        print(Dict)
        Dict[a]=b
        return(True,Dict)