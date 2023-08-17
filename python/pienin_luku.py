#LUT Johdatus ohjelmointiin- Kurssi
#Tehtävä: L04-T3
#Nimi:  Lauri Heikkinen
###################################################

laskuri = 0
pienin = 0

print("Tämä ohjelma etsii antamistasi kokonaisluvuista pienimmän.")

numerot = []

while (True):
    luku = int(input("Anna kokonaisluku väliltä 1-100 (-1 lopettaa): "))
    numerot.append(luku)
    laskuri += 1

    if (luku == -1):
        laskuri = laskuri + 1
        break

    if (luku < 1) or (luku > 100):
        print("Väärä syöte. Vain arvosanat 1-100 kelpaavat (-1 lopettaa).")
        luku -= luku
        laskuri -= 1
        luku -= luku
        
pienin = int(inf)
for i in numerot:
	if i < pienin:
		pienin = i
  
print("Antamistasi luvuista pienin oli:", pienin)
print("Kiitos ohjelman käytöstä.")
	