
import time
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)


def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def speedy_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.001)
def insanelyfast_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.0001)








class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   PINK= '\033[35m'
   WHITE='\033[97m'
   BlACK='\033[31m'
   FLASH='\033[5m'
   IDK='\033[13m'



class Item():
  def __init__(self,name,display,description,value,hp):
    self.name = name
    self.display=display
    self.description = description
    self.value = value
    self.hp= hp 
  def __str__(self):
    return self.name
  def details(self):
    return"{}\n=========\n{}\n==========\nVALUE: {} HP: {}".format(self.name, self.description,self.value,self.hp)
class Scroll():
  def __init__(self, name,display,call,text):
    self.name=name
    self.display=display
    self.call=call
    self.text=text
  def read(self):
    return self.text

    
class Weapon():
  def __init__(self,name,display,description,value,damage):
    self.name = name
    self.display=display
    self.description = description 
    self.value=value
    self.damage=damage
     
  def __str__(self):
    return self.name
  def details(self):
    return"{}\n=========\n{}\n==========\nDAMAGE: {} VALUE: {}".format(self.name, self.description,self.damage,self.value)

class Enemy():
  def __init__(self, name,display,items,battlecry,damage,hp):
    self.name = name
    self.display=display
    self.items=items
    self.battlecry=battlecry
    self.damage=damage
    self.hp=hp
  def isalive(self):
    return self.hp>0
  def isdead(self):
    return self.hp<=0
class Riddle():
  def __init__(self,question,answer):
    self.question=question
    self.answer=answer
  def askq(self):
    delay_pdrint self.question


    

class Player():
  def __init__(self,name,hp,damage,items,gold,weaponslot):
    self.name=name
    self.hp=hp
    self.damage=damage
    self.items=items
    self.gold=gold
    self.weaponslot=weaponslot
  def isdead(self):
    return self.hp<=0
    exit()
  def inventory(self):
    print (color.YELLOW)
    if len(self.items)>0 :
      delay_print("\nYou currently have:\n")
      for item in self.items:
        delay_print(str(item.display)+", ")
      delay_print("\n")
    else:
      delay_print("\nYou currently have nothing in your inventory.\n")
    if self.gold>=0:
      delay_print("\nThere is {} gold in your bag.\n".format(self.gold))
    if len(self.weaponslot)==0:
      delay_print("\nYou have no weapon equipped\n")
    else: 
      delay_print("\nIn your hand is a ")
      for item in self.weaponslot:
        delay_print(item.display+"\n")
    print(color.END)
  def equipweapon(self):
    
    for item in self.items:
      if hasattr(item,'damage'):
        self.weaponslot.append(item)
        delay_print("You equipped a {}.\n".format(item.name))
        return
  
    for item in self.items:
      if hassat(item,'hp'):
        delay_print("You can't equip that.") 
  def unequipweapon(self):
    if len(self.weaponslot)>0:
      for item in self.weaponslot:
        self.weaponslot.remove(item)
        delay_print("You unequipped a {}.\n".format(item.name))
        return
    else: 
      delay_print("You have no weapon equipped")
      return


  def __str__(self):
    return self.name
    

class NPC():
  def __init__(self, name,display,items,greeting,info):
    self.name = name
    self.display=display
    self.items=items
    self.greeting=greeting
    self.info=info
  def __str__(self):
    return self.name
  def sellitem(self):
    for item in self.items:
      ite=parts[0]
      if ite==str(item) and p.gold>=item.value:
        p.item.append(item)
        p.gold=p.gold-item.value

  def dropitem(self):
    for item in room['npcitems']:
      if item.name=="scroll" or "key":
        room['items'].append(item)
        room['npcitems'].remove(item)
