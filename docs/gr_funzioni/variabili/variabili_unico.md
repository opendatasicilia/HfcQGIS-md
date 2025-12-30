---
social_image: img/card_social/hfc_gr_variabili.png
---

# Variabili

Questo gruppo contiene variabili dinamiche relative all'applicazione, al file di progetto e ad altre impostazioni. Le variabili possono essere utilizzate nelle espressioni precedute dal carattere `@`.

---

## atlas_feature

Restituisce l'elemento corrente dell'atlante come oggetto feature.

### Sintassi

```
@atlas_feature
```

### Argomenti

Nessun argomento richiesto.

### Esempi

```py
-- Accede all'elemento corrente dell'atlante
@atlas_feature

-- Ottiene un attributo dell'elemento atlante corrente
attribute(@atlas_feature, 'nome_campo')
```

### Note

* Disponibile solo nel contesto di un atlante di stampa
* Restituisce l'intera feature con geometria e attributi
* Utile per accedere agli attributi dell'elemento corrente dell'atlante in layout di stampa

### Osservazioni

La variabile `@atlas_feature` è particolarmente utile quando si lavora con gli atlanti nei layout di stampa di QGIS. Permette di riferirsi dinamicamente all'elemento corrente che viene iterato dall'atlante.

**Esempio pratico**: In un atlante che stampa una mappa per ogni comune, `@atlas_feature` rappresenta il comune corrente ad ogni iterazione.

---

## row_number

Memorizza il numero della riga corrente.

### Sintassi

```
@row_number
```

### Argomenti

Nessun argomento richiesto.

### Esempi

```py
-- Restituisce il numero della riga corrente
@row_number

-- Uso in una condizione
if(@row_number = 1, 'Prima riga', 'Altra riga')

-- Numerazione progressiva delle feature
@row_number
```

### Note

* Disponibile in: calcolatore di campi, tabella attributi, moduli
* Il conteggio parte sempre da **1** (non da 0)
* Molto utile per creare numerazioni progressive
* A differenza di `$id`, `@row_number` parte sempre da 1 indipendentemente dal tipo di layer

### Osservazioni

La variabile `@row_number` è particolarmente utile quando si ha bisogno di un contatore affidabile che parte sempre da 1, indipendentemente dal formato del layer (shapefile, geopackage, etc.).

**Differenza con $id**:
- `$id`: può partire da 0 (shapefile) o da 1 (altri formati)
- `@row_number`: parte sempre da 1

**Esempio pratico**: Creare un campo con numerazione progressiva partendo sempre da 1:

```py
@row_number
```

Se hai 100 feature, genererà numeri da 1 a 100, indipendentemente da come sono numerati gli ID originali.

---

## parent

Si riferisce all'elemento padre corrente in una relazione uno-a-molti.

### Sintassi

```
@parent
```

### Argomenti

Nessun argomento richiesto.

### Esempi

```py
-- Accede all'elemento padre nella relazione
@parent

-- Ottiene un attributo dell'elemento padre
attribute(@parent, 'nome_campo')

-- Confronta un valore con quello del padre
"campo_figlio" = attribute(@parent, 'campo_padre')
```

### Note

* Disponibile solo nel contesto di una relazione uno-a-molti
* Utilizzabile nei moduli incorporati (embedded forms)
* Permette di accedere ai dati del layer padre dal layer figlio
* Fondamentale per implementare filtri e vincoli nelle relazioni

### Osservazioni

La variabile `@parent` è essenziale quando si lavora con **relazioni tra layer** in QGIS. Permette al layer figlio di accedere agli attributi del layer padre.

**Contesti di utilizzo**:

1. **Moduli incorporati**: Quando si visualizza un form del layer figlio all'interno del form del layer padre
2. **Widget relazione**: Per filtrare o vincolare i dati del layer figlio
3. **Espressioni di validazione**: Per verificare che i dati del figlio siano coerenti con il padre

**Esempio pratico** - Relazione Comuni-Edifici:

```py
-- Nel layer Edifici, filtra solo gli edifici del comune corrente
attribute(@parent, 'cod_comune') = "cod_comune"
```

Se si è nel form di un Comune specifico, il widget relazione mostrerà solo gli edifici appartenenti a quel comune.

**Altro esempio** - Calcolo automatico basato sul padre:

```py
-- Imposta automaticamente il nome del comune nell'edificio
attribute(@parent, 'nome_comune')
```

### Vedi anche

* [current_parent_feature](current_parent_feature.md) - Rappresenta la feature corrente nel form padre
* [current_parent_geometry](current_parent_geometry.md) - Geometria della feature nel form padre

---

## Collegamenti utili

* [Documentazione ufficiale QGIS sulle variabili](https://docs.qgis.org/3.40/en/docs/user_manual/expressions/functions_list.html#variables)
* [Video di Nyall Dawson sulle variabili](https://www.youtube.com/watch?v=h-mpUkwDdOQ)
