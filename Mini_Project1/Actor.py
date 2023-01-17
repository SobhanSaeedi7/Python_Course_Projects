ACTORS = []
class Actor:
    def __init__(self, id, n, c, a):
        self.ID = id
        self.name = n
        self.country = c
        self.age = a
    
    @staticmethod
    def download():
        database = open("txt_actor.txt", "r")
        for line in database:
            data = line.split(",")
            actor = Actor(data[0], data[1], data[2], data[3])
            ACTORS.append(actor)
        database.close()
        
    @staticmethod
    def show(num):
        Actor.download()
        for actor in ACTORS:
            if actor.ID == int(num):
                print(actor.name,"\t",actor.age,"\t",actor.country,"\n")
        Actor.upload()


    @staticmethod
    def add():
        Actor.download()
        ID = input("Enter an ID : ")
        name = input("Enter actor`s name : ")
        age = input("Enter actor`s age : ")
        country = input("Enter actor`s country : ")

        new_actor = Actor(ID, name, country, age)
        ACTORS.append(new_actor)
        Actor.upload()



    @staticmethod
    def upload():
        f = open("txt_actor.txt", "w")
        for actor in ACTORS:
            f.write(str(actor.ID)+","+str(actor.name)+","+str(actor.country)+","+str(actor.age)+"+"+"\n")
        f.close()

Actor.download()
#print(ACTORS)