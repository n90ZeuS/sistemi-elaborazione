# T10 — Stringhe
# Esempi per la lezione frontale 10
# Indici, slicing, ciclo for su una stringa, metodi delle stringhe, formattazione dei numeri
#
# Accanto a ogni stampa trovate, in commento, il risultato atteso.

# =============================================================================
# 1. Indici e immutabilità
# =============================================================================
print("--- 1. Indici e immutabilità ---")

testo: str = "Statistica"

# Il primo carattere ha indice 0, l'ultimo ha indice len(testo) - 1
print(testo[0])            # S
print(testo[3])            # t
print(testo[len(testo) - 1])  # a
print(testo[-1])           # a   (gli indici negativi contano dalla fine)
print(testo[-2])           # c
print(len(testo))          # 10

# in controlla se una stringa è contenuta in un'altra
print("ist" in testo)      # True
print("IST" in testo)      # False (maiuscole e minuscole sono diverse)

# Le stringhe sono immutabili: la riga seguente darebbe
# TypeError: 'str' object does not support item assignment
# testo[0] = "s"

# Per avere una stringa diversa se ne crea una nuova
testo_minuscolo: str = "s" + testo[1:]
print(testo_minuscolo)     # statistica
print(testo)               # Statistica (l'originale non cambia)
print()


# =============================================================================
# 2. Slicing
# =============================================================================
print("--- 2. Slicing ---")

# s[inizio:fine:passo]: da inizio a fine esclusa, come in range()
s: str = "Programmazione"

print(s[0:6])     # Progra
print(s[:6])      # Progra          (manca l'inizio: si parte da 0)
print(s[6:])      # mmazione        (manca la fine: si arriva in fondo)
print(s[-6:])     # azione          (gli ultimi sei caratteri)
print(s[2:5])     # ogr
print(s[::2])     # Pormain         (un carattere sì e uno no)
print(s[::-1])    # enoizammargorP  (al contrario)

# Lo slicing non dà errore se gli indici escono dalla stringa
print(s[10:100])  # ione
print(s[20:])     # (stringa vuota: stampa una riga vuota)

# Esempio: separare anno, mese e giorno da una data scritta come aaaa-mm-gg
data: str = "2026-10-27"
anno: str = data[:4]
mese: str = data[5:7]
giorno: str = data[8:]
print(f"Giorno {giorno}, mese {mese}, anno {anno}")  # Giorno 27, mese 10, anno 2026
print()


# =============================================================================
# 3. Scorrere una stringa con for
# =============================================================================
print("--- 3. Scorrere una stringa ---")

parola: str = "zucca"

# A ogni giro la variabile vale un carattere
for carattere in parola:
    print(carattere, end=" ")
print()                    # z u c c a

# Se serve anche la posizione si scorrono gli indici
for i in range(len(parola)):
    print(f"{i}:{parola[i]}", end=" ")
print()                    # 0:z 1:u 2:c 3:c 4:a

# Pattern contatore: quante vocali ci sono?
frase: str = "la statistica è una scienza"
n_vocali: int = 0
for carattere in frase:
    if carattere in "aeiouàèéìòù":
        n_vocali += 1
print(f"Vocali in '{frase}': {n_vocali}")  # Vocali in 'la statistica è una scienza': 11

# Pattern accumulatore: costruire una stringa nuova un carattere alla volta
rovesciata: str = ""
for carattere in parola:
    rovesciata = carattere + rovesciata   # il nuovo carattere va davanti
print(rovesciata)          # accuz
print(parola[::-1])        # ananab (stesso risultato con lo slicing)

# Pattern ricerca: posizione della prima cifra
codice: str = "ABC7X9"
posizione: int = -1
for i in range(len(codice)):
    if codice[i].isdigit():
        posizione = i
        break
print(f"Prima cifra in posizione {posizione}")  # Prima cifra in posizione 3
print()


# =============================================================================
# 4. Metodi delle stringhe
# Ogni metodo restituisce un valore nuovo e lascia invariata la stringa originale.
# =============================================================================
print("--- 4. Metodi delle stringhe ---")

# strip, lstrip, rstrip: tolgono spazi, tabulazioni e a capo ai bordi
dato: str = "  42.5  \n"
print(repr(dato))            # '  42.5  \n'
print(repr(dato.strip()))    # '42.5'
print(repr(dato.lstrip()))   # '42.5  \n'
print(repr(dato.rstrip()))   # '  42.5'

# replace: sostituisce tutte le occorrenze
valore: str = "valore: N/A"
print(valore.replace("N/A", "0"))       # valore: 0
numeri: str = "1,2,,4,,6"
print(numeri.replace(",,", ",0,"))      # 1,2,0,4,0,6
decimale: str = "3,14"
print(decimale.replace(",", "."))       # 3.14  (virgola decimale all'italiana)
print(valore)                           # valore: N/A (l'originale non cambia)

# count: quante volte compare una sottostringa
print("statistica".count("t"))    # 3
print("statistica".count("ti"))   # 2
print("statistica".count("x"))    # 0

# find e index: posizione della prima occorrenza
titolo: str = "La media campionaria"
print(titolo.find("media"))     # 3
print(titolo.find("varianza"))  # -1 (non trovata)
print(titolo.index("media"))    # 3
# titolo.index("varianza") darebbe ValueError: substring not found

# startswith e endswith: prefisso e suffisso
nome_file: str = "dati_2024.csv"
print(nome_file.startswith("dati"))   # True
print(nome_file.endswith(".csv"))     # True
print(nome_file.endswith(".xlsx"))    # False

# upper, lower, title, capitalize: maiuscole e minuscole
corso: str = "statistica Descrittiva"
print(corso.upper())        # STATISTICA DESCRITTIVA
print(corso.lower())        # statistica descrittiva
print(corso.title())        # Statistica Descrittiva
print(corso.capitalize())   # Statistica descrittiva

# Confronto senza badare alle maiuscole: si porta tutto in minuscolo
risposta: str = "  Si "
if risposta.strip().lower() == "si":
    print("Confermato")     # Confermato

# isdigit, isalpha, isalnum: controllano il contenuto
print("42".isdigit())       # True
print("3.14".isdigit())     # False (il punto non è una cifra)
print("-5".isdigit())       # False (il segno meno non è una cifra)
print("abc".isalpha())      # True
print("abc123".isalnum())   # True
print("abc 123".isalnum())  # False (lo spazio non è né lettera né cifra)
print("".isdigit())         # False (stringa vuota)

# I metodi si possono concatenare: si applicano da sinistra a destra
grezzo: str = "   mARIO rossi   "
print(grezzo.strip().title())   # Mario Rossi
print()


# =============================================================================
# 5. Formattare i numeri nelle f-string
# =============================================================================
print("--- 5. Formattare i numeri ---")

# .Nf: N cifre decimali
media: float = 27.4567
print(f"Media: {media:.2f}")    # Media: 27.46
print(f"Media: {media:.1f}")    # Media: 27.5
print(f"Media: {media:.0f}")    # Media: 27

# .N%: percentuale con N decimali (il valore viene moltiplicato per 100)
quota: float = 0.0325
print(f"Quota: {quota:.1%}")    # Quota: 3.2%
print(f"Quota: {quota:.0%}")    # Quota: 3%

# Il formato cambia solo la stampa: la variabile mantiene tutte le cifre
print(media)                    # 27.4567

# Esempio: percentuale di cifre in un codice
matricola: str = "AB123456"
n_cifre: int = 0
for carattere in matricola:
    if carattere.isdigit():
        n_cifre += 1
print(f"Cifre: {n_cifre} su {len(matricola)} ({n_cifre / len(matricola):.1%})")
# Cifre: 6 su 8 (75.0%)
print()


# =============================================================================
# 6. Esempio completo: pulire e controllare un dato
# =============================================================================
print("--- 6. Pulire e controllare un dato ---")

# Un valore letto da un file: spazi ai bordi e virgola decimale
grezzo_peso: str = "  72,5 kg "

pulito: str = grezzo_peso.strip()                   # '72,5 kg'
if pulito.endswith("kg"):
    pulito = pulito[:-2].strip()                    # '72,5'
pulito = pulito.replace(",", ".")                   # '72.5'

# Prima di convertire controlliamo che, tolto il punto, restino solo cifre
if pulito.count(".") <= 1 and pulito.replace(".", "").isdigit():
    peso: float = float(pulito)
    print(f"Peso: {peso:.1f} kg")                   # Peso: 72.5 kg
else:
    print(f"Valore non valido: '{grezzo_peso}'")


print("\nFine degli esempi T10")
