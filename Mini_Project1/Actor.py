ACTORS = []
class Actor:
    def __init__(self, id, n, c, a):
        self.ID = id
        self.name = n
        self.country = c
        self.age = a
    
    @staticmethod
    def download():
        f = open("Mini_Project1\Actor.txt", "r")
        for line in f:
            data = line.split(",")
            actor = Actor(int(data[0]), data[1], data[2], data[3])
            ACTORS.append(actor)
        f.close
    @staticmethod
    def show(num):
        for actor in ACTORS:
            if actor.ID == int(num):
                print(actor.name,"\t",actor.age,"\t",actor.country)
    @staticmethod
    def add():
        ID = input("Enter an ID : ")
        name = input("Enter actor`s name : ")
        age = input("Enter actor`s age : ")
        country = input("Enter actor`s country : ")

        new_actor = Actor(ID, name, country, age)
        ACTORS.append(new_actor)
    @staticmethod
    def upload():
        f = open("Mini_Project1\Actor.txt", "w")
        for actor in ACTORS:
            f.write(str(actor.ID)+","+str(actor.name)+","+str(actor.country)+","+str(actor.age))