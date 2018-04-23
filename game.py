"""TODO:
-ORGANIZE AND IMPLEMENT DEF AND CLASS IMPORTS
-IMPLEMENT REQUIREMENTS FOR ROOMS
-RIDDLES
-KEYS?"""



map=[]
room = None
loot=[]
weap=[]

import time
import sys
import random
from classes  import color,Item,Scroll,Weapon,Enemy,Player,NPC,delay_print,slow_print,speedy_print,insanelyfast_print
print(color.END)
print (color.IDK)

name=raw_input(color.FLASH+"USERNAME:"+color.END)
name=name.strip()
name=name.lower()
p=Player(str(name),10,0,loot,5,weap)

def admintools():
	pass

def username():

  if name== "daniel":
    slow_print("\nu cute\n")
    p.gold=p.gold+100
    slow_print("Welcome to your adventure, "+name)
  elif name== "quit":
    exit()
  elif name=="mark":
    delay_print("INCORRECT\n\n\n\n......just kidding\nACCESS GRANTED")
  elif name=="robinett":
    item=Item("pixel","a pixel","It looks as if it has seen many an adventure",999,999)
    p.items.append(item)
    slow_print("Welcome to your adventure, "+name)
  elif name=="parzival":
    item=Item("credit","An Arcade Token","It says 'Gregarious Games' on it. You wonder what it could do?",1,0)
    p.items.append(item)
    slow_print("say hi to Aech and Arty for me, P.\n")
  elif len(name)>0:
    slow_print("Welcome to your adventure, "+name)
  else:
    delay_print("That name won't work. Try again\n")
    user=username()
    return user
"""
delay_print("dedicated to warren robinett\n")
delay_print("PLEASE PLAY IN FULLSCREEN FOR GRAPHIC FORMATTING PURPOSES\n")
slow_print("R E A D Y\n")
time.sleep(1)
slow_print("P L A Y E R\n")
time.sleep(1)
slow_print("O N E\n")
time.sleep(1)
delay_print("01101101\n01100001\n01100100\n01100101\n01100010\n01111001\n01100100\n01100001\n01101110\n01101001\n01100101\n01101100\n01110011\n01110100\n01101111\n01101110\n01100101\n01110100\n01101000\n01100101\n01101111\n01110010\n01101001\n01100111\n01101001\n01101110\n01100001\n01101100\n01100100\n01100001\n01110010\n01101011\n01110011\n01110000\n01110101\n01110010")

"""

username()

def shop(choice):

  if choice=="yes":
      if item.value<=p.gold:
        delay_print("\nYou bought {}.\n".format(str(item)))
        p.gold=p.gold-item.value
        p.items.append(item)
        room['npcitems'].remove(item)
        return
      else:
        delay_print("\nYou don't have enough gold to buy this item. Come back when you have more!\n")
        comd=cmdInterpret(cmd)
        return
  elif choice=="no":
    delay_print("Come again soon, {}.\n")
   
    return 
  else: 
    delay_print("\nI don't have that... check back later.")
    
    return 


def cmdInterpret(cmd):
  global room,map,p
  parts = cmd.split(" ")
  verb = parts[0]
  recog=["equip","inspect","get","greet","take","kill","buy","sell","drop","check","hello","read","drink","use","eat","unequip","talk","jack","jerk","look","attack", "examine","talkto","interactwith","interact", "go", "move", "collect","buyfrom","talk","commands"]
  preps={"at","to","with","from"}
  article={"a","the"}
  
  if cmd=="quit":
    slow_print("byeeee.......\n")
    exit()
    return
  if cmd=="commands":
    for s in recog:
      delay_print(s+"\n")
    return 
  if cmd=="kill":
    for enemy in room['enemies']:
      room['enemies'].remove(enemy)
  if len(parts)<2:
    return 

  
  if not verb in recog:
    
    return 
  
  if verb=="check":
    if parts[1]=="inventory":
      p.inventory()  
  
  if verb=="jack"or "jerk":
    if parts[1]=="off":
      slow_print("This is what you get for sinning.")
      time.sleep(600)
      exit()
  

  
 

  if verb=="get" or "take"or"collect": 
    for item in room['items']: 
      if parts[1] ==item.name :
        if hasattr(item,'value'):
          p.items.append(item) #adds it to player inventory array
          room['items'].remove(item) #removes it from the room array
          delay_print("\nYou picked up a {}.\n".format(item.name))
          return

  if verb=="drop":
    for item in p.items: 
      if parts[1] ==item.name :
        p.items.remove(item) #adds it to player inventory array
        room['items'].append(item) #removes it from the room array
        delay_print("\nYou dropped your {}.\n".format(item.name))
        return
        
  if verb=="eat"or"consume" or "drink":
    for item in p.items:
      if hasattr(item,'hp'):
        if parts[1]==item.name:
          p.hp=p.hp+item.hp
          p.items.remove(item)
          delay_print(color.GREEN+"You used {} to heal yourself. You gained {} HP.\n".format(item.display,item.hp)+color.END)
          return  
  
  if verb=="equip":
    for item in p.items:
      if len(p.weaponslot)==1:
        delay_print("Unequip your weapon first.\n")
        return
      if parts[1]==item.name:
        if hasattr(item,'damage'):
          p.weaponslot.append(item)
          delay_print("You equipped a {}.\n".format(item.name))
          return
        if hassat(item,'hp'):
          delay_print("You can't equip that.") 
          return
        

  if verb=="unequip":
    for item in p.weaponslot:
      if parts[1]==str(item):
        p.unequipweapon()

  if verb=="inspect" or "examine":
    for item in p.items:
        if parts[1]==item.name:
          delay_print(item.details())
          return

  if verb=="look": 
    if parts[1]=="around":
      delay_print(room['info'])
      return
  


  
  
  if verb=="read":
    if parts[1]=="scroll":
      for scroll in room['items']:
        if hasattr(scroll,'text'):
          delay_print(color.CYAN+scroll.text+color.END)
          return


  if verb=="greet" or "hello":
    for npc in room["npcs"]:
      if parts[1]==npc.name:
        delay_print("You walk up to {}.\n{}: ".format(npc.display,npc.display))
        delay_print(str(npc.greeting)+"\n")
        for item in room['npcitems']:
          if item.name=="scroll":
            room['items'].append(item)
            room['npcitems'].remove(item)
        return
    
    

  if verb == "go" or "move":
    dir = parts[1].strip().lower()
    dirs = ["north","east","west","south","up","down"]
    if set(dirs).intersection(parts):
      nextRoom = -1
      if len(room['enemies'])>0:
        delay_print("You can't leave until the enemies are dead.")
        return
#Search if dir in room connector (there is a better way)
      for connector in room['connects']:
        if (dir in connector):
          nextRoom = connector[dir]
          slow_print ("Moving.............")
      if (nextRoom<0):
        delay_print ("""Blocked
""")
        return
      room = map[nextRoom]
  


                  
          

  if verb=="attack"or "fight":
     
      for enemy in room['enemies']:
        char=parts[1]
        if char==enemy.name:
          delay_print("You approach {}.\n{}:".format(enemy.display,enemy.display)+enemy.battlecry)
          if len(p.weaponslot)==0:
            delay_print("\nYou can't go into combat without a weapon.\nEquip one to enter combat\n")
            return
          for weapon in p.weaponslot:
            p.hp=p.hp-enemy.damage
            enemy.hp=enemy.hp-weapon.damage
            delay_print(color.RED+"\nYou did {} damage to {}. {} has {} hp left.\n{} did {} damage to you. You have {} hp left.\n".format(weapon.damage,enemy.display,enemy.display,enemy.hp,enemy.display,enemy.damage,p.hp)+color.END)
            if enemy.isdead():
              delay_print("You defeated {}! Here are your rewards:".format(enemy.display))
              room['enemies'].remove(enemy)
              for item in room['enemyitems']:
                delay_print("\n"+item.display)
                room['items'].append(item)
                room['enemyitems'].remove(item)
  if verb=="sell":
    for npc in room['npcs']:
      if parts[1]=="to":
        if parts[2]==npc.name:
          if len(p.items)>0:
            while len(p.items)>0:
              for item in p.items:
                chaching=raw_input(color.PURPLE+"\n{}: Your {} looks like a treasure!\nI could take it off your hands for {} gold.\nWould you like to sell it to me?\n>".format(npc.display,item.display,item.value)+color.END)
                chaching=chaching.lower().strip()
                if chaching=="yes":
                  p.items.remove(item)
                  p.gold=p.gold+item.value
                  if item in p.weaponslot:
                    p.weaponslot.remove(item)
                  delay_print("\nYou sold {} to {} for {} gold.\n".format(item.display,npc.display,item.value))
                  pass
                if chaching=="no":
                  delay_print(color.PURPLE+"That's too bad.\nIf you would like to leave, type 'exit'.\n"+color.END)
                  break   
           
              if chaching=="exit":
                break
            return
          else: 
            delay_print("\n{}: You have nothing to sell me.\n".format(npc.display))
            return
            
  if verb=="talk"or"interact":
    color.YELLOW
    for npc in room['npcs']:
      if parts[1]=="to":
        if len(parts)==3:
          pers=parts[2]  
          if pers==npc.name:
            delay_print("\n{}:Hello,{}.\n{}:".format(npc.display,p.name,npc.display)+npc.info)
            for item in room['npcitems']:
              if item.name=="scroll":
                room['items'].append(item)
                room['npcitems'].remove(item)
              return
    color.END
  if verb=="buy"or "purchase":
    print(color.DARKCYAN)
    if parts[1]=="from":
      for npc in room["npcs"]:
        pers=parts[2]
        if pers==npc.name:
          if len(room['npcitems'])>0:
            for item in room['npcitems']:
              if hasattr(item,'value'):
                choice=raw_input("\nWould you like to buy {},{}?\n".format(item.display,p.name))
                delay_print("{}\nPrice:{}".format(str(item),item.value))
               
                choice=choice.lower().strip()
                if choice=="yes":
                  if item.value<=p.gold:
                    delay_print("\nYou bought {}.\n".format(item.display))
                    p.gold=p.gold-item.value
                    p.items.append(item)
                    room['npcitems'].remove(item)
                  else:
                    delay_print("\nYou don't have enough gold to buy this item. Come back when you have more!\n")
                    comd=cmdInterpret(cmd)
                    return
                if choice=="no":
                  delay_print("\nCome again soon, {}.\n".format(p.name))
                  return 
          else:
            delay_print("\n{}: I haven't got any items for sale.\n".format(npc.display))
            return

    print(color.END)


 

  


  




def init():
  global room, map
  map=[]
  #0
  map.append({"name":"The Courtyard of the Castle Darkspur.", "info":"You are in a courtyard with stone walls and moss covering the ground.\nThere is a puddle of odd looking liquid south of you. \nTo the north is a large wooden door with a rusty iron handle.\n",
    "connects":[{"north":1},{"up":10}],
    "items":[Item("bread","Moldy Bread","It's a little moldy, but still edible",0,3),Weapon("knife","Knife(lv 0)","It's pretty rusty...",2,4),Scroll("scroll","Scroll of Summoning","scrollx","Welcome to the Castle Darkspur, traveller.\nHere are some useful tips to get you started.\n-You can move using compass directions, e.g. north, south, etc.\n-You need to equip the weapon you want to use before attacking an enemy.\nIf you are having trouble picking something up or attacking an enemy, try not using its adjectives. Remember, this is a work in progress.\n-Talk to characters by saying 'greet ____','talk to _____','sell to _____'or 'buy from _____'.\n-Type 'check inventory' to see what's in your bag and what weapon you have equipped.\n-Look around to get more infomation about the room you're in.\n-Explore the castle and find the secret that seeks to be found. Only then will you succeed in your quest to rid Castle Darkspur of its evil.")],
    "npcs":[NPC("davkas","Davkas",0,"Greetings, traveller.\nRead the scroll on the ground. It will cost you nothing.","The only advice I can give you is to read the scroll I have left in the room.")],
    "npcitems":[],
    "enemies":[Enemy("spider","Giant Spider","Fang","sssssss",random.randint(0,5),5)],
    "enemyitems":[Weapon("fang","Fang","It looks poisonous, but deadly.(lv 1)",5,5)]})
  room=map[0]
  map.append({"name":"The Castle Entry.\n","info": "\nA wrought iron Gargoyle looms above your head. On top of the gate is the crest of the family darkspur, who many years ago fell victim to a curse placed on the castle by a wizard.\n",
    "connects":[{"south":0},{"north":2}],
    "items":[Item("potion","Lesser Health Potion","It heals you, a little.",5,5),Scroll("scroll","Scroll of wisdom","scrolly","The story of the Family Darkspur.\nMany years ago, a family of valiant knights and warrior-women reigned over this land.\nThey were kind and generous to all that did them no harm.\nTo those that challenged their authority, a quick and painless death was their punishment.\nThe only thing more important to the Family Darkspur than power was wealth.\nThe family always ran into battle dressed in the finest dragon-scale mail with diamonds around their necks.\nLittle did they know that this would be their downfall.\nBEWARE OF MYSTERIOUS TREASURE.")],
    "npcs":[],
    "npcitems":[],
    "enemies":[],
    "enemyitems":[]})
  map.append({"name":"The foyer of a castle.",
    "info":"It smells of rot and death. It seems as though years have passed since anyone has been here. There are doors to the east and west of you. ",
    "connects":[{"south":1},{"west":3},{"east":4}],
    "items":[],
    "npcs":["rhello","Rhello, the sage","Great hall Key","I have a riddle for you...","What starts with E, ends with E, and contains one letter?"],
    "npcitems":[],
    "enemies":[],
    "enemyitems":[]})
  map.append({"name":"The front of the Great Hall.",
    "info":"moldy food....",
    "connects":[{"east":2},{"west":6}],
    "items":[],
    "npcs":[],
    "npcitems":[]})
  map.append({"name":"The Castle Kitchen.",
    "info":"cook stuff",
    "connects":[{"south":5},{"west":2}],
    "items":[],
    "npcs":[],
    "npcitems":[],
    "enemies":[],
    "enemyitems":[]})
  map.append({"name":"The Servant House.",
    "info":"ppl live here",
    "connects":[{"north":4}],
    "items":[],
    "npcs":[],
    "npcitems":[],
    "enemies":[],
    "enemyitems":[]})
  map.append({"name":"The Throne Room",
    "info":"it lit",
    "connects":[{"east":3},{"west":7}],
    "items":[],
    "npcs":[],
    "npcitems":[],
    "enemies":[],
    "enemyitems":[]})
  map.append({"name":"The Dungeon.",
    "info":"it stank",
    "connects":[{"east":6},{"south":8}],
    "items":[],
    "npcs":[],
    "npcitems":[],
    "enemies":[],
    "enemyitems":[]})
  map.append({"name":"The Library",
    "info":"books an stuff",
    "connects":[{"north":7},{"south":9}],
    "items":[],
    "npcs":[],
    "npcitems":[],
    "enemies":[],
    "enemyitems":[]})
  map.append({"name":" The Archmage's Study.",
    "info":"studdy",
    "connects":[{"north":8}],"items":[],
    "npcs":[],
    "npcitems":[],
    "enemies":[],
    "enemyitems":[]})
  map.append({"name":"Heaven",
    "info":"Welcome to dev heaven",
    "connects":[{"down":0}],
    "items":[],
    "npcs":[NPC("ben","Ben Berman","Dildo","Aloha nigga.","My butthole itches real bad. Come scratch it.")],
    "npcitems":[Item("dildo","Dildo","IT THICC AF",69,-69)],
    "enemies":[],
    "enemyitems":[]})

"""
self.name = name
    self.display=display
    self.description = description
    self.value = value
    self.hp= hp 

self.name = name
    self.display=display
    self.items=items
    self.greeting=greeting
    self.info=info"""
def roominfo():
  delay_print(color.BLUE)
  delay_print("\nLocation:\n"+room['name']+"\n")
  if len(room['npcs'])>0:
     for npc in room['npcs']:
      delay_print("\n{} is sitting in the corner.\n".format(str(npc.display)))
  if len(room['enemies'])>0:
    for enemy in room['enemies']:
      delay_print("\n{} blocks your way.\n".format(str(enemy.display)))
  if len(room['npcs'])<=0 and len(room['enemies'])<=0:
    delay_print("There's no one here.")
  if len(room['items'])>0:
     delay_print("\nItems in room:\n")
     for item in room['items']:
        delay_print(item.display+"\n")
  else:
    delay_print("\nThere are no items to be found here.\n")

  if p.hp>0:
    delay_print("\nYou have {} hp.\n".format(p.hp))
  else:
    delay_print("YOU DIED! GAME OVER....")
    exit()
  delay_print(color.END)
  
    
  
def main():
  global p

  init()
  while True:
    roominfo()
    delay_print("\n-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-=x=-\n")
    cmd=raw_input(color.FLASH+color.WHITE+">"+color.END)
    cmd=cmd.strip()
    cmd=cmd.lower()
    cmdInterpret(cmd)

   
    
if __name__ == "__main__":
  main()
 