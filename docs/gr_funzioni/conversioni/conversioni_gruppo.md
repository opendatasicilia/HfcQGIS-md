# Conversioni

Questo gruppo contiene funzioni per convertire i dati da un tipo ad un'altro, es. da stringa a intero, da intero a stringa. 

| Funzione  | Descrizione| Info
|----------:|:-----------|-----
|[from_base64](from_base64.md)|Decodifica una stringa Base64 in un valore binario|>= QGIS 3.14
|[md5](md5.md)|Crea un hash md5 da una stringa.|>= QGIS 3.12
|[sha256](sha256.md)|Crea un hash sha256 da una stringa|>= QGIS 3.12
|[to_base64](to_base64.md)|Decodifica una stringa Base64 in un valore binario.|>= QGIS 3.14
|[to_date](to_date.md)|	Converte una stringa in un oggetto data|
|[to_datetime](to_datetime.md)|Converte una stringa in un oggetto datetime|
|[to_dm](to_dm.md)|Converte una coordinata in gradi, minuti| >= QGIS 3.4
|[to_dms](to_dms.md)|Converte una coordinata in gradi, minuti e secondi| >= QGIS 3.4
|[to_int](to_int.md)|Converte una stringa in un numero intero. Non viene restituito nulla se un valore non può essere convertito ad intero (es. '123asd' non è valido)|
|[to_interval](to_interval.md)|Converte una stringa in un tipo intervallo. Può essere usata per estrarre giorni, ore, mese, etc. da una data.|
|[to_real](to_real.md)|Converte una stringa in un numero reale. Non viene restituito nulla se un valore non può essere convertito a reale (es. '123.56asd' non è valido). I numeri sono arrotondati dopo aver salvato le modifiche se la precisione è minore del risultato della conversione|
|[to_string](to_string.md)|	Converte un numero in stringa|
|[to_time](to_time.md)|Converti una stringa in un oggetto time|


![](../../img/conversioni/gruppo_conversioni1.png)