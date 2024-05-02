class Crew:
    def __init__(self,name,status='Active',location='Sleep Pods'):
        self.name = name
        self.status = status
        self.location = location

    def __repr__(self):
        return f"{self.name} : {self.status}, at {self.location}"
    
if __name__ == '__main__':
    crew = Crew('Eduard')
    print(crew.name)
    print(crew.location)
    print(crew.status)
    print(crew)
    