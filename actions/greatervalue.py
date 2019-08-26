import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a):
        if a>6:
            for num in range(a):
                for i in range(num):
                print (num, end="")
                print("\n")
        else:
        print("data will be greater than 6")
        return(True,a)       