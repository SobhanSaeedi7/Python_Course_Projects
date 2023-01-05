from Media import Media
from Film import Film
from Series import Series
from Documentary import Documentary
from Clip import Clip
from Actor import Actor

MEDIAS = []
def download():
    database = open("Mini_Project1\Medias.txt", "r")

    for line in database:
        details = line.split(",")
        if len(details) == 8:
            obj = Media(int(details[0]),details[1],details[2],float(details[3]),details[4],details[5],[details[6],details[7],details[8]])
        elif len(details) == 9:
            obj = Series(int(details[0]),details[1],details[2],float(details[3]),details[4],details[5],[details[6],details[7],details[8]],details[9])

        MEDIAS.append(obj)
    database.close()

def upload():
    data = open("Mini_Project1\Medias.txt", "w")
    for media in MEDIAS:
        if len(media) == 6:
            data.write(str(media.ID)+","+str(media.name)+","+str(media.director)+","+str(media.IMBDscore)+","+str(media.url)+","+str(media.duration)+","+str(media.casts))
        if len(media) == 6:
            data.write(str(media.ID)+","+str(media.name)+","+str(media.director)+","+str(media.IMBDscore)+","+str(media.url)+","+str(media.duration)+","+str(media.casts)+","+str(media.episods))
    data.close()

def search():
    kind = input("Do you want to search with name and ID of media (enter 1) or with duration (enter 2)??") 
    if kind == "1":
        user_input = input("Enter name or ID : ")
        for media in MEDIAS:
            if media.name == user_input or media.ID == int(user_input):
                media.show_info()
        else:
            print("Not found!")
    elif kind == "2":
        hour1 = input("Enter hour of first time(smaller time) : ")
        min1 = input("Enter minute of first time(smaller time) : ")
        hour2 = input("Enter hour of second time(bigger time) : ")
        min2 = input("Enter minute of second time(bigger time) : ")
        time1 = int(hour1)*3600 + int(min1)*60
        time2 = int(hour2)*3600 + int(min2)*60
        for media in MEDIAS:
            spliting = media.duration.split(":")
            mediatime = int(spliting[0])*3600 + int(spliting[1])*60
            if time1 <= mediatime <= time2:
                media.show_list()
        else:
            print("Not found!!")             

def show_menu():
    print("1-add➕")
    print("2-edit🖊")
    print("3-remove❌")
    print("4-search🔎")
    print("5-show list📜")
    print("6-download📥")
    print("7-exit🏃")

#_____________________________________________________________________________________________________________________________________________________________________

download()
while True:
    show_menu()
    choose = input("Enter number of your choice : ")

    if choose == "1":
        new_media = Media.add()
        MEDIAS.append(new_media)
        print("Added successful✅")

    elif choose == "2":
        user_input = input("Enter a name or ID to search : ")
        for media in MEDIAS:
            if media.ID == int(user_input) or media.name == user_input:
                media.edit()
                print("Edited successful✅")
        else:
            print("Not found!")

    elif choose == "3":
        user_input = input("Enter a name or ID to search : ")
        for media in MEDIAS:
            if media.ID == int(user_input) or media.name == user_input:
                okey = input("Are you sure that you want to remove this media??Y/N ; ")
                if okey == "Y":
                    MEDIAS.remove(media)
                    print("Removed successfully✅")
                elif okey == "N":
                    print()
                else :
                    print("Just enter Y(yes) or N(no)")
        else:
            print("Not found!")

    elif choose == "4":
        Media.search()

    elif choose == "5":
        for obj in MEDIAS:
            obj.show_list()
            print()

    elif choose == "6":
        user_input = input("Enter a name or ID to search : ")
        for media in MEDIAS:
            if media.ID == int(user_input) or media.name == user_input:
                media.download()
                print("Downloaded successful✅")

        else:
            print("Not found!")
    elif choose == "7":
        Actor.add()

    elif choose == "8":
        upload()
        exit()

    else:
        print("Please just enter number of your choose😕")

