# Errori comuni — F16: Programmazione a oggetti

Gli errori più frequenti commessi dagli studenti sugli argomenti della lezione F16.
Ogni errore include il codice sbagliato, la spiegazione e la correzione.

---

### Errore 1: Dimenticare `self` nei metodi della classe

**Codice errato:**
```python
class Studente:
    def __init__(nome, cognome, matricola):
        nome = nome
        cognome = cognome
        matricola = matricola

    def presentati():
        return f"Sono {nome} {cognome}"

s = Studente("Luca", "Rossi", "MAT001")
```

**Cosa succede:**
```
TypeError: Studente.__init__() takes 3 positional arguments but 4 were given
```

**Perché è sbagliato:** Ogni metodo di una classe riceve automaticamente l'istanza come primo argomento, che per convenzione si chiama `self`. Senza `self`, Python non sa dove salvare gli attributi dell'oggetto. Inoltre, `nome = nome` senza `self.` assegna il parametro a se stesso (una variabile locale), senza salvare nulla nell'istanza.

**Codice corretto:**
```python
class Studente:
    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola

    def presentati(self):
        return f"Sono {self.nome} {self.cognome}"

s = Studente("Luca", "Rossi", "MAT001")
print(s.presentati())  # Sono Luca Rossi
```

**Regola da ricordare:** Ogni metodo di una classe deve avere `self` come primo parametro, e gli attributi dell'oggetto vanno assegnati con `self.attributo`.

---

### Errore 2: Attributo di classe mutabile condiviso tra istanze

**Codice errato:**
```python
class Corso:
    iscritti = []  # attributo di classe (condiviso!)

    def __init__(self, nome):
        self.nome = nome

    def iscrivi(self, studente):
        self.iscritti.append(studente)

statistica = Corso("Statistica")
informatica = Corso("Informatica")

statistica.iscrivi("Luca")
informatica.iscrivi("Anna")

print(f"Iscritti a Informatica: {informatica.iscritti}")
```

**Cosa succede:**
```
Iscritti a Informatica: ['Luca', 'Anna']
```
Luca compare anche tra gli iscritti a Informatica, anche se è stato iscritto solo a Statistica.

**Perché è sbagliato:** `iscritti = []` è un attributo di classe, condiviso tra tutte le istanze. Tutte le istanze di `Corso` puntano alla stessa lista. Quando si modifica la lista tramite un'istanza, la modifica è visibile da tutte le altre. Gli attributi mutabili (liste, dizionari, set) devono essere creati nel `__init__`.

**Codice corretto:**
```python
class Corso:
    def __init__(self, nome):
        self.nome = nome
        self.iscritti = []  # attributo di istanza (separato per ogni oggetto)

    def iscrivi(self, studente):
        self.iscritti.append(studente)

statistica = Corso("Statistica")
informatica = Corso("Informatica")

statistica.iscrivi("Luca")
informatica.iscrivi("Anna")

print(f"Iscritti a Informatica: {informatica.iscritti}")  # ['Anna']
```

**Regola da ricordare:** Non usare mai liste, dizionari o altri oggetti mutabili come attributi di classe: creali dentro `__init__` con `self.` per avere una copia separata per ogni istanza.

---

### Errore 3: `__init__` che restituisce un valore

**Codice errato:**
```python
class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
        return base * altezza  # lo studente vuole calcolare l'area

r = Rettangolo(5, 3)
```

**Cosa succede:**
```
TypeError: __init__() should return None, not 'int'
```

**Perché è sbagliato:** Il metodo `__init__` serve solo a inizializzare l'oggetto, impostando i suoi attributi. Non può restituire valori con `return`. Python crea l'oggetto internamente e `__init__` lo configura: il risultato di `Rettangolo(5, 3)` è sempre l'oggetto creato, non un valore di ritorno.

**Codice corretto:**
```python
class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

r = Rettangolo(5, 3)
print(r.area())  # 15
```

**Regola da ricordare:** Il metodo `__init__` non deve mai contenere `return valore`: serve solo a impostare gli attributi con `self.`, non a restituire risultati.

---

### Errore 4: Dimenticare `super().__init__()` nelle sottoclassi

**Codice errato:**
```python
class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

class Studente(Persona):
    def __init__(self, nome, età, matricola):
        # manca super().__init__(nome, età)
        self.matricola = matricola

s = Studente("Luca", 21, "MAT001")
print(s.nome)
```

**Cosa succede:**
```
AttributeError: 'Studente' object has no attribute 'nome'
```

**Perché è sbagliato:** Quando una sottoclasse definisce il proprio `__init__`, sovrascrive quello della classe genitore. Se non si chiama `super().__init__(...)`, gli attributi definiti nel `__init__` del genitore (`nome`, `età`) non vengono mai creati. L'oggetto `Studente` avrà solo l'attributo `matricola`.

**Codice corretto:**
```python
class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

class Studente(Persona):
    def __init__(self, nome, età, matricola):
        super().__init__(nome, età)  # inizializza gli attributi del genitore
        self.matricola = matricola

s = Studente("Luca", 21, "MAT001")
print(s.nome)       # Luca
print(s.matricola)  # MAT001
```

**Regola da ricordare:** Quando una sottoclasse ha il proprio `__init__`, chiama sempre `super().__init__(...)` per inizializzare gli attributi ereditati dalla classe genitore.

---

### Errore 5: Confondere metodo e attributo (parentesi mancanti o in eccesso)

**Codice errato:**
```python
class Cerchio:
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return 3.14159 * self.raggio ** 2

c = Cerchio(5)
print(c.area)       # dimentica le parentesi
print(c.raggio())   # aggiunge parentesi a un attributo
```

**Cosa succede:**
```
<bound method Cerchio.area of <__main__.Cerchio object at 0x...>>
TypeError: 'int' object is not callable
```
`c.area` senza parentesi restituisce il riferimento al metodo, non il risultato. `c.raggio()` con le parentesi cerca di "chiamare" un intero.

**Perché è sbagliato:** I metodi sono funzioni e vanno chiamati con le parentesi `()`. Gli attributi sono valori e non vanno chiamati. Confondere i due porta a risultati inattesi o errori. `c.area` senza `()` restituisce l'oggetto metodo, non il suo risultato. `c.raggio()` tenta di invocare il numero come funzione.

**Codice corretto:**
```python
c = Cerchio(5)
print(c.area())   # 78.53975 — chiama il metodo con ()
print(c.raggio)   # 5 — accede all'attributo senza ()
```

**Regola da ricordare:** I metodi si chiamano con le parentesi `oggetto.metodo()`, gli attributi si accedono senza: `oggetto.attributo`.

---

### Errore 6: Creare un'istanza senza le parentesi

**Codice errato:**
```python
class Studente:
    def __init__(self, nome):
        self.nome = nome

    def saluta(self):
        return f"Ciao, sono {self.nome}"

s = Studente  # mancano le parentesi e l'argomento!
print(s.saluta())
```

**Cosa succede:**
```
TypeError: Studente.saluta() missing 1 required positional argument: 'self'
```

**Perché è sbagliato:** Senza parentesi, `s = Studente` assegna a `s` la classe stessa, non un'istanza della classe. `s` diventa un alias per la classe `Studente`. Quando si chiama `s.saluta()`, Python lo interpreta come una chiamata al metodo sulla classe (non su un'istanza), e non sa quale `self` usare.

**Codice corretto:**
```python
class Studente:
    def __init__(self, nome):
        self.nome = nome

    def saluta(self):
        return f"Ciao, sono {self.nome}"

s = Studente("Luca")  # crea un'istanza con le parentesi
print(s.saluta())     # Ciao, sono Luca
```

**Regola da ricordare:** Per creare un oggetto scrivi `variabile = NomeClasse(argomenti)` con le parentesi: senza parentesi, ottieni la classe, non un'istanza.

---
