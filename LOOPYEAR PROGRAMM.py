# LOOPYEAR PROGRAMM


# userinput = ("please enter a year: ")
# y = 4,100,400

# def userloopyear(userinput,y):
#     if userinput%y == 0:
#         else print("no loopyear") #ich weiß nicht warum hier "expected expression kommt"
#         userloopyear(100)
        
        
# habe es mir von google zusammengesucht. anders konnte ich das nicht mehr aus dem kopf abrufen,
# ich verinnerliche die sachen als anfänger nicht so schnell (ich brauche viel mehr wiederh.) + wir haben länger kein python gemacht
# also das wieder nach den aws themen abzurufen klappt bei mir nicht.
print("Aufgabe2")
print()

namen = ["peter", "hans", "markus lanz"]

file = open("namen.txt","w")

for name in namen:
    print(name+"\n")
    file.write(name)

file.close()