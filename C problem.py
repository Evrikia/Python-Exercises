class Crew:
    def __init__(self,name,status='Active',location='Sleep Pods'):
        self.name = name
        self.status = status
        self.location = location

    def __repr__(self):
        return f"{self.name} : {self.status}, at {self.location}"
    
    def move(self,location):
          if location == 'Bridge' or location == 'Medbay' or location == 'Engine' or location == 'Lasers' or location == 'Sleep Pods':
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

    
if __name__ == '__main__':
      crew1 = Crew('Sakashi')
      crew2 = Crew('Jina')
      crew3 = Crew('Daniel')
      space_boat = Starship('Ebon Hawk',[crew1,crew2,crew2])
      print(space_boat.name)
      print(space_boat.crew_list)
      print(space_boat.damaged)
      crew1.move('Dungeon')
      print(crew1.location)
      crew1.move('Engine')
      print(crew1.location)
      crew2.repair(space_boat)
      crew3.first_aid(space_boat)
      crew2.fire_lasers(space_boat,space_boat,"Engine")