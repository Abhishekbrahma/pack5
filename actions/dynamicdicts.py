import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    def run(self, a,b,c,d,e,f,g,h,i):
        Dicttest = dict()
        if b in a:
            Dicttest.update({a:{b:c},d:e,f:g,h:i)
        elif d in a:
            Dicttest.update({a:{d:e},b:c,f:g,h:i)
        elif f in a:
             Dicttest.update({a:{f:g},b:c,d:e,h:i)
        elif h in a:
             Dicttest.update({a:{h:i},b:c,d:e,f:g)
        print(Dicttest)
        return(True,Dicttest)