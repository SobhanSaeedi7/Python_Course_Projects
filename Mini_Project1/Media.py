import pytube

from Series import Series
from Actor import Actor

class Media:
    def __init__(self, id, n, di, s, u, du, c):
        self.ID = id
        self.name = n
        self.director = di
        self.IMBDscore = s
        self.url = u
        self.duration = du
        self.casts = c


    @staticmethod
    def add():
        ID = input("Enter an ID : ")
        name = input("Enter name of media : ")
        director = input("Emter director of media : ")
        IMBDscore = input("Enter its IMBD score : ")
        url = input("Entar a download url for it : ")
        duration = input("Enter duration : ")
        actor1 = input("Enter cast one : ")
        actor2 = input("Enter cast two : ")
        actor3 = input("Enter cast three : ")
        kind = input("Are you adding a serie 'Y' or no 'N'?")
        if kind == "Y" :
            episods = input("Enter number of episods : ")
            new_media = Series(ID, name, director, score, url, duration, [actor1,actor2,actor3], episods)
            return new_media
        elif kind == "N":
           new_media = Media(ID, name, director, score, url, duration, [actor1,actor2,actor3])
           return new_media 

 
    def show_info(self):
        if len(self) == 6:
            print(self.ID,"Name: ",self.name)
            print("Director: ",self.director)
            print("IMBD score: ",self.score)
            print("Duration: ",self.duration)
            print("Casts: ")
            for id in len(self.casts):
                Actor.show(id)
        elif len(self) == 7:
            print(self.ID,"Name: ",self.name)
            print("Director: ",self.director)
            print("IMBD score: ",self.score)
            print("Duration: ",self.duration)
            print("Number of Epizods: ",self.episods)
            print("Casts: ")
            for id in len(self.casts):
                Actor.show(id)
    def show_list(self):
        if len(self) == 6:
            print(self.ID,"Name: ",self.name)
            print("Director: ",self.director)
            print("IMBD score: ",self.score)
            print("Duration: ",self.duration)
        elif len(self) == 7:
            print(self.ID,"Name: ",self.name)
            print("Director: ",self.director)
            print("IMBD score: ",self.score)
            print("Duration: ",self.duration)
            print("Number of Epizods: ",self.episods)

    def edit(self):
        self.ID == input("Enter an ID : ")
        self.name = input("Enter name of media : ")
        self.director = input("Emter director of media : ")
        self.score = input("Enter its IMBD score : ")
        self.url = input("Entar a download url for it : ")
        self.duration = input("Enter duration : ")
        self.actor1 = input("Enter cast one : ")
        self.actor2 = input("Enter cast two : ")
        self.actor3 = input("Enter cast three : ")
        if len(self) == 7:
            self.episods == input("Enter number of episods : ")

    def download(self):
        url=self.url
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
