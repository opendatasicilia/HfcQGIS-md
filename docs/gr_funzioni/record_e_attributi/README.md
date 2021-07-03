# Record ed attributi

Questo gruppo contiene funzioni e/o espressioni che agiscono sui record o attributi. Es.: $id; get_feature().

| Funzione  | Descrizione|
|:----------:|:-----------|
|[\$currentfeature]($currentfeature.html)|Restituisce l'elemento corrente corrente da valutare. Questo può essere usato con la funzione 'attribute' per valutare i valori dell'attributo dall'elemento corrente|
|[\$id]($id.html)|Restituisce l'id geometria della riga corrente|
|[\$map]($map.html)|Restituisce l'id della voce della mappa corrente se la mappa viene disegnata in una composizione, o "tela" se la mappa viene disegnata all'interno della finestra principale di QGIS|
|[attribute](attribute.html)|Restituisce il valore di un attributo specificato da una geometria|
|[get_feature](get_feature.html)|Restituisce la prima geometria di un vettore che corrisponde a un determinato valore di attributo|
|[get_feature_by_id](get_feature_by_id.html)|	Restituisce l'id dell'elemento della riga corrente|
|[is_selected](is_selected.html)|	Indica se una geometria è selezionata. Se chiamata senza parametri, controlla la geometria corrente|
|[num_selected](num_selected.html)|Restituisce il numero di geometrie selezionate in un vettore dato. Per impostazione predefinita funziona sul vettore sul quale l'espressione è valutata|
|[represent_value](represent_value.html)|	Restituisce il valore di rappresentazione configurato per un valore di campo. Dipende dal tipo di widget configurato. Spesso, questo è utile per i widget di 'Value Map'|
|[uuid](uuid.html)|Genera un Identificatore Universale Unico (UUID) per ogni riga usando il metodo Qt QUuid::createUuid. Aggiornato a QGIS 3.18|

![](../../img/record_e_attributi/gruppo_record_e_attributi1.png)
