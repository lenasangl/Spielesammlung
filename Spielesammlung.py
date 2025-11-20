#--------------------------------------------------------------------------------------------------------------------
#Spiel 1 Guess a number
import random

max_Versuche_GAN = 15

#Spieler gibt einen Tipp ab
def Versuch_GAN():
    while True:
        try:
            eingabe_GAN = int(input("Gib eine Nummer zwischen 1 und 1000 ein: \n"))
            if 1 <= eingabe_GAN <= 1000:
                return eingabe_GAN
            else:
                print("Deine Eingabe ist ungültig, wähle eine Zahl zwischen 1 und 1000\n")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")

#Versuch wird überprüft
def Versuch_überprüfen_GAN(Versuch_GAN, zufällige_Nummer_GAN):
    if Versuch_GAN == zufällige_Nummer_GAN:
        return "Correct"
    elif Versuch_GAN < zufällige_Nummer_GAN:
        return "Zu niedrig"
    else:
        return "Zu hoch"

#Spielstruktur
def spiel_GAN():
    zufällige_Nummer_GAN = random.randint(1, 1000)
    Versuche_GAN = 0
    gewonnen_GAN = False

    print("Willkommen beim Zahlenraten-Spiel!")
    print(f"Du hast {max_Versuche_GAN} Versuche, um die geheime Zahl zu erraten.")

    while Versuche_GAN < max_Versuche_GAN:
        Versuche_GAN += 1
        eingabe_GAN = Versuch_GAN()  # Hier wird die Eingabe des Spielers abgefragt
        ergebnis_GAN = Versuch_überprüfen_GAN(eingabe_GAN, zufällige_Nummer_GAN)  # Hier wird das Ergebnis überprüft

        if ergebnis_GAN == "Correct":
            print(f"Glückwunsch! Du hast die geheime Zahl {zufällige_Nummer_GAN} in {Versuche_GAN} Versuchen erraten.\n")
            gewonnen_GAN = True
            break
        else:
            print(f"{ergebnis_GAN}. Versuche es erneut!\n")

    if not gewonnen_GAN:
        print(f"Schade, du hast verloren! Die geheime Zahl war {zufällige_Nummer_GAN}.")


def Spiel1():
    if __name__ == "__main__":
        print("Okay, lass uns eine Runde Guess the number spielen. Mach dich bereit!\n")
        print("Soll ich dir die Spielregeln erklären? - Antworte mit Ja oder Nein")
        Spielregeln_GAN = input()

        #Spielregeln
        if (Spielregeln_GAN == "Ja" or Spielregeln_GAN == "ja"):
            print("Dein Ziel ist es, die geheime Nummer zu erraten.\n")
            print("Allgemein gilt:")
            print("Du hast 15 Versuche.")
            print("Ist dein Versuch falsch erhälst du eine der folgenden Informationen: Zu niedrig, Zu hoch")
            print("So hast du die Möglichkeit, dich an die gesuchte Zahl heranzutasten und sie im besten Fall mit möglichst wenig Versuchen zu erraten.\n")
            print("Das wars schon, lass uns starten... Viel Glück!\n")
        elif (Spielregeln_GAN == "Nein" or Spielregeln_GAN == "nein"):
            print("Dann lass uns starten")

        # Das erste Spiel wird hier gestartet
        while True:
            spiel_GAN()
            weiterspielen_GAN = input("Möchtest du weiterspielen? (Ja/Nein): \n")
            if weiterspielen_GAN.lower() != "ja":
                print("Spiel beendet. Ich hoffe es hat dir Spaß gemacht!\n")
                break




#--------------------------------------------------------------------------------------------------------------------
#Spiel 2 Quiz der lustigen Fragen

def Spiel2():
    points_Q = 0
    hints_Q = 1

    # Funktion zur Frage- und Antwortbehandlung
    def frage_und_antwort_Q(frage_Q, antworten_Q, richtige_antwort_Q, hinweis_Q, hint_needed_Q, points_Q, hints_Q):
        print(f"\n{frage_Q}\n")
        for i, antwort_Q in enumerate(antworten_Q, 1):
            print(f"{i}: {antwort_Q}")

        # Hinweise Struktur
        if hints_Q > 0 and hint_needed_Q:
            print("Hinweis: Ja oder Nein?\n")
            hint_needed_input_Q = input()
            if hint_needed_input_Q.lower() == "ja":
                hints_Q -= 1
                print(hinweis_Q)
        
        print("Gib hier deine Antwort ein:")
        answer_Q = input()
        if answer_Q == richtige_antwort_Q:
            print("Richtig")
            points_Q += 1
        else:
            print("Das war leider Falsch")
        
        return points_Q, hints_Q

    # Spielregeln
    print("Okay, lass uns das Quiz der lustigen Fragen spielen. Mach dich bereit!\n")
    print("Soll ich dir die Spielregeln erklären? - Antworte mit Ja oder Nein")
    Spielregeln_Q = input()

    if Spielregeln_Q.lower() == "ja":
        print("Bei diesem Quiz bekommst du 6 lustige Fragen mit dazugehörigen Antworten. Dein Ziel ist es, möglichst viele richtige Antworten zu geben.\n")
        print("Allgemein gilt:")
        print("Du hast während diesem Quiz 1 Hinweis zur Verfügung.")
        print("Mit jeder richtigen Antwort kannst du Punkte sammeln.")
        print("Das wars schon, lass uns starten... Viel Glück!\n")
    elif Spielregeln_Q.lower() == "nein":
        print("Dann lass uns starten\n")

    # Fragen mit Antworten, Hinweise und richtigen Antworten
    fragen_Q = [
        #Frage 1
        ("Wie lange kann ein Faultier brauchen, um einmal die Straße zu überqueren?", 
        ["5 Minuten", "15 Minuten", "30 Minuten", "eine Stunde"], 
        "3", 
        "Antwort 2 ist falsch", 
        True),
        
        #Frage 2
        ("Wie nennt man eine Gruppe von Flamingos?", 
        ["Ein Schwarm", "Eine Parade", "Ein Club", "Eine Welle"], 
        "2", 
        "Antwort 3 ist falsch", 
        True),
        
        #Frage 3
        ("Was passiert, wenn man Pinguinen ein Bild von etwas Lustigem zeigt?", 
        ["Sie laufen weg", "Sie gucken schief", "Sie lachen wirklich", "Sie erkennen es nicht"], 
        "4", 
        "Antwort 1 ist falsch", 
        True),
        
        #Frage 4
        ("Wie viel wiegt ein Wolkenkratzer aus Marshmallows?", 
        ["Es gibt keinen, aber es wurde berechnet, dass es 500 Tonnen wären", 
        "Es gibt keinen, aber es wurde berechnet, dass es 50 Tonnen wären", 
        "Es gibt keinen, aber es wurde berechnet, dass es 2 Tonnen wären", 
        "Es gibt keinen, aber es wurde berechnet, dass es 250 Tonnen wären"], 
        "4", 
        "Antwort 1 ist falsch", 
        True),
        
        #Frage 5
        ("Wie lange schläft eine Schnecke?", 
        ["3 Stunden am Tag", "Eine Woche am Stück", "3 Jahre am Stück", "Schnecken schlafen gar nicht"], 
        "3", 
        "Antwort 4 ist falsch", 
        True),
        
        #Frage 6
        ("Warum kann ein Tintenfisch ein Glas aufschrauben?", 
        ["Weil er acht Arme hat", "Weil er ein Problem mit Stressabbau hat", 
        "Weil er extrem klug ist", "Weil es sein Lieblingsspielzeug ist"], 
        "3", 
        "Antwort 2 ist falsch", 
        True)
    ]

    # Quiz-Schleife
    print("Das Quiz der lustigen Fragen\n")
    for frage, antworten, richtige_antwort, hinweis, hint_needed in fragen_Q:
        points_Q, hints_Q = frage_und_antwort_Q(frage, antworten, richtige_antwort, hinweis, hint_needed, points_Q, hints_Q)

    # erreichte Punkte
    print("\nDu hast " + str(points_Q) + " Punkte erreicht")






#--------------------------------------------------------------------------------------------------------------------
#Spiel 3 Schere Stein Papier

def Spiel3():
    import random

    # Begrüßung
    print("Okay, lass uns eine Runde Schere Stein Papier spielen. Mach dich bereit!\n")

    # Spielregeln Ja/Nein
    print("Soll ich dir die Spielregeln erklären? - Antworte mit Ja oder Nein")
    Spielregeln_SSP = input()

    # Wenn Spielregeln anezeigt werden sollen:
    if (Spielregeln_SSP == "Ja" or Spielregeln_SSP == "ja"):
        print("Zuerst wählst du zwischen Schere, Stein und Papier und gibst deine Wahl ein. \nWährenddessen wählt der Computer ebenfalls eine der 3 Optionen.\n")
        print("Allgemein gilt:")
        print("Schere schneidet Papier → Schere gewinnt")
        print("Papier wickelt Stein ein → Papier gewinnt")
        print("Stein zerschlägt Schere → Stein gewinnt\n")
    elif (Spielregeln_SSP == "Nein" or Spielregeln_SSP == "nein"):
        print("Dann lass uns starten\n")

    # Auswahlmöglichkeiten
    Optionen_SSP = ["Schere", "Stein", "Papier"]

    # Schleife wenn Nutzer weiterspielen möchte
    weiterspielen_SSP = "ja"
    while weiterspielen_SSP.lower() == "ja":
        # Nutzer wählt
        NutzerEntscheidung_SSP = input("Wähle Schere, Stein oder Papier: ")

        # Eingabe von Nutzer wird überprüft
        if NutzerEntscheidung_SSP in Optionen_SSP:
            # Computer wählt
            Wahl_Computer_SSP = random.choice(Optionen_SSP)
            print(f"Du hast dich für {NutzerEntscheidung_SSP} entschieden und der Computer hat {Wahl_Computer_SSP} gewählt")

            # Ergebnisse werden überprüft und Ausgegeben
            if NutzerEntscheidung_SSP == Wahl_Computer_SSP:
                print("Unentschieden!")
            elif (NutzerEntscheidung_SSP == "Schere" and Wahl_Computer_SSP == "Papier") or \
                (NutzerEntscheidung_SSP == "Papier" and Wahl_Computer_SSP == "Stein") or \
                (NutzerEntscheidung_SSP == "Stein" and Wahl_Computer_SSP == "Schere"):
                print("Du gewinnst!")
            else:
                print("Der Computer gewinnt!")
        else:
            # Wenn Nutzereingabe ungültig
            print("Deine Eingabe ist nicht gültig, überprüfe, ob du Schere, Stein oder Papier gewählt hast und achte darauf, dass der erste Buchstabe im Wort groß geschrieben ist.")

        # weiterspielen ja/nein
        weiterspielen_SSP = input("Möchtest du weiterspielen? (Ja/Nein): \n")
        if weiterspielen_SSP.lower() != "ja":
            # Wenn Nutzer NICHT "ja" eingibt, wird das Spiel beendet
            print("Spiel beendet. Ich hoffe es hat dir Spaß gemacht!\n")
            break







#--------------------------------------------------------------------------------------------------------------------
#Spiel 4 TictacToe

def Spiel4():
    import random

    # Funktion zur Anzeige des Spielfelds
    def Spielfeld_TTT(spielfeld):
        print(f"{spielfeld[0]} | {spielfeld[1]} | {spielfeld[2]}")
        print("---------")
        print(f"{spielfeld[3]} | {spielfeld[4]} | {spielfeld[5]}")
        print("---------")
        print(f"{spielfeld[6]} | {spielfeld[7]} | {spielfeld[8]}\n")

    # Spielerzug (1 Spieler, Mensch gegen Computer)
    def Auswahl_Spieler_1Spieler_TTT(spieler, spielfeld):
        if spieler == "X":
            while True:
                move = input(f"Spieler {spieler}, wähle eine Nummer zwischen 1 und 9, um dein Symbol zu setzen: ")
                if move in spielfeld and spielfeld[int(move) - 1] not in ["X", "O"]:
                    spielfeld[int(move) - 1] = spieler
                    break
                else:
                    print("Ungültige Eingabe, gib eine Zahl von 1 bis 9 ein.")
        else:
            while True:
                move = str(random.randint(1, 9))
                if spielfeld[int(move) - 1] not in ["X", "O"]:
                    spielfeld[int(move) - 1] = spieler
                    print(f"Computer platziert {spieler} an der Position {move}")
                    break

    # Spielerzug (2 Spieler)
    def Auswahl_Spieler_2Spieler_TTT(spieler, spielfeld):
        while True:
            move = input(f"Spieler {spieler}, wähle eine Nummer zwischen 1 und 9, um dein Symbol zu setzen: ")
            if move in spielfeld and spielfeld[int(move) - 1] not in ["X", "O"]:
                spielfeld[int(move) - 1] = spieler
                break
            else:
                print("Ungültige Eingabe, gib eine Zahl von 1 bis 9 ein.")

    # Überprüfung, ob jemand gewonnen hat
    def Überprüfung_TTT(spieler, spielfeld):
        Gewinnkombinationen = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in Gewinnkombinationen:
            if spielfeld[combo[0]] == spielfeld[combo[1]] == spielfeld[combo[2]] == spieler:
                return True
        return False

    # 2-Spieler-Modus
    def Zwei_Spieler_Spielen_TTT():
        spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Spielfeld_TTT(spielfeld)
        spieler_X = "X"
        spieler_O = "O"

        for _ in range(9):
            if _ % 2 == 0:
                print("Spieler X ist am Zug.")
                Auswahl_Spieler_2Spieler_TTT(spieler_X, spielfeld)
            else:
                print("Spieler O ist am Zug.")
                Auswahl_Spieler_2Spieler_TTT(spieler_O, spielfeld)
            Spielfeld_TTT(spielfeld)

            if Überprüfung_TTT(spieler_X, spielfeld):
                print(f"Herzlichen Glückwunsch! Spieler {spieler_X} gewinnt!")
                return
            if Überprüfung_TTT(spieler_O, spielfeld):
                print(f"Herzlichen Glückwunsch! Spieler {spieler_O} gewinnt!")
                return
        print("Unentschieden!")

    # 1-Spieler-Modus (Mensch gegen Computer)
    def Ein_Spieler_Spielen_TTT():
        spielfeld = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Spielfeld_TTT(spielfeld)
        spieler_X = "X"
        spieler_O = "O"

        for _ in range(9):
            if _ % 2 == 0:
                Auswahl_Spieler_1Spieler_TTT(spieler_X, spielfeld)
            else:
                Auswahl_Spieler_1Spieler_TTT(spieler_O, spielfeld)
            Spielfeld_TTT(spielfeld)

            if Überprüfung_TTT(spieler_X, spielfeld):
                print(f"Glückwunsch! Spieler {spieler_X} gewinnt!")
                return
            if Überprüfung_TTT(spieler_O, spielfeld):
                print("Sorry! Der Computer gewinnt :(")
                return
        print("Unentschieden!")

    # Start des Spiels
    def spielstarten_TTT():
        print("Okay, lass uns eine Runde Tic Tac Toe spielen. Mach dich bereit!\n")
        print("Soll ich dir die Spielregeln erklären? - Antworte mit Ja oder Nein")
        spielregeln = input()

        if spielregeln.lower() == "ja":
            print("Dein Ziel ist es, drei deiner Symbole nebeneinander zu platzieren.")
            print("Das Spielfeld ist 3x3 Felder groß, und jedes Feld ist nummeriert.")
            print("Platziere dein Symbol, indem du die entsprechende Zahl eingibst.")
            print("Der Spieler, der zuerst drei Symbole in eine Zeile, Spalte oder Diagonale setzt, gewinnt.")
            print("Viel Glück!\n")

        print("1 oder 2 Spieler?")
        anzahl_spieler = input()

        if anzahl_spieler == "1":
            print("Du spielst gegen den Computer. Du bist X! Viel Glück :)\n")
            Ein_Spieler_Spielen_TTT()
        elif anzahl_spieler == "2":
            print("Ihr spielt gegeneinander. Einigt euch, wer X und wer O ist. Viel Spaß :)\n")
            Zwei_Spieler_Spielen_TTT()
        else:
            print("Ungültige Eingabe. Bitte gib '1' oder '2' ein.")

    # Hauptschleife für das Spiel
    def main_TTT():
        while True:
            spielstarten_TTT()
            weiterspielen = input("Möchtest du weiterspielen? (Ja/Nein): \n")
            if weiterspielen.lower() != "ja":
                print("Spiel beendet. Ich hoffe, es hat dir Spaß gemacht! \n")
                break

    main_TTT()









#--------------------------------------------------------------------------------------------------------------------
#Spielesammlung an sich

def main_Spielesammlung():
    #Begrüßung
    print("Willkommen zur Spielesammlung!")
    print("Hier hast du die Möglichkeit 4 unterschiedliche Spiele zu spielen.")

    while True:
        #Spielmöglichkeiten
        print("\nWähle ein Spiel aus:")
        print("1. Guess the number")
        print("2. Das Quiz der lustigen Fragen")
        print("3. Schere Stein Papier")
        print("4. Tic Tac Toe")

        #Abfrage welches Spiel gespielt werden möchte
        spielwahl = input("Gib die Nummer des gewünschten Spiels ein (1/2/3/4): \n")

        if spielwahl == "1":
            Spiel1()
        elif spielwahl == "2":
            Spiel2()
        elif spielwahl == "3":
            Spiel3()
        elif spielwahl == "4":
            Spiel4()
        else:
            print("Ungültige Auswahl. Bitte wähle eine der Optionen (1/2/3/4).")
            continue

        # Spielesammlung beenden oder noch ein Spiel
        weiterspielen = input("Möchtest du noch ein anderes Spiel spielen? (Ja/Nein): ")
        if weiterspielen.lower() != "ja":
            print("Danke fürs Spielen! Auf Wiedersehen!")
            break


if __name__ == "__main__":
    main_Spielesammlung()




#--------------------------------------------------------------------------------------------------------------------
#Allgemein:
#Damit ich bei den verschiedenen Variaben usw. nicht durcheinanderkomme,
#habe ich jedem Spiel kürzel gegeben und diese dann im jeweiligen Spiel verwendet.

#Damit man die Bennungen nachvollziehen kann hier die Erklärung der Kürzel:
# GAN - Guess a number
# Q - Quiz
# SSP - Schere Stein Papier
# TTT - TicTacToe