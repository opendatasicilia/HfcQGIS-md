# line_substring

Restituisce la porzione di una geometria di linea (o curva) che rientra tra le distanze iniziale e finale specificate (misurata dall'inizio della linea). I valori Z e M sono linearmente interpolati dai valori esistenti.

## Sintassi

line_substring(_<span style="color:red;">geometry</span>,<span style="color:red;">start_distance</span>,<span style="color:red;">end_distance</span>_)

## Argomenti

* _<span style="color:red;">geometry</span>_ una geometria lineare o curva
* _<span style="color:red;">start_distance</span>_ distanza all'inizio della sottostringa
* _<span style="color:red;">end_distance</span>_ distanza alla fine della sottostringa

## Esempi

* `geom_to_wkt(line_substring(geometry:=geom_from_wkt('LineString(0 0, 10 0)'),start_distance:=2,end_distance:=6)) → 'LineString (2 0,6 0)'`
* `line_substring( $geometry,  $length *.1,$length *.6) → <geometria: LineString>`

![](../../img/geometria/line_substring/line_substring1.png)

## nota bene

--

## osservazioni

--

Funzione utile per la tematizzazione

![](../../img/geometria/line_substring/line_substring2.png)
