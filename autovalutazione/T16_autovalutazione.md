# Autovalutazione — T16: Classi e Programmazione a Oggetti

Metti alla prova la tua comprensione! Per ogni esercizio, prova a rispondere **prima** di guardare la soluzione.

---

## Cosa stampa questo codice?

### Esercizio 1

```python
class Studente:
    universita = "La Sapienza"  # attributo di classe

    def __init__(self, nome, matricola):
        self.nome = nome          # attributo di istanza
        self.matricola = matricola

s1 = Studente("Alice", 12345)
s2 = Studente("Bob", 67890)

print(s1.universita)
print(s2.universita)

Studente.universita = "Tor Vergata"
print(s1.universita)
print(s2.universita)
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
La Sapienza
La Sapienza
Tor Vergata
Tor Vergata
```

**Spiegazione:** `universita` e' un **attributo di classe**, condiviso da tutte le istanze. Quando lo modifichiamo tramite `Studente.universita`, il cambiamento e' visibile da tutte le istanze. Questo accade perche' `s1.universita` e `s2.universita` non trovano un attributo di istanza con quel nome, quindi risalgono all'attributo di classe.
</details>

---

### Esercizio 2

```python
class Contatore:
    conteggio = 0

    def __init__(self):
        Contatore.conteggio += 1

    def quanti(self):
        return Contatore.conteggio

c1 = Contatore()
c2 = Contatore()
c3 = Contatore()
print(c1.quanti())
print(c2.quanti())
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
3
3
```

**Spiegazione:** Ogni volta che viene creata un'istanza, `__init__` incrementa l'attributo di classe `conteggio`. Dopo tre istanze, `conteggio` vale `3`. Il metodo `quanti()` restituisce il valore dell'attributo di classe, che e' lo stesso per tutte le istanze. Sia `c1.quanti()` che `c2.quanti()` restituiscono `3`.
</details>

---

### Esercizio 3

```python
class Animale:
    def __init__(self, nome):
        self.nome = nome

    def parla(self):
        return f"{self.nome} fa un suono generico"

class Cane(Animale):
    def parla(self):
        return f"{self.nome} fa: Bau!"

class Gatto(Animale):
    def parla(self):
        return f"{self.nome} fa: Miao!"

animali = [Cane("Fido"), Gatto("Micio"), Animale("Creatura")]
for a in animali:
    print(a.parla())
```

<details>
<summary>Mostra la risposta</summary>

**Output:**
```
Fido fa: Bau!
Micio fa: Miao!
Creatura fa un suono generico
```

**Spiegazione:** Questo e' un esempio di **ereditarieta'** e **polimorfismo**. `Cane` e `Gatto` ereditano da `Animale` e sovrascrivono il metodo `parla()`. Quando chiamiamo `a.parla()`, Python usa il metodo della classe specifica dell'oggetto. `Cane` usa il suo `parla()`, `Gatto` usa il suo, e `Animale` usa quello generico. Tutti e tre condividono l'`__init__` della classe base.
</details>

---

## Trova l'errore

### Esercizio 4

```python
class Rettangolo:
    def __init__(self, base, altezza):
        base = base
        altezza = altezza

    def area(self):
        return self.base * self.altezza

r = Rettangolo(5, 3)
print(r.area())
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `AttributeError: 'Rettangolo' object has no attribute 'base'`

**Problema:** Nell'`__init__`, manca `self.` davanti agli attributi. `base = base` crea una variabile locale che viene scartata alla fine del metodo, invece di salvare il valore nell'istanza.

**Correzione:**
```python
class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base       # self. salva nell'istanza
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

r = Rettangolo(5, 3)
print(r.area())  # 15
```

**Lezione:** Dentro `__init__`, usate sempre `self.nome_attributo = valore` per salvare i dati nell'istanza. Senza `self.`, i valori sono solo variabili locali temporanee.
</details>

---

### Esercizio 5

```python
class Squadra:
    giocatori = []  # attributo di classe

    def __init__(self, nome):
        self.nome = nome

    def aggiungi(self, giocatore):
        self.giocatori.append(giocatore)

roma = Squadra("Roma")
lazio = Squadra("Lazio")
roma.aggiungi("Totti")
lazio.aggiungi("Immobile")

print(f"Roma: {roma.giocatori}")
print(f"Lazio: {lazio.giocatori}")
```

<details>
<summary>Mostra la risposta</summary>

**Output indesiderato:**
```
Roma: ['Totti', 'Immobile']
Lazio: ['Totti', 'Immobile']
```

**Problema:** `giocatori = []` e' un **attributo di classe mutabile**. La lista e' condivisa tra tutte le istanze. Quando `roma.aggiungi("Totti")` fa `append`, modifica la stessa lista visibile anche da `lazio`.

**Correzione:**
```python
class Squadra:
    def __init__(self, nome):
        self.nome = nome
        self.giocatori = []  # attributo di istanza: ogni squadra ha la sua lista

    def aggiungi(self, giocatore):
        self.giocatori.append(giocatore)

roma = Squadra("Roma")
lazio = Squadra("Lazio")
roma.aggiungi("Totti")
lazio.aggiungi("Immobile")

print(f"Roma: {roma.giocatori}")   # Roma: ['Totti']
print(f"Lazio: {lazio.giocatori}") # Lazio: ['Immobile']
```

**Lezione:** Non usate attributi di classe **mutabili** (liste, dizionari) se ogni istanza deve avere la propria copia. Inizializzateli dentro `__init__` con `self.`.
</details>

---

### Esercizio 6

```python
class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio
        return self.raggio * 3.14159

c = Cerchio(5)
```

<details>
<summary>Mostra la risposta</summary>

**Errore:** `TypeError: __init__() should return None, not 'float'`

**Problema:** Il metodo `__init__` **non deve restituire un valore**. Il suo compito e' solo inizializzare l'oggetto, non restituire risultati. Python lo chiama automaticamente dopo la creazione dell'oggetto.

**Correzione:**
```python
class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio

    def circonferenza(self):
        return 2 * 3.14159 * self.raggio

    def area(self):
        return 3.14159 * self.raggio ** 2

c = Cerchio(5)
print(c.area())           # 78.53975
print(c.circonferenza())  # 31.4159
```

**Lezione:** `__init__` serve solo per inizializzare gli attributi. I calcoli vanno in metodi separati che restituiscono i risultati.
</details>

---

## Completa il codice

### Esercizio 7

Completa la classe `Studente` con `__init__`, un metodo per aggiungere voti e uno per calcolare la media.

```python
class Studente:
    # --- COMPLETA: __init__ con nome e lista voti vuota ---

    def aggiungi_voto(self, voto):
        """Aggiunge un voto se e' valido (tra 18 e 30)."""
        # --- COMPLETA ---
        pass

    def media(self):
        """Restituisce la media dei voti, o None se non ci sono voti."""
        # --- COMPLETA ---
        pass

    def __str__(self):
        """Rappresentazione leggibile dello studente."""
        # --- COMPLETA: restituisci una stringa tipo "Alice - Media: 27.5" ---
        pass

# Test
s = Studente("Alice")
s.aggiungi_voto(28)
s.aggiungi_voto(30)
s.aggiungi_voto(15)  # Non valido, deve essere ignorato
s.aggiungi_voto(26)
print(s)           # Alice - Media: 28.0
print(s.media())   # 28.0
```

<details>
<summary>Mostra la soluzione</summary>

```python
class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = []

    def aggiungi_voto(self, voto):
        """Aggiunge un voto se e' valido (tra 18 e 30)."""
        if 18 <= voto <= 30:
            self.voti.append(voto)

    def media(self):
        """Restituisce la media dei voti, o None se non ci sono voti."""
        if not self.voti:
            return None
        return sum(self.voti) / len(self.voti)

    def __str__(self):
        """Rappresentazione leggibile dello studente."""
        m = self.media()
        if m is None:
            return f"{self.nome} - Nessun voto"
        return f"{self.nome} - Media: {m}"

s = Studente("Alice")
s.aggiungi_voto(28)
s.aggiungi_voto(30)
s.aggiungi_voto(15)  # Ignorato
s.aggiungi_voto(26)
print(s)           # Alice - Media: 28.0
print(s.media())   # 28.0
```

**Spiegazione:** La lista `voti` e' inizializzata in `__init__` come attributo di istanza. `aggiungi_voto` valida il voto prima di aggiungerlo. `media` gestisce il caso di lista vuota restituendo `None`. `__str__` viene chiamato automaticamente da `print()`.
</details>

---

### Esercizio 8

Completa le classi usando l'ereditarieta'.

```python
class Forma:
    def __init__(self, colore):
        self.colore = colore

    def area(self):
        raise NotImplementedError("Le sottoclassi devono implementare area()")

    def descrizione(self):
        return f"Forma {self.colore} con area {self.area():.2f}"


class Quadrato(Forma):
    # --- COMPLETA: __init__ e area ---
    pass


class CerchioColorato(Forma):
    # --- COMPLETA: __init__ e area ---
    pass


# Test
q = Quadrato("rosso", 4)
c = CerchioColorato("blu", 3)
print(q.descrizione())  # Forma rosso con area 16.00
print(c.descrizione())  # Forma blu con area 28.27
```

<details>
<summary>Mostra la soluzione</summary>

```python
import math

class Forma:
    def __init__(self, colore):
        self.colore = colore

    def area(self):
        raise NotImplementedError("Le sottoclassi devono implementare area()")

    def descrizione(self):
        return f"Forma {self.colore} con area {self.area():.2f}"


class Quadrato(Forma):
    def __init__(self, colore, lato):
        super().__init__(colore)
        self.lato = lato

    def area(self):
        return self.lato ** 2


class CerchioColorato(Forma):
    def __init__(self, colore, raggio):
        super().__init__(colore)
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2


q = Quadrato("rosso", 4)
c = CerchioColorato("blu", 3)
print(q.descrizione())  # Forma rosso con area 16.00
print(c.descrizione())  # Forma blu con area 28.27
```

**Spiegazione:** `super().__init__(colore)` chiama l'`__init__` della classe base `Forma` per inizializzare `self.colore`. Ogni sottoclasse aggiunge i propri attributi specifici (`lato` o `raggio`) e implementa il metodo `area()`. Il metodo `descrizione()` ereditato da `Forma` funziona correttamente perche' chiama `self.area()`, che grazie al polimorfismo usa la versione della sottoclasse.
</details>
