loc_list = ['Bridge','Medbay','Engine','Lasers','Sleep Pods']

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
    def __init__(self,name,crew_list,damaged={'Bridge':False,'Medbay':False,'Engine':False,'Lasers':False,'Sleep Pods':False}):
        self.name = name
        self.crew_list = crew_list
        self.damaged = damaged

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



if __name__ == '__main__':
    engi1 = Engineer('Chris')
    print(isinstance(engi1, Crew)) #True
    cap1 = Captain('Emily')
    print(isinstance(cap1, Crew)) #True
    doc1 = Doctor('Audrey')
    print(isinstance(doc1, Crew)) #True
    print(doc1.medpacs) #3

    engi2 = Engineer('Mitali')
    engi2.move('Medbay')
    doc2 = Doctor('Jack')
    doc2.move('Bridge')
    cap2 = Captain('Andrew')
    engi3 = Engineer('Jess')
    doc3 = Doctor('Preston')
    cap3 = Captain('Abdul')
    cap3.move('Engine')

    ship1 = Starship('Voyager', [engi1, doc1, cap1])
    ship2 = Starship('Tempest', [engi2, doc2, cap2, engi3, doc3, cap3])

    cap1.fire_lasers(ship1, ship2, "Weak Point") #Not a valid location.
    cap1.fire_lasers(ship1, ship2, 'Medbay') #Emily must be in the Bridge to fire lasers.
    cap1.move('Bridge')
    cap1.fire_lasers(ship1, ship2, 'Sleep Pods') #Voyager fires lasers at Tempest's Sleep Pods.
    print(ship2.damaged) #{'Bridge': False, 'Medbay': False, 'Engine': False, 'Lasers': False, 'Sleep Pods': True}
    print(ship2.crew_list) #[Mitali : Active, at Medbay, Jack : Active, at Bridge, Andrew : Injured, at Sleep Pods, Jess : Injured, at Sleep Pods, Preston : Injured, at Sleep Pods, Abdul : Active, at Engine]

    engi2.move('Sleep Pods')
    engi2.first_aid(ship2) #Mitali doesn't know how to do that.
    engi2.repair(ship2) #Mitali fixed the damage to Sleep Pods.
    print(ship2.damaged) #{'Bridge': False, 'Medbay': False, 'Engine': False, 'Lasers': False, 'Sleep Pods': False}
    print(engi2) #Mitali : Active, at Sleep Pods

    doc2.move('Sleep Pods')
    doc2.first_aid(ship2) #Jack healed Andrew's injuries.
                        #Jack healed Jess's injuries.
                        #Jack healed Preston's injuries.
    print(ship2.crew_list) #[Mitali : Active, at Sleep Pods, Jack : Active, at Sleep Pods, Andrew : Active, at Sleep Pods, Jess : Active, at Sleep Pods, Preston : Active, at Sleep Pods, Abdul : Active, at Engine]
    print(doc2.medpacs) #2
    doc2.first_aid(ship2)
    doc2.first_aid(ship2)
    print(doc2.medpacs) #0
    print(doc1.medpacs) #3
    doc2.first_aid(ship2) #Jack has no medpacs left.

    cap2.move('Medbay')
    cap1.fire_lasers(ship1, ship2, 'Medbay') #Voyager fires lasers at Tempest's Medbay.
    print(cap2) #Andrew : Injured, at Medbay
    print(ship2.damaged['Medbay']) #True
    doc2.move('Medbay')
    doc2.first_aid(ship2) #Jack has no medpacs left.
    print(doc2.medpacs) #0
    print(cap2) #Andrew : Injured, at Medbay
    engi3.repair(ship2) #Sleep Pods isn't damaged.
    engi3.move('Medbay')
    engi3.repair(ship2) #Jess fixed the damage to Medbay.
    doc2.first_aid(ship2) #Jack's supply of medpacs has been replenished.
                        #Jack healed Andrew's injuries.
    print(doc2.medpacs) #3
    print(cap2) #Andrew : Active at Medbay
    doc2.first_aid(ship2) #Jack's supply of medpacs has been replenished.
    print(doc2.medpacs) #3

    cap3.move('Bridge')
    cap3.fire_lasers(ship2, ship1, 'Lasers') #Tempest fires lasers at Voyager's Lasers.
    cap1.fire_lasers(ship1, ship2, 'Engine') #Lasers are too damaged to fire.
    ship1.damaged['Bridge'] = True
    cap1.fire_lasers(ship1, ship2, 'Engine') #Bridge is too damaged to order lasers to be fired.