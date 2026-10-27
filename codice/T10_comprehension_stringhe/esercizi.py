# T10 — Stringhe
# Esercizi per la lezione frontale 10
# Vocali e consonanti, palindromi, cifrario di Cesare, controllo di un'email,
# controllo di una password
#
# Ogni esercizio parte da dati scritti nel codice: cambiate i valori
# e rilanciate il programma per provare casi diversi.
# Accanto a ogni risultato trovate, in commento, il valore atteso.

# =============================================================================
# Esercizio 1: Vocali, consonanti e altri caratteri
# Contare vocali, consonanti, cifre e spazi di una frase (pattern contatore).
# Le maiuscole vanno contate come le minuscole.
# =============================================================================
print("--- Esercizio 1: Vocali e consonanti ---")

frase: str = "Nel 2026 la Statistica compie 3 secoli"

vocali: int = 0
consonanti: int = 0
cifre: int = 0
spazi: int = 0

for carattere in frase.lower():
    if carattere in "aeiou":
        vocali += 1
    elif carattere.isalpha():
        consonanti += 1
    elif carattere.isdigit():
        cifre += 1
    elif carattere == " ":
        spazi += 1

print(f"  Frase: '{frase}'")
print(f"  Vocali: {vocali}")          # atteso: 12
print(f"  Consonanti: {consonanti}")  # atteso: 15
print(f"  Cifre: {cifre}")            # atteso: 5
print(f"  Spazi: {spazi}")            # atteso: 6
print(f"  Totale: {len(frase)}")      # atteso: 38 (12 + 15 + 5 + 6)
print()


# =============================================================================
# Esercizio 2: Palindromi
# Una frase è palindroma se si legge uguale nei due versi,
# senza contare spazi e maiuscole.
# =============================================================================
print("--- Esercizio 2: Palindromi ---")

candidata: str = "I topi non avevano nipoti"

# Tolgo gli spazi e porto tutto in minuscolo
pulita: str = candidata.replace(" ", "").lower()

# Versione 1: confronto con la stringa rovesciata
palindroma: bool = pulita == pulita[::-1]

# Versione 2: confronto il primo carattere con l'ultimo, il secondo con
# il penultimo e così via (pattern ricerca: mi fermo alla prima differenza)
palindroma_ciclo: bool = True
for i in range(len(pulita) // 2):
    if pulita[i] != pulita[len(pulita) - 1 - i]:
        palindroma_ciclo = False
        break

print(f"  '{candidata}' -> '{pulita}'")      # atteso: 'itopinonavevanonipoti'
print(f"  Palindroma (slicing): {palindroma}")      # atteso: True
print(f"  Palindroma (ciclo):   {palindroma_ciclo}")  # atteso: True
# Altri casi da provare: "anna" -> True, "Python" -> False, "Ai lati d'Italia" -> False
# (l'apostrofo resta nella stringa: provate a toglierlo con un altro replace)
print()


# =============================================================================
# Esercizio 3: Cifrario di Cesare
# Ogni lettera viene sostituita da quella che si trova `chiave` posizioni
# più avanti nell'alfabeto; dopo la z si riparte dalla a.
# Gli altri caratteri (spazi, punteggiatura) restano uguali.
# isupper() restituisce True se il carattere è una lettera maiuscola
# (islower(), usato nell'esercizio 5, fa lo stesso per le minuscole).
# =============================================================================
print("--- Esercizio 3: Cifrario di Cesare ---")

alfabeto: str = "abcdefghijklmnopqrstuvwxyz"
messaggio: str = "Ciao Mondo!"
chiave: int = 3

cifrato: str = ""
for carattere in messaggio:
    posizione: int = alfabeto.find(carattere.lower())
    if posizione == -1:
        cifrato += carattere              # non è una lettera: resta uguale
    else:
        nuova: str = alfabeto[(posizione + chiave) % 26]
        if carattere.isupper():           # conservo la maiuscola
            nuova = nuova.upper()
        cifrato += nuova

# Per decifrare si sposta all'indietro della stessa chiave
decifrato: str = ""
for carattere in cifrato:
    posizione = alfabeto.find(carattere.lower())
    if posizione == -1:
        decifrato += carattere
    else:
        nuova = alfabeto[(posizione - chiave) % 26]
        if carattere.isupper():
            nuova = nuova.upper()
        decifrato += nuova

print(f"  Messaggio: {messaggio}")    # atteso: Ciao Mondo!
print(f"  Cifrato:   {cifrato}")      # atteso: Fldr Prqgr!
print(f"  Decifrato: {decifrato}")    # atteso: Ciao Mondo!
# Altri casi da provare: "xyz" con chiave 3 -> "abc"
# Con chiave 13 cifrare due volte restituisce il messaggio originale.
print()


# =============================================================================
# Esercizio 4: Controllo di un indirizzo email
# Regole semplici:
#   - nessuno spazio
#   - esattamente una @
#   - almeno un carattere prima della @
#   - dopo la @ un dominio con almeno un punto, che non inizia e non finisce con il punto
# Si stampa il primo problema trovato, oppure "Email valida".
# =============================================================================
print("--- Esercizio 4: Controllo email ---")

email: str = "mario.rossi@studenti.unipd.it"

chiocciola: int = email.find("@")
utente: str = email[:chiocciola]
dominio: str = email[chiocciola + 1:]

if " " in email:
    esito: str = "Contiene spazi"
elif email.count("@") != 1:
    esito = f"Deve contenere una sola @ (trovate: {email.count('@')})"
elif len(utente) == 0:
    esito = "Manca la parte prima della @"
elif "." not in dominio:
    esito = "Il dominio deve contenere un punto"
elif dominio.startswith(".") or dominio.endswith("."):
    esito = "Il dominio non può iniziare o finire con il punto"
else:
    esito = "Email valida"

print(f"  {email}: {esito}")
# atteso: mario.rossi@studenti.unipd.it: Email valida
print(f"  Utente: {utente}")     # atteso: mario.rossi
print(f"  Dominio: {dominio}")   # atteso: studenti.unipd.it
# Altri casi da provare:
#   "senza-chiocciola.it"  -> Deve contenere una sola @ (trovate: 0)
#   "@unipd.it"            -> Manca la parte prima della @
#   "mario@@unipd.it"      -> Deve contenere una sola @ (trovate: 2)
#   "mario@unipd"          -> Il dominio deve contenere un punto
#   "mario@.unipd.it"      -> Il dominio non può iniziare o finire con il punto
#   "mario rossi@unipd.it" -> Contiene spazi
print()


# =============================================================================
# Esercizio 5: Controllo di una password
# Una password è accettata se ha almeno 8 caratteri e contiene almeno
# una maiuscola, una minuscola e una cifra. Stampare anche la quota di
# cifre sul totale dei caratteri.
# =============================================================================
print("--- Esercizio 5: Controllo password ---")

password: str = "Statistica2026"

n_maiuscole: int = 0
n_minuscole: int = 0
n_cifre: int = 0
for carattere in password:
    if carattere.isupper():
        n_maiuscole += 1
    elif carattere.islower():
        n_minuscole += 1
    elif carattere.isdigit():
        n_cifre += 1

print(f"  Lunghezza: {len(password)}")  # atteso: 14
print(f"  Maiuscole: {n_maiuscole}, minuscole: {n_minuscole}, cifre: {n_cifre}")
# atteso: Maiuscole: 1, minuscole: 9, cifre: 4
print(f"  Quota di cifre: {n_cifre / len(password):.1%}")  # atteso: 28.6%

if len(password) < 8:
    print("  Password rifiutata: servono almeno 8 caratteri")
elif n_maiuscole == 0 or n_minuscole == 0 or n_cifre == 0:
    print("  Password rifiutata: servono maiuscole, minuscole e cifre")
else:
    print("  Password accettata")           # atteso: Password accettata
# Altri casi da provare: "corta1A" -> troppo corta, "statistica2026" -> manca la maiuscola
print()


print("Fine degli esercizi T10")
