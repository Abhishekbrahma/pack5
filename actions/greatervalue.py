import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c):
        max=0
        if a>b and a>c:
           max=a
        elif b>a and b>c:
            max=b
        else:
           max=c
        print("greater value is :{}".format(max))
        print("greater value is :" +str(max))
        return(True,max)