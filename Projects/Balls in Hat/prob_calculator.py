import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self,**balls):
    self.hatter=balls
    self.contents=[]
    self.total=sum(self.hatter.values())
    for key,value in self.hatter.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self,count):
    ballsremoved=[]
    if count>len(self.contents):
      copyList=copy.deepcopy(self.contents)
      self.contents=[]
      return copyList
    for i in range(count):
      index=random.randint(0,(len(self.contents)-1))
      ballRemoved=self.contents.pop(index)
      ballsremoved.append(ballRemoved)
    return ballsremoved

  def testdraw(self,count):
    ballsremoved=[]
    copyList=copy.deepcopy(self.contents)
    if count>=len(copyList):
      return copyList
    for i in range(count):
      index=random.randint(0,(len(copyList)-1))
      ballRemoved=copyList.pop(index)
      ballsremoved.append(ballRemoved)
    return ballsremoved  


def experiment(hat, expected_balls, num_balls_drawn, num_experiments): 
  fails=0
  for experiment in range(num_experiments):
    test=hat.testdraw(num_balls_drawn)
    for key in expected_balls.keys():
      if expected_balls[key]<=test.count(key):
        continue
      else:
        fails+=1
        break
  success=num_experiments-fails  
  print(success)
        
  return success/num_experiments
