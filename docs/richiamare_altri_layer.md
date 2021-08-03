# Richiamare altri layer

Il **field Calc** o il **costruttore di espressioni** è sempre relativo ad un layer, ovvero, il calcolatore di campi è avviabile solo dopo aver selezionato un layer dalla TOC. Questo significa che tutte le funzioni e/o espressioni fanno riferimento al relativo layer corrente. Esistono delle funzioni che permettono di _richiamare_ layer diversi dal layer corrente, questo permette di lavorare anche con attributi che non sono del layer corrente.

Le funzioni che permettono di richiamare in modo diretto (è un argomento della funzione) altri layer sono:

nro| funzione          | descrizione            | sintassi
---|-------------------|------------------------|------------
1  | [get_feature](./gr_funzioni/record_e_attributi/record_e_attributi_unico.md#get_feature)       | Restituisce il primo elemento di un layer che corrisponde ad un dato valore di attributo. | get_feature(_<span style="color:red;">layer</span>_,attribute,value)
2  | [get_feature_by_id](./gr_funzioni/record_e_attributi/record_e_attributi_unico.md#get_feature_by_id) | Restituisce l'elemento con un id su un layer.| get_feature_by_id(_<span style="color:red;">layer</span>_,feature_id)
3  | [aggregate](./gr_funzioni/aggrega/aggrega_unico.md#aggregate)         | Restituisce un valore aggregato calcolato usando elementi da un altro vettore.| aggregate(_<span style="color:red;">layer</span>_,aggregate,expression[,filter][,concatenator=''][,order_by])
4  | [relation_aggregate](./gr_funzioni/aggrega/aggrega_unico.md#relation_aggregate)| Restituisce un valore aggregato calcolato usando tutte gli elementi figli corrispondenti da una relazione di layer.| relation_aggregate(_<span style="color:red;">relation</span>_,aggregate,expression[,concatenator=''][,order_by])
5  | [overlay_contains](./gr_funzioni/geometria/geometria_unico.md#overlay_contains)  |Restituisce se l'elemento corrente contiene spazialmente almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target contenuti nell'elemento corrente.|overlay_contains(_<span style="color:red;">layer</span>_[,expression][,filter][,limit][,cache=false])
6  | [overlay_crosses](./gr_funzioni/geometria/geometria_unico.md#overlay_crosses)   |Restituisce se l'elemento corrente attraversa spazialmente almeno un elemento di un layer target o un array di risultati basati su espressioni per gli elementi nel layer target attraversati dall'elemento corrente.|overlay_crosses(_<span style="color:red;">layer</span>_[,expression][,filter][,limit][,cache=false])
7  | [overlay_disjoint](./gr_funzioni/geometria/geometria_unico.md#overlay_disjoint)  |Restituisce se l'elemento corrente è spazialmente disgiunto da tutti gli elementi di un layer target, o un array di risultati basati su espressione per gli elementi nel layer target che sono disgiunti dall'elemento corrente.|overlay_disjoint(_<span style="color:red;">layer</span>_[,expression][,filter][,limit][,cache=false])
8  | [overlay_equals](./gr_funzioni/geometria/geometria_unico.md#overlay_equals)    |Restituisce se l'elemento corrente è spazialmente uguale ad almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target che sono spazialmente uguali all'elemento corrente.|overlay_equals(_<span style="color:red;">layer</span>_[,expression][,filter][,limit][,cache=false])
9  | [overlay_intersects](./gr_funzioni/geometria/geometria_unico.md#overlay_intersects)|Restituisce se l'elemento corrente interseca spazialmente almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target intersecati dall'elemento corrente.|overlay_intersects(_<span style="color:red;">layer</span>_[,expression][,filter][,limit][,cache=false])
10  | [overlay_nearest](./gr_funzioni/geometria/geometria_unico.md#overlay_nearest)  |Restituisce se l'elemento corrente ha elementi da un layer target entro una data distanza o un array di risultati basati su espressioni per gli elementi nel layer di target entro una distanza dall'elemento corrente. Nota: questa funzione può essere lenta e consuma molta memoria per layer con molte feature.|overlay_nearest(_<span style="color:red;">layer</span>_[,expression][,filter][,limit=1][,max_distance][,cache=false])
11  | [overlay_touches](./gr_funzioni/geometria/geometria_unico.md#overlay_touches) |Restituisce se l'elemento corrente tocca spazialmente almeno un elemento da un layer target o un array di risultati basati su espressioni per gli elementi nel layer target toccati dall'elemento corrente.|overlay_touches(_<span style="color:red;">layer</span>_[,expression][,filter][,limit][,cache=false])
12  | [overlay_within](./gr_funzioni/geometria/geometria_unico.md#overlay_within)   |Restituisce se l'elemento corrente è spazialmente all'interno di almeno un elemento da layer destinazione, o un array di risultati basati su espressione per gli elementi nel layer destinazione che contengono l'elemento corrente.|overlay_within(_<span style="color:red;">layer</span>_[,expression][,filter][,limit][,cache=false])

## Esempi

### JOIN al volo

Realizzare una join tabellare al volo, cioè usando solo le espressioni:

```
attribute(
get_feature (
layer:='pop_res_regioni_ISTAT20190101',
attribute:='cod_ISTAT',
value:= attribute($currentfeature , 'cod_reg')),
'pop_res2019')
```

dove:

- `pop_res_regioni_ISTAT20190101` nome del layer 'sinistro` che contiene il dato da visualizzare/usare;
- `cod_ISTAT` nome dell'attributo (pop_res_regioni_ISTAT20190101) da correlare con il layer di `destra`;
- `cod_reg` nome dell'attributo del layer di `destra` da correlare con `cod_ISTAT`del layer di sinistra;
- `pop_res2019` attributo del layer di `sinistra` da usare/visualizzare

### Relazione al volo

```
aggregate( 
layer:='Reg01012021_WGS84',
aggregate:='count',
expression:= "den_reg",
filter:= "cod_rip" = attribute(@parent,'cod_rip'))
```

dove:

- `Reg01012021_WGS84` nome del layer figlio;
- `den_reg` nome attributo da conteggiare;
- `cod_rip` attributo del layer figlio (Reg01012021_WGS84) da correlare;
- `cod_rip` nome attributo layer padre


### Geometria più vicina

Layer corrente nel filed calc è `punti`, richiamo la geometria più vicona di un altro layer `strade_palermo`:

```
overlay_nearest('strade_palermo',$geometry)[0]
```

vedi esempio [51](./esempi/layer_vicino.md)
