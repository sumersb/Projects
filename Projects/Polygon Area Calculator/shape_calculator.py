class Rectangle:

  def __init__(self,wideness,heightness):
    self.width=wideness
    self.height=heightness

  def set_width(self,wideAdjust):
    self.width=wideAdjust

  def set_height(self,heightAdjust):
    self.height=heightAdjust

  def get_area(self):
    area=self.height*self.width
    return area

  def get_perimeter(self):
    perimeter=2*self.height+2*self.width
    return perimeter

  def get_diagonal(self):
    diagonal=((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    else:
      picture=''
      for i in range(self.height):
        picture+='*'*self.width+'\n'
        return picture
    
  def get_amount_inside(self):
    wideFitness='x'

  def __str__(self):
    return 'Rectangle(width='+str(self.width)+', height='+str(self.height)+')'

  def get_amount_inside(self,shape):
    sideA=shape.width
    sideB=shape.height
    wideFit=self.width//(sideA)
    heightFit=self.height//(sideB)
    totalFit=wideFit*heightFit
    return totalFit
    

class Square(Rectangle):

  def __init__(self,sides):
    self.width=sides
    self.height=sides

  def __str__(self):
    return 'Square(side='+str(self.width)+')'

  def set_side(self,sider):
    self.width=sider
    self.height=sider
