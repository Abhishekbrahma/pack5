import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a):
        for num range(a):
            print(num)
        return(True,a)