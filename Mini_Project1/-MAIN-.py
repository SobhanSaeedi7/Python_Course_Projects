from media import Media
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from actor import Actor

MEDIAS = []
def download():
    database = open("txt_media.txt", "r")

    for line in database:
        details = line.split(",")
        if details[5] == "none":
            obj = Series(details[0], details[1], details[2], float(details[3]), details[4], details[5], [details[6],details[7],details[8]], int(details[9]))
            MEDIAS.append(obj)    
        else:
            obj = Media(details[0], details[1], details[2], float(details[3]), details[4], details[5], [details[6],details[7],details[8]])
            MEDIAS.append(obj)

    database.close()

def upload():
    data = open("txt_media.txt", "w")
    for media in MEDIAS:
        if media.duration == "none":
            data.write(str(media.ID)+","+str(media.name)+","+str(media.director)+","+str(media.IMBDscore)+","+str(media.url)+","+str(media.duration)+","+str(media.casts[0])+","+str(media.casts[1])+","+str(media.casts[2])+","+str(media.episods)+","+"\n")
        else:
            data.write(str(media.ID)+","+str(media.name)+","+str(media.director)+","+str(media.IMBDscore)+","+str(media.url)+","+str(media.duration)+","+str(media.casts[0])+","+str(media.casts[1])+","+str(media.casts[2])+","+"\n")
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
    print("7-add a new actor👤")
    print("8-exit🏃")

#_____________________________________________________________________________________________________________________________________________________________________

download()
while True:
    show_menu()
    choose = input("Enter number of your choice : ")

    if choose == "1":
        kind = input("Do you want to add a serie'Y' or no'N'?")
        if kind == "Y" :
            new_media = Series.add()
            MEDIAS.append(new_media)
            print("Added successful✅")
        elif kind == "N":
            new_media = Media.add()
            MEDIAS.append(new_media)
            print("Added successful✅")

    elif choose == "2":
        user_input = input("Enter a name or ID to search : ")
        for media in MEDIAS:
            if media.ID == user_input or media.name == user_input:
                if media.duration == "none":
                    media.edit_serie()
                    print("Edited successful✅")
                else:
                    media.edit_media()
                    print("Edited successful✅")
        else:
            print("Not found!")

    elif choose == "3":
        user_input = input("Enter a name or ID to search : ")
        for media in MEDIAS:
            if media.ID == user_input or media.name == user_input:
                okey = input("Are you sure that you want to remove this media??Y/N ; ")
                if okey == "Y":
                    MEDIAS.remove(media)
                    print("Removed successfully✅")
                    break
                elif okey == "N":
                    print("Didn`t remove🔁")
                    break
                else :
                    print("Just enter Y(yes) or N(no)")

        else:
            print("Not found!")

    elif choose == "4":
        kind = input("Do you want to search with name and ID 'N' or with duration 'D' : ")
        if kind == "N":
            user_input = input("Enter a name or ID to search : ")
            for media in MEDIAS:
                if media.ID == user_input or media.name == user_input:
                    if media.duration == "none":
                        media.show_serie()
                    else:
                        media.show_info()
        elif kind == "D":
            hour1 = input("Enter hour of first time(smaller one) : ")
            min1 = input("Enter minute of first time(smaller one) : ")
            hour2 = input("Enter hour of second time(bigger one) : ")
            min2 = input("Enter minute of second time(bigger one) : ")
            for media in MEDIAS:
                if media.duration != "none":
                    media.search_duration(hour1, min1, hour2, min2)
            else: 
                print("not found!!")
        else:
            print("Just enter 'N' to search with name and ID or 'D' to search with time")

    elif choose == "5":
        for obj in MEDIAS:
            if obj.duration == "none":
                obj.show_serie_from_list()
                print()
            else:
                obj.show_media_from_list()
                print()                

    elif choose == "6":
        user_input = input("Enter a name or ID to search : ")
        for media in MEDIAS:
            if media.ID == user_input or media.name == user_input:
                media.download()
                print("Download started📥")

        else:
            print("Not found!")

    elif choose == "7":
        Actor.add()

    elif choose == "8":
        upload()
        exit(0)

    else:
        print("Please just enter number of your choose😕")

