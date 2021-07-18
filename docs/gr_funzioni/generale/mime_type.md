# mime_type

Restituisce il tipo mime dei dati binari.

## Sintassi

* mime_type(_<span style="color:red;">bytes</span>_)

## Argomento

* _<span style="color:red;">bytes</span>_ I dati binari

## Esempi

* `mime_type('<html><body></body></html>') → text/html`
* `mime_type(from_base64('R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAIAOw==')) → image/gif`

![](../../img/generale/mime_type1.png)
