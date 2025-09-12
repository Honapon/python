# tall = [1, 3, 5, 7, 9]
# bokstaver = ['a', 'b', 'c', 'd', 'e']

# print(tall[0])
# print(bokstaver[4])
# print(bokstaver[-2])

# fotballklubber = []
# #print(fotballklubber)
# fotballklubber.append('Tottenham')
# fotballklubber.append('liverpool')
# fotballklubber.append('Arsenal')

# #print(fotballklubber)

# #sjekk om element finnes med in
# if 'Arsenal' in fotballklubber :
#     print("Arsenal er DOGGGF")

# #sjekk om element ikke finnes med not in
# if 'Arsenal' not in fotballklubber:
#     print("Arsenal er fortsatt dog")
    
    
# #skrive ut alle klubbene
# for fotballklubb in fotballklubber:
#     print(fotballklubb)
    
# #hva skjer hvis vi bruker variabelen utenfor løkka?
# print(fotballklubb)

# #ny_klubb = input("Legg til en ny klubb: ")
# #fotballklubber.append(ny_klubb)

# print(fotballklubber)

# #if 'Fulham' in fotballklubber:
# #    fjernIndex = fotballklubber.index('Fulham')
# #    fotballklubber.pop(fjernIndex)

# for fotbalkubb in fotballklubber:
#     print (fotbalkubb)

# for i in range(len(fotballklubber)):
#     print(fotballklubber[i])


#lister oppgaver

# tall = [1, 3, -2, 2, 5, -1, -7, 8, 5, 6, -4, 5]

# print(max(tall))
# print(min(tall))





# navn = ["stine", "mari", "ingrid"]

# for lærer in navn:
#     print(lærer)

# navn[2] = "nanna"
# print(navn)

# navne_liste = [["stine", "mari"], ["hamid", "hans", "houman"], ["sezer"]]

# for navn in navne_liste:
    
#     print(navn)

# for subliste in navne_liste:
#     for navn in subliste:
#         print(navn, end =" ")
        
        
# for i in range(len(navne_liste)):
#     for j in range(len(navne_liste[i])):
#         print(navne_liste[i][j])

#Oppgaver lister OG Funksjoner

#oppg 1
# tabell = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]

# print(tabell[0][1])
# print(tabell[0][2])
# print(tabell[1][0])
# print(tabell[2][0])

#oppg 2

# def Norge(by, land):
#     print(f"{by} er en by i {land}")
    
# Norge("Oslo", "Norge")

liste = ["druer", "jordbær", "bringebær"]

def dex(list):
    a = -1
    for frukt in list:
        a += 1
        print(frukt, f"er {a} i rekka.", end=" ")

# dex(liste)

tall = [1, 2, 3, 4, 5]
def double(talliste):
    tallx2 = []
    for tall in talliste:
        tall2 = tall * 2
        tallx2.append(tall2)
    print(tallx2)
    
double(tall)
#oppg 3

filmliste = ["Weapons", "Longlegs", "Everything, everywhere all at once", "Kung fu panda", "Shrek"]

def skriv_filmer(filmliste):
    for film in filmliste:
        print(film)

skriv_filmer(filmliste)


def legg_til_film(filmliste, film):
    sjekkFilm(filmliste, film)
    filmliste.append(film)
    


legg_til_film(filmliste, "Shrek")

def sjekkFilm(filmliste, film):       
    if film in filmliste:
       print("Filmen din er i lista!")
    else: 
        print("Filmen er ikke i listen :,(")
       

sjekkFilm(filmliste,)