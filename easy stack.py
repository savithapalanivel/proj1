class stack
  def__init__(self,dataval):
    self.stack=[]
  def add(self,dataval):
     self.stack.append(dataval)
  def peek(self):
     return self.stack[-1]
  def printi(self):
     print(self.stack)
    
  def remove(self):
     if len(self.stack)<=0:
      return("no element")
     else: r
      return self.stack.pop()
s=stack()
s.add(110)
s.add(120)
s.add(65)
print(s.peek())
s.printi()
s.remove()             
s.printi()
