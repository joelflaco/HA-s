""""
Aufgabe 1
(a) Entschlüssele die in der Abbildung gezeigte Antwort von Asterix.

(b) Entschlüssele die Nachricht: Surjudpplhuxqj lvw hlqidfk qxu phjd jxw.

(b) Verschlüssele analog eine selbst gewählte Nachricht. Benutze jetzt eine
Alphabetverschiebung um 7 Zeichen, die 'A' durch 'H' ersetzt ('B' durch 'I', 'C' durch 'I'). Gib
die Nachricht zusammen mit dem Schlüssel an deine Nachbarin bzw. deinen Nachbarn
weiter. Sie bzw. er soll die verschlüsselte Nachricht dann wieder entschlüsseln.

"""


# zeichen = 'A'
# # ord(order) funktion sucht aus ASCII tabelle passende Zahl zu A raus (65)
# zahl = ord('A')
# # print(f"ord: ", A "->", 65)
# print('ord: ', zeichen, '->', zahl)
# zahl = 90
# # chr(character) funktion sucht aus der ASCII Tabelle den passenden Buchstaben zu der 90 raus
# zeichen = chr(zahl)
# # print(f"chr: ", 90 "->", Z)
# print('chr: ', zahl, '->', zeichen)


print("Message Encrypter ")

# input("enter your secret message ")
# letter1 = "A"
# number1 = ord("A")
# number2 = 90
# letter2 = chr(number2)


""""
Aufgabe 2
(a) Das Python-Programm zur Buchstabenverschiebung funktioniert nicht, wenn man z.B.
zeichen = 'T' und schluessel = 10 vorgibt. Teste und begründe.
(b) Ändere das Python-Programm zur Buchstabenverschiebung so ab, dass es für alle
sinnvollen Vorgaben zeichen = ... und schluessel = ... korrekt funktioniert.
"""

zeichen = "T"
schluessel = 10
zahl = ord(zeichen)
# aber hier muss die if bediengung hin da die neue zahl berechnet wird
neueZahl = zahl + schluessel
if neueZahl > 90:
    # hier wird das ergebnis von neueZahl-26 durch das "=" gespeichert
    neueZahl = neueZahl-26
# um von der 91([) auf die 65(A) zu kommen -26 rechnen
neuesZeichen = chr(neueZahl)
print (neuesZeichen)
print()


"""
Aufgabe 3
Der letzte Funktionsaufruf liefert noch nicht das beabsichtigte Ergebnis. Ändere die
Funktionsdefinition geeignet ab. Teste die Funktion dann mit weiteren Funktionsaufrufen.
"""
print("Aufgabe 3")

# Funktionsdefinition
def verschiebung(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl + schluessel
# hier wird die if bedingung eingesetzt
    if neueZahl > 90:
        neueZahl = neueZahl-26
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

# Funktionsaufrufe
print(verschiebung('P', 6))
print(verschiebung('A', 8))
print(verschiebung('T', 9))
print("Aufgabe 3.1")
print(verschiebung('Z', 26))


"""
Aufgabe 4
Ergänze die Funktionsdefinitionen im folgenden Programmgerüst passend. Benutze für die
Funktion verschiebung das (korrekte) Ergebnis aus Aufgabe 3. Die Funktionsdefinition
zur Funktion verschluesselung kann sich am gezeigten Algorithmus orientieren. Günstig
ist es, die Funktion verschiebung dabei zu benutzen. Teste mit verschiedenen
Funktionsaufrufen.
"""
# leeres print für leerzeile
print()
print("Aufgabe 4")

# Funktionsdefinitionen
def verschiebung(zeichen, schluessel):
    zahl = ord(zeichen)
    neueZahl = zahl + schluessel
# hier wird die if bedingung eingesetzt
    if neueZahl > 90:
        neueZahl = neueZahl-26
    neuesZeichen = chr(neueZahl)
    return neuesZeichen

# ALGORITHMUS verschluesselung: Übergabe: text, schluessel
def verschluesselung(text, schluessel):
# neuerText (hier wird das wort JUERGEN verschlüsselt und nicht reingeschrieben
    neuerText = ""
# für alle Zeichen character in text: (character = zeichen)
    for character in text:
# ermittle mit dem schluessel das zu character verschobene Zeichen d
        d = verschiebung(character, schluessel)  
# füge d am Ende an die von neuerText verwaltete Zeichenkette an
# wenn wir neuerText mit d überschreiben...
        neuerText = neuerText+d
# Rückgabe: neuerText
    return neuerText

# Funktionsaufrufe
# mit -(beliebige zahl) und +(beliebige zahl) kann man je nach in welchem in der ASCII Tabelle man gehen möchte verschlüsseln
print(verschluesselung("JUERGEN", 26+4))


"""
Aufgabe 5
(a) Texte, die mit der Funktion verschluesselung verschlüsselt wurden, können mit
derselben Funktion entschlüsselt werden, wenn man den Schlüssel geeignet wählt. Zeige
das mit geeigneten Beispielen.
(b) Die Entschlüsselung von Texten, die mit dem Verschiebeverfahren verschlüsselt wurden,
sollen mit demselben Schlüssel entschlüsselt werden. Entwickle hierfür eine geeignete
Funktion entschluesselung
"""
# noch nicht fertig
# habe hier nur ein wenig ausprobiert
#################################################
print()
print("Aufgabe 5.")

def entschluesselung(text, schluessel):
    schluessel = 4
    neuerText = ""
    for character in text:
        d = verschiebung(character, schluessel)
        neuerText = neuerText+d
        return neuerText
    print(entschluesselung("NYIVKIR", 26-4))
#################################################    
    
    
    