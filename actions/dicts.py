import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
        Dicttest = dict()
        Dicttest.update({a:{b:c,d:e},f:{g:h,i:j},k:{l:m,n:o}})
        print(Dicttest)
        return(True,Dicttest)