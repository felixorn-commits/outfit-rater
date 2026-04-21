# Funktion som ger poäng beroende på vald överdel
def ge_poang_overdel(overdel):
    if overdel == "hoodie":
        return 2
    elif overdel == "skjorta":
        return 3
    elif overdel == "t-shirt":
        return 1
    else:
        return 0  # Om användaren skriver något annat


# Funktion som ger poäng beroende på vald underdel
def ge_poang_underdel(underdel):
    if underdel == "svarta jeans":
        return 3
    elif underdel == "blå jeans":
        return 2
    elif underdel == "mjukisbyxor":
        return 1
    else:
        return 0


# Funktion som ger poäng beroende på valda skor
def ge_poang_skor(skor):
    if skor == "vita sneakers":
        return 3
    elif skor == "boots":
        return 2
    elif skor == "löparskor":
        return 1
    else:
        return 0


# Funktion som ger poäng beroende på stil
def ge_poang_stil(stil):
    if stil == "casual":
        return 2
    elif stil == "elegant":
        return 3
    elif stil == "street":
        return 2
    else:
        return 0


# Funktion som ger ett omdöme baserat på total poäng
def ge_omdome(total_poang):
    if total_poang >= 10:
        return "10/10 - Riktigt stark outfit."
    elif total_poang >= 7:
        return "7/10 - Snygg och välbalanserad outfit."
    elif total_poang >= 4:
        return "5/10 - Helt okej, men ganska enkel."
    else:
        return "3/10 - Outfiten behöver förbättras."


# Funktion som ger ett stilråd beroende på vald stil
def ge_stilrad(stil):
    if stil == "casual":
        return "Tips: Casual blir ofta bäst när det ser avslappnat men ändå rent ut."
    elif stil == "elegant":
        return "Tips: Elegant stil passar extra bra med enkla färger och rena linjer."
    elif stil == "street":
        return "Tips: Streetstil blir ofta bättre om ett plagg får sticka ut tydligt."
    else:
        return "Inget stilråd kunde ges."


# Huvudloop. Kör programmet om och om igen tills användaren avslutar
while True:
    print("\n--- OUTFIT RATER PRO ---")

    # Användaren får skriva in sina val
    overdel = input("Välj överdel (hoodie, skjorta, t-shirt): ").lower()
    underdel = input("Välj underdel (svarta jeans, blå jeans, mjukisbyxor): ").lower()
    skor = input("Välj skor (vita sneakers, boots, löparskor): ").lower()
    stil = input("Välj stil (casual, elegant, street): ").lower()

    # Startvärde för poäng
    total_poang = 0

    # Vi lägger ihop poängen från alla funktioner
    total_poang += ge_poang_overdel(overdel)
    total_poang += ge_poang_underdel(underdel)
    total_poang += ge_poang_skor(skor)
    total_poang += ge_poang_stil(stil)

    # Skriver ut resultatet
    print("\nDin outfit fick", total_poang, "poäng.")
    print(ge_omdome(total_poang))  # Visar omdöme
    print(ge_stilrad(stil))        # Visar stilråd

    # Frågar om användaren vill köra igen
    igen = input("\nVill du testa en ny outfit? (ja/nej): ").lower()

    # Om användaren inte skriver "ja" avslutas programmet
    if igen != "ja":
        print("Programmet avslutas.")
        break