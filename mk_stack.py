#!/usr/bin/python
#--coding:UTF-8--
class stack:
  def __init__(self):
    self.item = []

  def isEmpty(self):
    return self.item == []

  def push(self,m):
    self.item.append(m)
  
  def pop(self):
    #if self.isEmpty is  True:  wrong :miss (); 
    if self.isEmpty() is  True:
    #if self.item == []:
      return "this stack has empty"
    else:
      return self.item.pop()
  def peek(self):
    if self.isEmpty() is  True :
    #if self.item == []:
      return "stack has nothing!"
    else:
      return self.item[len(self.item)-1] 

  def size(self):
    return len(self.item)






if __name__ == "__main__":
  s=stack()
  if s.isEmpty :
    print "this stack is empty!"
  else:
    print s.size 
  s.push(123)
  s.push(44)
  s.push("你好！")
  if  s.isEmpty == True :
    print "this stack is empty!"
  else:
    print s.size() 
  print s.peek()
  s.pop()
  print(s.peek())
  s.pop()
  print s.peek()
  s.pop()
  print(s.peek())
  s.pop()
