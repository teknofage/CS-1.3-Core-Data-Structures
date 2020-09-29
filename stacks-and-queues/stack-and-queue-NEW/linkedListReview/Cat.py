#from linkedlist import LinkedList

#my_ll = LinkedList()

#
class Cat:

  def __init__(self, cat_age , cat_says, is_sleeping):

    self.age = cat_age
    self.says = cat_says
    self.is_sleeping = is_sleeping
    self.is_fluffy = True

  def eat(self, food):
    return "I am eating: " + food
  
  def is_fluffy_method(self):
    print(self.is_fluffy)

#composition, class that is composed of other classes

class CrazyCatLadyHouse:

  def __init__(self, cats_list):
    self.cats_list = cats_list


cats = [Cat(5, "Meow", True), Cat(10, "Meep", False), Cat(2, "Mrow", True)]

cat_lady_house = CrazyCatLadyHouse(cats)
print(cat_lady_house.cats_list)




