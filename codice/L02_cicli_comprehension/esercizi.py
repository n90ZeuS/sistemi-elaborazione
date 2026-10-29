# L02 — Cicli e stringhe (esercizi di Halloween)
# Soluzioni degli esercizi del laboratorio 02
#
# Ogni esercizio corrisponde a un file della traccia (nome tra parentesi).
# I programmi leggono i dati con input(): eseguendo questo file vengono
# chiesti i dati di tutti gli esercizi, uno dopo l'altro. Per provarne
# uno solo, copiatelo in un file a parte.


# ============================================================================
# ESERCIZIO 1: epidemia zombie — epidemia.py
# ============================================================================
print("--- Esercizio 1: Epidemia zombie ---")
giorni: int = int(input("Giorni: "))

infetti: int = 1
for giorno in range(1, giorni + 1):
    print(f"Giorno {giorno}: {infetti} infetti")
    infetti = infetti * 2
print()


# ============================================================================
# ESERCIZIO 2: quando cade la città — apocalisse.py
# ============================================================================
print("--- Esercizio 2: Quando cade la città ---")
abitanti: int = int(input("Abitanti: "))

giorno: int = 1
infetti: int = 1
while infetti <= abitanti:
    giorno += 1
    infetti = infetti * 2

print(f"La città cade il giorno {giorno}: {infetti} infetti")
print()


# ============================================================================
# ESERCIZIO 3: venerdì 17 — venerdi17.py
# ============================================================================
print("--- Esercizio 3: Venerdì 17 ---")
n: int = int(input("Controlla i numeri fino a: "))

sfortunati: int = 0
for i in range(1, n + 1):
    if i % 17 == 0 or "17" in str(i):
        sfortunati += 1

print(f"Numeri sfortunati: {sfortunati}")
print(f"Percentuale: {sfortunati / n:.1%}")
print()


# ============================================================================
# ESERCIZIO 4: la cena di dracula — cena_dracula.py
# ============================================================================
print("--- Esercizio 4: La cena di Dracula ---")
sacche: int = int(input("Sacche di sangue: "))

if sacche <= 0:
    print("Errore: serve almeno una sacca")
else:
    possibilita: int = 0
    for commensali in range(1, sacche + 1):
        if sacche % commensali == 0:
            print(f"Commensali {commensali}, sacche a testa {sacche // commensali}")
            possibilita += 1
    print(f"Possibilità: {possibilita}")

    if possibilita == 2:
        print(f"{sacche} è primo: si divide solo tra 1 o {sacche} commensali")
print()


# ============================================================================
# ESERCIZIO 5: l'epitaffio — epitaffio.py
# ============================================================================
print("--- Esercizio 5: L'epitaffio ---")
PREZZO_LETTERA: int = 2
PREZZO_CIFRA: int = 3
PREZZO_ALTRO: int = 1      # gli spazi sono gratis

epitaffio: str = input("Epitaffio: ")

lettere: int = 0
cifre: int = 0
spazi: int = 0
altri: int = 0
for carattere in epitaffio:
    if carattere.isalpha():
        lettere += 1
    elif carattere.isdigit():
        cifre += 1
    elif carattere == " ":
        spazi += 1
    else:
        altri += 1

costo: int = (lettere * PREZZO_LETTERA
              + cifre * PREZZO_CIFRA
              + altri * PREZZO_ALTRO)

print(f"Lettere: {lettere}  Cifre: {cifre}")
print(f"Spazi: {spazi}  Altri: {altri}")
print(f"Costo dell'incisione: {costo} EUR")
if len(epitaffio) > 0:
    print(f"Lettere sul totale: {lettere / len(epitaffio):.1%}")
print()


# ============================================================================
# ESERCIZIO 6: anagrammi maledetti — anagrammi.py
# ============================================================================
print("--- Esercizio 6: Anagrammi maledetti ---")
ALFABETO: str = "abcdefghijklmnopqrstuvwxyz"

prima: str = input("Prima parola: ").lower().replace(" ", "")
seconda: str = input("Seconda parola: ").lower().replace(" ", "")

anagrammi: bool = True
for lettera in ALFABETO:
    if anagrammi and prima.count(lettera) != seconda.count(lettera):
        anagrammi = False
        print(f"Lettera {lettera}: {prima.count(lettera)} nella prima, {seconda.count(lettera)} nella seconda")

if anagrammi:
    print("Sono anagrammi")
else:
    print("Non sono anagrammi")
print()


# ============================================================================
# ESERCIZIO 7: il bottino della notte — bottino.py
# ============================================================================
print("--- Esercizio 7: Il bottino della notte ---")
case: int = 0
totale: int = 0
porte_chiuse: int = 0
piu_caramelle: int = 0
casa_generosa: int = 0

testo: str = input("Casa 1, caramelle (fine per finire): ")
while testo.strip().lower() != "fine":
    caramelle: int = int(testo)
    if caramelle < 0:
        print("Valore non valido, ignorato")
    else:
        case += 1
        totale += caramelle
        if caramelle == 0:
            porte_chiuse += 1
        if caramelle > piu_caramelle:
            piu_caramelle = caramelle
            casa_generosa = case
    testo = input(f"Casa {case + 1}, caramelle (fine per finire): ")

if case == 0:
    print("Nessuna casa visitata")
else:
    print(f"Case visitate: {case}")
    print(f"Caramelle totali: {totale}")
    print(f"Media per casa: {totale / case:.1f}")
    if piu_caramelle > 0:
        print(f"Casa più generosa: la {casa_generosa}, con {piu_caramelle} caramelle")
    print(f"Porte chiuse: {porte_chiuse / case:.1%}")
print()


# ============================================================================
# ESERCIZIO 8: il login di dracula — login_dracula.py
# ============================================================================
print("--- Esercizio 8: Il login di Dracula ---")
valida: bool = False

while not valida:
    password: str = input("Password: ")

    maiuscola: bool = False
    cifra: bool = False
    spazio: bool = False
    for carattere in password:
        if carattere.isupper():
            maiuscola = True
        elif carattere.isdigit():
            cifra = True
        elif carattere == " ":
            spazio = True

    lunga: bool = len(password) >= 8
    minuscola: str = password.lower()
    proibita: bool = "aglio" in minuscola or "croce" in minuscola
    valida = lunga and maiuscola and cifra and not spazio and not proibita

    if not lunga:
        print("- servono almeno 8 caratteri")
    if not maiuscola:
        print("- manca una lettera maiuscola")
    if not cifra:
        print("- manca una cifra")
    if spazio:
        print("- niente spazi")
    if proibita:
        print("- parola proibita: il conte non gradisce")

print("Benvenuto nel castello")
print()


# ============================================================================
# SFIDA: apocalisse con esercito — apocalisse_esercito.py
# ============================================================================
print("--- Sfida: Apocalisse con esercito ---")
CRESCITA: float = 0.5               # gli zombie sopravvissuti crescono del 50%
ELIMINATI_PER_SOLDATO: int = 2
ZOMBIE_PER_SOLDATO_INFETTO: int = 10
MAX_GIORNI: int = 30

zombie: int = int(input("Zombie iniziali: "))
soldati: int = int(input("Soldati iniziali: "))

giorno: int = 0
print(f"Giorno {giorno}: {zombie} zombie, {soldati} soldati")
while giorno < MAX_GIORNI and zombie > 0 and soldati > 0:
    giorno += 1
    # infettati ed eliminati si calcolano con i valori di inizio giornata
    infettati: int = zombie // ZOMBIE_PER_SOLDATO_INFETTO
    if infettati > soldati:
        infettati = soldati
    eliminati: int = soldati * ELIMINATI_PER_SOLDATO
    if eliminati > zombie:
        eliminati = zombie
    sopravvissuti: int = zombie - eliminati
    contagi: int = int(sopravvissuti * CRESCITA)
    zombie = sopravvissuti + contagi + infettati
    soldati -= infettati
    print(f"Giorno {giorno}: infettati {infettati},",
          f"eliminati {eliminati}, sopravvissuti {sopravvissuti},",
          f"contagi {contagi} -> {zombie} zombie, {soldati} soldati")

if zombie == 0:
    print(f"Vittoria il giorno {giorno}, restano {soldati} soldati")
elif soldati == 0:
    print(f"Sconfitta il giorno {giorno}, restano {zombie} zombie")
else:
    print(f"Dopo {MAX_GIORNI} giorni la guerra continua")
print()


# ============================================================================
print("=" * 60)
print("Fine degli esercizi del laboratorio 02")
print("=" * 60)
