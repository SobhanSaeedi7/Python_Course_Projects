from media import Media

class Series(Media):
    def __init__(self, id, n, di, s, u, du, c, e):
        super().__init__(id, n, di, s, u, du, c)
        self.episods = e

    @staticmethod
    def add():
        ID = input("Enter an ID : ")
        name = input("Enter name of media : ")
        director = input("Emter director of media : ")
        IMBDscore = input("Enter its IMBD score : ")
        url = input("Entar a download url for it : ")
        duration = input("Enter duration : ")
        actor1 = input("Enter number of cast one(you can add new actor with add a new actor option) : ")
        actor2 = input("Enter number of cast two : ")
        actor3 = input("Enter number of cast three : ")
        episods = input("Enter number of episods : ")

        new_media = Series(ID, name, director, IMBDscore, url, duration, [actor1,actor2,actor3],episods)
        return new_media 
    
    def edit_serie(self):
        self.ID == input("Enter an ID : ")
        self.name = input("Enter name of media : ")
        self.director = input("Emter director of media : ")
        self.score = input("Enter its IMBD score : ")
        self.url = input("Entar a download url for it : ")
        self.duration = input("Enter duration : ")
        self.actor1 = input("Enter cast one : ")
        self.actor2 = input("Enter cast two : ")
        self.actor3 = input("Enter cast three : ")
        self.episods == input("Enter number of episods : ")

    def show_serie_from_list(self):
        print(self.ID,"Name: ",self.name)
        print("Director: ",self.director)
        print("IMBD score: ",self.IMBDscore)
        print("Number of Epizods: ",self.episods)
    
    def show_serie(self):
        print(self.ID,"Name: ",self.name)
        print("Director: ",self.director)
        print("IMBD score: ",self.IMBDscore)
        print("Number of Epizods: ",self.episods)
        print("Casts: ")
        for id in len(self.casts):
            Actor.show(id)