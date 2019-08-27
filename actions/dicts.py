import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c,d,e,f,g,h):
        Dicttest = dict{}
        Dicttest.update(a,b)
        print(Dicttest)
        return(True,Dict)