class Adventurer:
    def __init__(self,name,level,strength,speed,power):
        self.name = str(name)
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = self.level * 6
        self.hidden = False

    def __repr__(self):
        return self.name+' '+'-'+' '+"HP:"+' '+str(self.HP)

    def __lt__(self,target):
        if self.HP < target.HP:
            return True
        else:
            return False

    def attack(self,target):
        if  target.hidden == True:
            print(self.name+' '+"can't see"+' '+target.name)
        else:
            target.HP = target.HP-(self.strength+4)
            print(self.name+' '+"attacks"+' '+str(target.name)+' '+"for"+' '+ str(self.strength+4)+' '+"damage")

class Fighter(Adventurer):
    def __init__(self,name,level,strength,speed,power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = level * 12

    def attack(self,target):
        if  target.hidden == True:
            print(self.name+' '+"can't see"+' '+target.name)
        else:
            target.HP = target.HP-(2*self.strength+6)
            print(self.name+' '+"attacks"+' '+str(target.name)+' '+"for"+' '+ str(2*self.strength+6)+' '+"damage")

class Thief(Adventurer):
    def __init__(self,name,level,strength,speed,power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = level * 8
        self.hidden = True

    def attack(self,target):
        if self.hidden:
            if target.hidden == self.hidden and self.speed < target.speed:
                print(self.name+' '+"can't see"+' '+target.name)
            else:
                target.HP = target.HP-(self.speed+self.level)*5
                self.hidden = False
                if type(target) == Thief:
                    target.hidden = False
                print(self.name+' '+"attacks"+' '+str(target.name)+' '+"for "+ str((self.speed+self.level)*5)+' '+"damage")
        else:
            Adventurer.attack(self, target)


class Wizard(Adventurer):
    def __init__(self,name,level,strength,speed,power):
         Adventurer.__init__(self,name,level,strength,speed,power)
         self.fireball_left = power

    def attack(self,target):
        if self.fireball_left > 0:
            target.HP = target.HP - (self.level * 3)
            self.fireball_left = self.fireball_left - 1
            print(self.name+" cast fireball on "+target.name+" for "+str(self.level *3 )+" damage")
            if type(target) == Thief:
                target.hidden = False
        else:
            Adventurer.attack(self, target)

def duel(adv1,adv2):
    while True:
        if adv1.HP <= 0 and adv2.HP > 0:
            print(repr(adv1))
            print(repr(adv2))
            print(adv2.name+" wins!")
            return False
        elif adv2.HP <= 0 and adv1.HP > 0:
            print(repr(adv1))
            print(repr(adv2))
            print(adv1.name+" wins!")
            return True
        elif adv1.HP <= 0 and adv2.HP <= 0:
            print(repr(adv1))
            print(repr(adv2))
            print("Everyone loses")
            return False
    
        print(repr(adv1))
        print(repr(adv2))
        adv1.attack(adv2)


        if adv1.HP <= 0 and adv2.HP > 0:
            print(repr(adv1))
            print(repr(adv2))
            print(adv2.name+" wins!")
            return False
        elif adv2.HP <= 0 and adv1.HP > 0:
            print(repr(adv1))
            print(repr(adv2))
            print(adv1.name+" wins!")
            return True
        elif adv1.HP <= 0 and adv2.HP <= 0:
            print(repr(adv1))
            print(repr(adv2))
            print("Everyone loses")
            return False

        
        adv2.attack(adv1)


        if adv1.HP <= 0 and adv2.HP > 0:
            print(repr(adv1))
            print(repr(adv2))
            print(adv2.name+" wins!")
            return False
        elif adv2.HP <= 0 and adv1.HP > 0:
            print(repr(adv1))
            print(repr(adv2))
            print(adv1.name+" wins!")
            return True
        elif adv1.HP <= 0 and adv2.HP <= 0:
            print(repr(adv1))
            print(repr(adv2))
            print("Everyone loses")
            return False



def tournament(adv_list):
   if(len(adv_list)==0):
      return None
    
   elif(len(adv_list)==1):
      return adv_list[0]
    
   else: 
      while len(adv_list) > 1:
          adv_list.sort()
          first_highest=adv_list[len(adv_list)-1]
          second_highest=adv_list[len(adv_list)-2]
          if(duel(second_highest,first_highest)==True):
              adv_list.pop(len(adv_list)-1)
          else:
              adv_list.pop(len(adv_list)-2)

