# regexp_substr

Restituisce la porzione di una stringa che soddisfa l'espressione regolare passata.

## Sintassi

regexp_substr(_<span style="color:red;">input_string</span>, <span style="color:red;">regex</span>_)

## Argomenti

* _<span style="color:red;">input_string</span>_ la stringa in cui cercare
* _<span style="color:red;">regex</span>_ L'espressione regolare da contro abbinare. I caratteri backslash devono essere "double escaped" ( es `"\\s"` per selezionare un carattere spazio).

## Esempi

* `regexp_substr('abc123','(\\d+)') → '123'`

![](/img/stringhe_di_testo/regexp_substr/regexp_substr1.png)

## nota bene

--

## osservazioni

--
