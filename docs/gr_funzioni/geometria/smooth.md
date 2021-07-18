# smooth

Smussa una geometria con l'aggiunta di ulteriori nodi che arrotondano gli angoli nella geometria.

## Sintassi

- smooth( _<span style="color:red;">geometry</span>_,  _<span style="color:red;">iterations=1</span>_,  _<span style="color:red;">offset=0.25</span>_,  _<span style="color:red;">min_length=1</span>_,  _<span style="color:red;">max_angle=180</span>_)

## Argomenti

*  _<span style="color:red;">geometry</span>_ una geometria
*  _<span style="color:red;">iterations</span>_ Numero di iterazioni di smussatura da applicare. Valori più alti fanno risultare geometria più morbide, ma più complesse.
*  _<span style="color:red;">offset</span>_ valore tra 0 e 0.5 che controlla quanto la geometria smussata segua strettamente la geometria originale. Valori più piccoli risultano in una lisciatura più stretta, valori più grandi risultano in una lisciatura più larga.
*  _<span style="color:red;">min_length</span>_ lunghezza minima dei segmenti ai quali applicare la smussatura. Questo parametro può essere usato per evitare di posizionare nodi aggiuntivi eccessivi nei segmenti più corti della geometria.
*  _<span style="color:red;">max_angle</span>_ angolo massimo (0-180) da applicare al nodo per la smussatura. Abbassando intenzionalmente l'angolo massimo si abbassa l'arrotondamento sugli angoli della geometria. Per esempio, un valore di 80 gradi preserverà l'angolo nella geometria.

## Esempi

![](../../img/geometria/smooth/smooth1.png)

## nota bene

--

## osservazioni

--
