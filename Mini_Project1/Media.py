import pytube

from actor import Actor

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
        actor1 = input("Enter number of cast one(you can add new actor with add a new actor option) : ")
        actor2 = input("Enter number of cast two : ")
        actor3 = input("Enter number of cast three : ")

        new_media = Media(ID, name, director, IMBDscore, url, duration, [actor1,actor2,actor3])
        return new_media 

 
    def show_info(self):
        print(self.ID,"Name: ",self.name)
        print("Director: ",self.director)
        print("IMBD score: ",self.IMBDscore)
        print("Duration: ",self.duration)
        print("Casts: ")
        for id in self.casts:
            Actor.show(id)


    def show_media_from_list(self):
            print(self.ID,"Name: ",self.name)
            print("Director: ",self.director)
            print("IMBD score: ",self.IMBDscore)
            print("Duration: ",self.duration)


    def edit_media(self):
        self.ID == input("Enter an ID : ")
        self.name = input("Enter name of media : ")
        self.director = input("Emter director of media : ")
        self.score = input("Enter its IMBD score : ")
        self.url = input("Entar a download url for it : ")
        self.duration = input("Enter duration : ")
        self.actor1 = input("Enter cast one : ")
        self.actor2 = input("Enter cast two : ")
        self.actor3 = input("Enter cast three : ")


    def download(self):
        link=self.url
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename='test.mp4')

    def search_duration(self,hour1,min1,hour2,min2):
        time1 = int(hour1)*3600 + int(min1)*60
        time2 = int(hour2)*3600 + int(min2)*60
        self_times = self.duration.split(":")
        self_time = int(self_times[0])*3600 + int(self_times[1])*60
        if time1 > self_time > time2:
            self.show_info()