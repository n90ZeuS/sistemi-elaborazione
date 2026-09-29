# T09 — Cicli
# Esempi per la lezione frontale 9
# for, range, enumerate, zip, while, break/continue, pattern di iterazione

# =============================================================================
# 1. Ciclo for e range()
# =============================================================================
print("--- 1. Ciclo for e range() ---")

# range(stop): da 0 a stop-1
numeri_0_4: list[int] = list(range(5))
assert numeri_0_4 == [0, 1, 2, 3, 4]
print(f"  range(5)       = {numeri_0_4}")

# range(start, stop): da start a stop-1
numeri_2_7: list[int] = list(range(2, 8))
assert numeri_2_7 == [2, 3, 4, 5, 6, 7]
print(f"  range(2, 8)    = {numeri_2_7}")

# range(start, stop, step): con passo
pari_0_10: list[int] = list(range(0, 11, 2))
assert pari_0_10 == [0, 2, 4, 6, 8, 10]
print(f"  range(0,11,2)  = {pari_0_10}")

# range con passo negativo (contare all'indietro)
conto_alla_rovescia: list[int] = list(range(5, 0, -1))
assert conto_alla_rovescia == [5, 4, 3, 2, 1]
print(f"  range(5,0,-1)  = {conto_alla_rovescia}")


# =============================================================================
# 2. enumerate() — indice + elemento
# =============================================================================
print("\n--- 2. enumerate() ---")

materie: list[str] = ["Analisi", "Fisica", "Programmazione", "Algebra"]

# enumerate restituisce coppie (indice, elemento)
print("  Materie del primo anno:")
for i, materia in enumerate(materie):
    print(f"    {i}: {materia}")

# enumerate con start personalizzato
print("  Numerazione da 1:")
for i, materia in enumerate(materie, start=1):
    print(f"    {i}. {materia}")

# Uso tipico: trovare la posizione di un elemento
indice_prog: int = -1
for i, materia in enumerate(materie):
    if materia == "Programmazione":
        indice_prog = i
        break
assert indice_prog == 2


# =============================================================================
# 3. zip() — iterazione parallela
# =============================================================================
print("\n--- 3. zip() ---")

nomi: list[str] = ["Alice", "Bob", "Carla"]
voti: list[int] = [28, 25, 30]
lodi: list[bool] = [False, False, True]

# zip combina le liste elemento per elemento
print("  Risultati esame:")
for nome, voto, lode in zip(nomi, voti, lodi):
    suffisso: str = " e lode" if lode else ""
    print(f"    {nome}: {voto}{suffisso}")

# zip si ferma alla lista piu' corta
corta: list[int] = [1, 2]
lunga: list[int] = [10, 20, 30, 40]
zippati: list[tuple[int, int]] = list(zip(corta, lunga))
assert zippati == [(1, 10), (2, 20)]
print(f"\n  zip([1,2], [10,20,30,40]) = {zippati}")

# Uso di zip per creare un dizionario
registro: dict[str, int] = dict(zip(nomi, voti))
assert registro == {"Alice": 28, "Bob": 25, "Carla": 30}
print(f"  dict(zip(nomi, voti)) = {registro}")


# =============================================================================
# 4. Ciclo while
# =============================================================================
print("\n--- 4. Ciclo while ---")

# Esempio: trovare la prima potenza di 2 maggiore di 1000
potenza: int = 1
esponente: int = 0
while potenza <= 1000:
    potenza *= 2
    esponente += 1

assert potenza == 1024
assert esponente == 10
print(f"  Prima potenza di 2 > 1000: 2^{esponente} = {potenza}")

# Esempio: approssimazione di sqrt(2) con il metodo di Newton
# x_{n+1} = (x_n + 2/x_n) / 2
x: float = 1.0
iterazioni: int = 0
while abs(x * x - 2) > 1e-12:
    x = (x + 2 / x) / 2
    iterazioni += 1

assert abs(x - 2 ** 0.5) < 1e-10
print(f"  sqrt(2) ≈ {x:.15f} (dopo {iterazioni} iterazioni)")


# =============================================================================
# 5. break e continue
# =============================================================================
print("\n--- 5. break e continue ---")

# break: esce dal ciclo immediatamente
print("  Ricerca del primo multiplo di 7 > 50:")
primo_multiplo: int = 0
for n in range(1, 100):
    if n % 7 == 0 and n > 50:
        primo_multiplo = n
        break
assert primo_multiplo == 56
print(f"    Trovato: {primo_multiplo}")

# continue: salta il resto dell'iterazione corrente
print("  Numeri da 1 a 10, saltando i multipli di 3:")
non_multipli_3: list[int] = []
for n in range(1, 11):
    if n % 3 == 0:
        continue
    non_multipli_3.append(n)
assert non_multipli_3 == [1, 2, 4, 5, 7, 8, 10]
print(f"    {non_multipli_3}")

# for-else: il blocco else si esegue solo se il ciclo NON e' stato interrotto da break
print("\n  for-else: verifica se 17 e' primo:")
n_test: int = 17
is_primo: bool = True
for d in range(2, int(n_test ** 0.5) + 1):
    if n_test % d == 0:
        is_primo = False
        break
else:
    # Questo blocco si esegue solo se break NON e' stato chiamato
    pass
assert is_primo is True
print(f"    {n_test} e' primo? {is_primo}")


# =============================================================================
# 6. Pattern: accumulatore
# =============================================================================
print("\n--- 6. Pattern: accumulatore ---")

# Somma dei quadrati dei primi N numeri naturali
n_max: int = 10
somma_quadrati: int = 0
for i in range(1, n_max + 1):
    somma_quadrati += i ** 2

# Formula nota: n(n+1)(2n+1)/6
formula: int = n_max * (n_max + 1) * (2 * n_max + 1) // 6
assert somma_quadrati == formula == 385
print(f"  Somma dei quadrati 1..{n_max}: {somma_quadrati}")
print(f"  Verifica con formula: {formula}")

# Accumulatore con prodotto (fattoriale)
n_fatt: int = 6
prodotto: int = 1
for i in range(1, n_fatt + 1):
    prodotto *= i
assert prodotto == 720
print(f"  {n_fatt}! = {prodotto}")


# =============================================================================
# 7. Pattern: contatore
# =============================================================================
print("\n--- 7. Pattern: contatore ---")

# Contare quanti studenti hanno superato l'esame
voti_classe: list[int] = [28, 15, 22, 30, 17, 25, 10, 19, 30, 24]
promossi: int = 0
bocciati: int = 0
for voto in voti_classe:
    if voto >= 18:
        promossi += 1
    else:
        bocciati += 1

assert promossi == 7
assert bocciati == 3
assert promossi + bocciati == len(voti_classe)
print(f"  Voti: {voti_classe}")
print(f"  Promossi: {promossi}, Bocciati: {bocciati}")


# =============================================================================
# 8. Pattern: filtro
# =============================================================================
print("\n--- 8. Pattern: filtro ---")

# Filtrare solo i voti sufficienti
voti_sufficienti: list[int] = []
for voto in voti_classe:
    if voto >= 18:
        voti_sufficienti.append(voto)

assert voti_sufficienti == [28, 22, 30, 25, 19, 30, 24]
print(f"  Voti sufficienti: {voti_sufficienti}")

# Filtrare i numeri pari da una lista
numeri: list[int] = list(range(1, 16))
pari: list[int] = []
for n in numeri:
    if n % 2 == 0:
        pari.append(n)
assert pari == [2, 4, 6, 8, 10, 12, 14]
print(f"  Pari in 1..15: {pari}")


# =============================================================================
# 9. Pattern: ricerca
# =============================================================================
print("\n--- 9. Pattern: ricerca ---")

# Ricerca del voto massimo (senza usare max())
voti_esame: list[int] = [22, 28, 19, 30, 25, 17, 30, 24]
voto_max: int = voti_esame[0]
posizione_max: int = 0
for i, voto in enumerate(voti_esame):
    if voto > voto_max:
        voto_max = voto
        posizione_max = i

assert voto_max == 30
assert posizione_max == 3  # Prima occorrenza di 30
print(f"  Voti: {voti_esame}")
print(f"  Voto massimo: {voto_max} alla posizione {posizione_max}")


# =============================================================================
# 10. Cicli annidati
# =============================================================================
print("\n--- 10. Cicli annidati ---")

# Tavola pitagorica 5x5
print("  Tavola pitagorica 5x5:")
print("     ", end="")
for j in range(1, 6):
    print(f"{j:>4}", end="")
print()
print("    " + "-" * 20)

for i in range(1, 6):
    print(f"  {i:>2}|", end="")
    for j in range(1, 6):
        print(f"{i * j:>4}", end="")
    print()

# Generazione di coppie (combinazioni)
elementi: list[str] = ["A", "B", "C", "D"]
coppie: list[tuple[str, str]] = []
for i in range(len(elementi)):
    for j in range(i + 1, len(elementi)):
        coppie.append((elementi[i], elementi[j]))

assert len(coppie) == 6  # C(4,2) = 6
assert coppie == [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("B", "D"), ("C", "D")]
print(f"\n  Coppie da {elementi}: {coppie}")


print("\nTutti gli assert passati — esempi T09 completati con successo!")
