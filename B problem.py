class Crew:
    def __init__(self,name,status='Active',location='Sleep Pods'):
        self.name = name
        self.status = status
        self.location = location

    def __repr__(self):
        return f"{self.name} : {self.status}, at {self.location}"
    
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