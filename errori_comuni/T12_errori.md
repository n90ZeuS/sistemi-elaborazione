# Errori comuni — T12: Dizionari, set e mutabilità

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione T12.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Accesso a una chiave inesistente senza `.get()`

**Codice errato:**
```python
studente = {"nome": "Luca", "età": 21}
voto = studente["voto"]
```

**Cosa succede:**
```
KeyError: 'voto'
```

**Perché è sbagliato:** Quando si accede a una chiave che non esiste nel dizionario con la sintassi `dizionario[chiave]`, Python solleva un `KeyError`. Questo è particolarmente problematico quando si lavora con dati reali dove non tutte le chiavi sono garantite.

**Codice corretto:**
```python
studente = {"nome": "Luca", "età": 21}
voto = studente.get("voto", None)  # restituisce None se la chiave non esiste
# oppure con un valore di default:
voto = studente.get("voto", 0)
```

**Regola da ricordare:** Usa `dizionario.get(chiave, default)` quando non sei sicuro che la chiave esista, per evitare `KeyError`.

---

### Errore 2: Usare una lista come elemento di un set

**Codice errato:**
```python
insieme = {[1, 2, 3], [4, 5, 6]}
```

**Cosa succede:**
```
TypeError: unhashable type: 'list'
```

**Perché è sbagliato:** I set in Python possono contenere solo oggetti *hashable*, cioè immutabili. Le liste sono mutabili, quindi non possono essere usate come elementi di un set né come chiavi di un dizionario. Python non saprebbe come calcolare un valore hash stabile per un oggetto che può cambiare.

**Codice corretto:**
```python
# Converti le liste in tuple (immutabili)
insieme = {(1, 2, 3), (4, 5, 6)}
```

**Regola da ricordare:** Solo gli oggetti immutabili (numeri, stringhe, tuple) possono essere inseriti in un set o usati come chiavi di un dizionario.

---

### Errore 3: Assumere che un dizionario sia ordinato in senso tradizionale

**Codice errato:**
```python
voti = {"Luca": 28, "Anna": 30, "Marco": 25}
# Lo studente pensa di poter accedere al "primo" elemento con un indice
primo_voto = voti[0]
```

**Cosa succede:**
```
KeyError: 0
```

**Perché è sbagliato:** I dizionari non sono sequenze: non si accede agli elementi tramite un indice numerico, ma tramite la chiave. Da Python 3.7 i dizionari mantengono l'ordine di inserimento, ma questo non li rende indicizzabili come le liste. `voti[0]` cerca la chiave `0`, che non esiste.

**Codice corretto:**
```python
voti = {"Luca": 28, "Anna": 30, "Marco": 25}
# Accesso per chiave
voto_luca = voti["Luca"]

# Se serve il "primo" elemento inserito
prima_chiave = list(voti.keys())[0]
primo_valore = list(voti.values())[0]
```

**Regola da ricordare:** I dizionari si accedono per chiave, non per posizione numerica: usa `dizionario[chiave]`, non `dizionario[indice]`.

---

### Errore 4: Argomento default mutabile in una funzione che usa un dizionario

**Codice errato:**
```python
def aggiungi_voto(nome, voto, registro={}):
    registro[nome] = voto
    return registro

r1 = aggiungi_voto("Luca", 28)
r2 = aggiungi_voto("Anna", 30)
print(r2)
```

**Cosa succede:**
```
{'Luca': 28, 'Anna': 30}
```
Lo studente si aspettava `{'Anna': 30}`, perché pensava che `registro` fosse un dizionario vuoto ad ogni chiamata. Invece il dizionario è condiviso tra tutte le chiamate.

**Perché è sbagliato:** In Python, gli argomenti default mutabili (come `{}` o `[]`) vengono creati una sola volta quando la funzione è definita, non ad ogni chiamata. Tutte le chiamate successive condividono lo stesso oggetto.

**Codice corretto:**
```python
def aggiungi_voto(nome, voto, registro=None):
    if registro is None:
        registro = {}
    registro[nome] = voto
    return registro

r1 = aggiungi_voto("Luca", 28)
r2 = aggiungi_voto("Anna", 30)
print(r2)  # {'Anna': 30}
```

**Regola da ricordare:** Non usare mai `{}` o `[]` come valore default di un parametro: usa `None` e crea l'oggetto mutabile dentro la funzione.

---

### Errore 5: Aliasing involontario con i dizionari

**Codice errato:**
```python
originale = {"corso": "Statistica", "crediti": 6}
copia = originale  # sembra una copia, ma non lo è

copia["crediti"] = 9
print(originale["crediti"])
```

**Cosa succede:**
```
9
```
Lo studente si aspettava `6`, ma anche l'originale è stato modificato.

**Perché è sbagliato:** L'assegnamento `copia = originale` non crea un nuovo dizionario: crea un *alias*, cioè un secondo nome che punta allo stesso oggetto in memoria. Qualsiasi modifica attraverso `copia` si riflette anche su `originale`, perché sono lo stesso dizionario.

**Codice corretto:**
```python
originale = {"corso": "Statistica", "crediti": 6}
copia = originale.copy()  # crea una copia superficiale

copia["crediti"] = 9
print(originale["crediti"])  # 6 — l'originale non è toccato
```

**Regola da ricordare:** Per duplicare un dizionario usa `.copy()`; l'assegnamento `b = a` crea solo un alias, non una copia.

---

### Errore 6: Confondere `.keys()`, `.values()` e `.items()`

**Codice errato:**
```python
voti = {"Luca": 28, "Anna": 30, "Marco": 25}

# Lo studente vuole scorrere nomi e voti insieme
for elemento in voti.keys():
    print(f"{elemento[0]} ha preso {elemento[1]}")
```

**Cosa succede:**
```
L ha preso u
A ha preso n
M ha preso a
```
Python non dà errore, ma i risultati sono completamente sbagliati: `elemento` è una stringa (la chiave), e `elemento[0]` e `elemento[1]` sono i primi due caratteri della stringa.

**Perché è sbagliato:** `.keys()` restituisce solo le chiavi, `.values()` solo i valori. Per ottenere coppie (chiave, valore) bisogna usare `.items()`, che restituisce tuple `(chiave, valore)`.

**Codice corretto:**
```python
voti = {"Luca": 28, "Anna": 30, "Marco": 25}

# .items() restituisce coppie (chiave, valore)
for nome, voto in voti.items():
    print(f"{nome} ha preso {voto}")
```

**Regola da ricordare:** Usa `.items()` per iterare su coppie chiave-valore, `.keys()` per le sole chiavi e `.values()` per i soli valori.

---
