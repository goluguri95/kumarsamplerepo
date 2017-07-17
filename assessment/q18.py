class listadjust:
    def __init__(self,l):
        self.l=l
    def getappend(self,x):
        return self.l.append(x)
    def getdelete(self,x):
        return self.l.remove(x)
    def getdisplay(self):
        return self.l

lists=listadjust([3,4,5])
lists.getdelete(5)
lists.getappend(9)
k=lists.getdisplay()
print(k)
