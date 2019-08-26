import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c,d,e):
        list=[]
        list.append(a)
        list.append(b)
        list.append(c)
        list.append(d)
        list.append(e)
        
        print(list)
        return(True,list)