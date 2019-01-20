class parent:
    parentattr=100
    def __init__(self):
        print("Calling Parent Constructor")
    def parentmethod(self):
        print("Calling Parent Method")
    def setattr(self,attr):
        parent.parentattr=attr
    def getattr(self):
        print("Parent Attribute: ",parent.parentattr)

class child(parent):
    def __init__(self):
        print("Calling Child Constructor")
    def childmethod(self):
        print("Calling Child Method")

c=child()
c.childmethod()
c.parentmethod()
c.setattr(20)
c.getattr()
