import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c,d,e,f,g,h):
        Dicttest = dict{}
        Dicttest[a]=b
        Dicttest[c]=d
        Dicttest[e]=f
        Dicttest[g]=h
        print(Dicttest)
        return(True,Dict)