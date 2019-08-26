import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c,d,e):
        samplelist=list()        
        samplelist.append(a)
        samplelist.append(b)
        samplelist.append(c)
        samplelist.append(d)
        samplelist.append(e)
        
        print(samplelist)
        return(True,samplelist)