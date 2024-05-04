import random

loc_list = ['Bridge','Medbay','Engine','Lasers','Sleep Pods']
left_deny_count = 2

class Crew:
    def __init__(self,name,status='Active',location='Sleep Pods'):
        self.name = name
        self.status = status
        self.location = location

    def __repr__(self):
        return f"{self.name} : {self.status}, at {self.location}"
    
    def move(self,location):
        if location in loc_list:
            self.location = location
        else:
            print("Not a valid location")
    
    def repair(self,ship):
        print(f"{self.name} doesn't know how to do that")
    
    def first_aid(self,ship):
        print(f"{self.name} doesn't know how to do that")
    
    def fire_lasers(self,ship,target_ship,target_location):
        print(f"{self.name} doesn't know how to do that")

class Starship:
    def __init__(self, name, crew_list, damaged={'Bridge': False, 'Medbay': False, 'Engine': False, 'Lasers': False, 'Sleep Pods': False}):
        self.name = name
        self.crew_list = crew_list
        self.damaged = damaged

    def encounter(self, enemy_ship):
        print('You have 3 choices for order of your crew members!')
        choice_count = 3
        while choice_count > 0:
            random.shuffle(self.crew_list)
            print(self.crew_list)
            OK = input("Do you want to play with this order?(Answer 'Yes' or 'No')")
            if OK == 'Yes':
                break
            choice_count-=1
        
        OK = input("You are called to a battle.Do you accept the call?(Answer 'Yes' or 'No')")
        if OK == 'No' and left_deny_count > 0:
            left_deny_count = left_deny_count - 1
            return
        else:
            print('You have 3 choices for order of your crew members!')
            choice_count = 3
            while True:
                random.shuffle(enemy_ship.crew_list)
                print(enemy_ship.crew_list)
                OK = input("Do you want to play with this order?(Answer 'Yes' or 'No')")
                if OK == 'Yes':
                    break

        crew1_injured_count,crew2_injured_count = 0,0 #crew1-ship,crew2-enemy_ship

        while True:
            for member in self.crew_list:
                if member.status == 'Injured':#if the member is injured the member can't do anything
                    continue
                if isinstance(member, Captain):#if the member is captain
                    member.fire_lasers(self, enemy_ship, loc_list[random.randint(0,4)])
                elif isinstance(member, Doctor):#if the member is doctor
                    member.first_aid(self)
                elif isinstance(member, Engineer):#if the member is engineer
                    member.repair(self)

            for member in enemy_ship.crew_list:
                if member.status == 'Injured':#if the member is injured the member can't do anything
                    continue
                if isinstance(member, Captain):#if the member is captain
                    member.fire_lasers(self, enemy_ship, loc_list[random.randint(0,4)])
                elif isinstance(member, Doctor):#if the member is doctor
                    member.first_aid(self)
                elif isinstance(member, Engineer):#if the member is engineer
                    member.repair(self)

            for member in self.crew_list:#returns the count of injured in self.crew_list
                if member.status == 'Injured':
                    crew1_injured_count+=1
            if crew1_injured_count == len(self.crew_list):#if all members are injured
                break

            for member in enemy_ship.crew_list:#returns the count of injured in enemy_ship.crew_list
                if member.status == 'Injured':
                    crew2_injured_count+=1
            if crew2_injured_count == len(enemy_ship.crew_list):#if all members are injured
                break

            crew1_injured_count,crew2_injured_count = 0,0

        if crew1_injured_count == len(self.crew_list):
            print(f"{enemy_ship.name} won the battle")
        elif crew2_injured_count == len(enemy_ship.crew_list):
            print(f"{self.name} won the battle")

class Engineer(Crew):
      def __init__(self,name):
           super().__init__(name)

      def repair(self, ship):
        if ship.damaged[self.location]:
            ship.damaged[self.location] = False
            print(f"{self.name} fixed the damage to {self.location}")
        else:
            print(f"{self.location} isn't damaged")

class Captain(Crew):
    def __init__(self, name):
        super().__init__(name)

    def fire_lasers(self, ship, target_ship, target_location):
        if not target_location in loc_list:
            print('Not a valid location')
        elif self.location != 'Bridge':
            print(f"{self.name} must be in the Bridge to fire lasers")
        elif ship.damaged['Bridge']:
            print('Bridge is too damaged to order lasers to be fired')
        elif ship.damaged['Lasers']:
            print('Lasers are too damaged to fire')
        else:
            print(f"{ship.name} fires lasers at {target_ship.name}'s {target_location}")
            target_ship.damaged[target_location] = True
            c_lis = target_ship.crew_list
            for member in c_lis:
                if member.location == target_location:
                    member.status = 'Injured'


class Doctor(Crew):
      def __init__(self,name,medpacs=3):
            super().__init__(name)
            self.medpacs = medpacs

      def first_aid(self, ship):
            if self.medpacs == 0:
                if self.location == 'Medbay' and not ship.damaged['Medbay']:
                    self.medpacs = 3
                    print(f"{self.name}'s supply of medpacs has been replenished")
                    c_lis = ship.crew_list
                    for member in c_lis:
                        if self.medpacs <= 0:
                            print(f"{self.name} has no medpacs left.")
                            break
                        if member.status == 'Injured':
                            member.status = 'Active'
                            print(f"{self.name} healed {member.name}'s injuries")
            else:
                if self.location == 'Medbay' and not ship.damaged['Medbay']:
                    self.medpacs = 3
                    print(f"{self.name}'s supply of medpacs has been replenished")
                else: 
                    self.medpacs-=1
                c_lis = ship.crew_list
                for member in c_lis:
                    if self.medpacs <= 0:
                        print(f"{self.name} has no medpacs left.")
                        break
                    if member.status == 'Injured':
                        member.status = 'Active'
                        print(f"{self.name} healed {member.name}'s injuries")