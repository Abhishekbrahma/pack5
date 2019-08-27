import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a):
        for num in range(a):

            print(num,end=" ")
        return(True,a)