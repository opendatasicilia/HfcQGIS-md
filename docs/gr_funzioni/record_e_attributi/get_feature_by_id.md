# get_feature_by_id

Restituisce l'id dell'elemento della riga corrente.

## Sintassi

* get_feature_by_id(*<span style="color:red;">layer</span>, <span style="color:red;">feature_id</span>*)

## Argomenti

* *<span style="color:red;">layer</span>* layer, nome del layer o id del layer
* *<span style="color:red;">feature_id</span>* L'id dell'elemento che deve essere restituito (inizia da 0 per gli shapefile)

## Esempi

* `et_feature_by_id('streets', 1) → l'elemento con id 1 nel vettore "streets"`


![](/img/record_e_attributi/get_feature_by_id1.png)
