liste = [1,5,9,-65,-999,20]
summe = 0
laenge = 0
for i in liste:
    if i ==-999:
        break
    if i>=0:
        summe = summe + i
        laenge = laenge + 1  
ergebnis = summe/laenge
print (ergebnis)
