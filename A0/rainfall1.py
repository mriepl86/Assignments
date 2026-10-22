
def rainfall1(liste):

    summe = 0
    laenge = 0

    for i in liste:
        if i ==-999:
            break
        if i>=0:
            summe = summe + i
            laenge = laenge + 1  


    try:
        ergebnis = summe/laenge

    except ZeroDivisionError as msg:
        return "Leere Liste (Fehler: {}).".format(msg)
    else: 
        return ergebnis
