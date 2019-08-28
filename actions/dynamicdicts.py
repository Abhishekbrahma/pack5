import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    def run(self, a,b,c,d,e,f,g,h,i):
        Dicttest = dict()
        if a.find(b):
             Dicttest.update({a:{b:c},d:e,f:g,h:i)
           
        print(Dicttest)
        return(True,Dicttest)