import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    def run(self, a,b,c,d,e,f,g,h,i):
        checkstr=a.join(b)
        Dicttest = dict()
        if a.startswith(b):
            Dicttest.update({a:{b:c},d:e,f:g,h:i})
        elif c.startswith(d):
            Dicttest.update({a:b,c:{d:e},f:g,h:i})
        elif e.startswith(f):
            Dicttest.update({a:b,c:d,e:{f:g},h:i})
           
        print(Dicttest)
        return(True,Dicttest)