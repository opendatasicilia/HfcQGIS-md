HfcQGIS: Help funzioni calcolatore di campi di `QGIS`_ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _QGIS: https://qgis.org/it/site/

Questa guida nasce per rispondere alle numerose richieste di aiuto sull'uso del **calcolatore di campi**, a integrazione - con esempi e molti screenshot - della `guida ufficiale di QGIS`_.
    
Questo manuale
~~~~~~~~~~~~~~  
   
.. raw:: html

    <embed>
        <p>Questa versione in formato <a class="reference external" href="https://docs.readthedocs.io/en/latest/index.html" target="_blank">Read The Docs</a> del <a class="reference external" href="https://github.com/pigreco/HfcQGIS/blob/master/README.md" target="_blank">lavoro</a> di Salvatore  FIANDACA, è stata realizzata dalla comunità <a class="reference external" href="./ods.html"><strong>OpenDataSicilia</strong></a>, in  particolare da: <a class="reference external" href="https://twitter.com/aborruso" target="_blank">Andrea Borruso</a>, <a class="reference external" href="https://twitter.com/totofiandaca" target="_blank">Totò Fiandaca</a> e <a class="reference external" href="https://twitter.com/gbvitrano" target="_blank">Giovan Battista Vitrano</a>.<br>
        L'idea è stata di Giovan Battista, mentre la musa ispiratrice per la scelta di Read The Docs è <a class="reference external" href="https://twitter.com/cirospat" target="_blank">Ciro Spataro</a>.</p>
    </embed>
    

    <div style="width: 100%; height: 200px; background-color:transparent !important; margin: 0 auto; display: block;" data-wordart-src="//cdn.wordart.com/json/dc6ztvy6kv0j" data-wordart-show-attribution></div>
  
    
Contenuti:
~~~~~~~~~~

.. toctree::
  :maxdepth: 2
 
  Home <http://hfcqgis.opendatasicilia.it/it/latest/>
  
.. toctree::
   :maxdepth: 2
      
   corso_formazione/corso_di_formazione
  
.. toctree::
   :maxdepth: 2
      
   calcolatore_campi/index
   
.. toctree::
   :maxdepth: 2
   
   esempi/index
   
.. toctree::
   :maxdepth: 2
   
   mettiti_alla_prova

.. toctree::
    :maxdepth: 2
    
   release/index
   
.. toctree::
   :maxdepth: 2
     
   gr_funzioni/index
     
.. toctree::
   :maxdepth: 2
   
   contribuire
   
.. toctree::
   :maxdepth: 2
   
   supporter
   
.. toctree::
   :maxdepth: 2

   parlano_di_noi
   
.. toctree::
   :maxdepth: 2
   
   ods
   
.. toctree::
   :maxdepth: 2
   
   privacy
   
.. toctree::
  :glob:
  :includehidden: Home <http://hfcqgis.opendatasicilia.it/it/latest/>
  
Autore HfcQGIS
~~~~~~~~~~~~~~
.. raw:: html

    <embed>
        <p><a href="http://hfcqgis.opendatasicilia.it/it/latest/autore.html" target="_blank"><strong>Salvatore Fiandaca</strong></a> (aka <em>pigreco</em>)</p>
    </embed>

.. raw:: html

    <embed>
        <h1>Traduzione <img src="https://raw.githubusercontent.com/gbvitrano/HfcQGIS/master/img/ita.jpg" class="immagonobox" width="90" height="18" alt=""/></h1>
    </embed>
La descrizione delle funzioni in italiano è stata realizzata dal gruppo di traduttori diretti da `Stefano Campus`_

Marco Grisolia, Roberto Angeletti, Michele Beneventi, Marco Braida, Stefano Campus, Luca Casagrande, Paolo Cavallini, Giuliano Curti, Luca Delucchi, Alessandro Fanna, Michele Ferretti, Matteo Ghetta, Anne Gishla, Maurizio Napolitano, Flavio Rigolon

Link utili
~~~~~~~~~
-  `QGIS.org`_
-  `Documentazione di QGIS`_
-  `App di matematica GeoGebra`_

Licenze
~~~~~~~
.. raw:: html

    <embed>
        <p>Se non specificato diversamente, tutti i contenuti sono soggetti alla licenza: <a title="Licenza Creative Commons (CC BY-SA)" href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="license noopener">Creative Commons Attribution-ShareAlike 4.0 licence (CC BY-SA)</a><br>
  <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img class="immagonobox" style="border-width: 0;" title="Se non specificato diversamente, tutti i contenuti sono soggetti alla licenza Creative Commons Attribution-ShareAlike 4.0 licence (CC BY-SA) " src="https://licensebuttons.net/l/by-sa/4.0/88x31.png" alt="Licenza Creative Commons" width="88" height="31"  /></a></a></p>
    </embed>
    
Disclaimer
~~~~~~~~~~~
.. raw:: html

    <embed>
        <p><a href="http://hfcqgis.opendatasicilia.it/it/latest/" target="_parent"><img src="http://hfcqgis.opendatasicilia.it/it/latest/_images/mActionCalculateField.png" class="immagonobox" width="24" height="24" alt=""/></a> Questa guida NON sostituisce il <a href="https://qgis.org/it/docs/index.html#" target="_blank">manuale</a> online di QGIS, cerca solo di rendere più facile la comprensione dello strumento. <br><br> Il marchio <strong>QGIS</strong> è stato realizzato da <a href="https://twitter.com/underdarkGIS?lang=it" target="_blank">Anita Graser</a>, l&rsquo;immagine HfcQGIS è stata realizzata da <a href="https://twitter.com/totofiandaca" target="_blank">Totò Fiandaca</a> (autore del manuale) usando <a href="https://inkscape.org/it/" target="_blank">InkSCAPE</a> e il carattere <a href="https://www.ffonts.net/Trueno-Bold.font" target="_blank">Trueno Bold</a>.<br>
  I colori utilizzati in questo RTD sono fedeli alla <a href="https://www.qgis.org/en/site/getinvolved/styleguide.html#primary-colors" target="_blank">Visual Style Guide</a> di <strong>QGIS</strong></p>
    </embed>

.. raw:: html

    <embed>
        <a href="https://github.com/pigreco/HfcQGIS" title="GitHub repo size in bytesS" target="_blank"><img src="https://img.shields.io/github/repo-size/pigreco/HfcQGIS.svg?style=flat-squar" class="immagonobox" alt="" title="GitHub repo size in bytes"/></a>&nbsp;<a href="https://qgis.org/en/site/getinvolved/donations.html" title="Donate to QGIS" target="_blank"><img src="https://img.shields.io/badge/donate%20to-QGIS-green.svg?style=flat-square" class="immagonobox" alt="Donate to QGIS" title="Donate to QGIS"/></a>
    </embed>

Tag Clouds
~~~~~~~~~~
L'immagine **HfcQGIS** Tag Cloud (in alto nella home) è stata realizzata con il tools `WordArt`_ che consente di creare incredibili e unici word cloud art con facilità.
   
Mappa del sito   
~~~~~~~~~~~~~~
.. toctree::
   :maxdepth: 2
   
   sitemap  

--------------

| **Per visualizzare e consultare correttamente i contenuti di HfcQGIS
  sono necessari:**
| **Risoluzione video desktop:** Pc con scheda video SVGA. Monitor a
  risoluzione minima di 1024x768 pixel con almeno 65.536 colori.
| **Mobile:** Risoluzione minima di 360 x 640 px (modello di riferimento
  Sansung Galaxy S3).
| **Browser:** HfcQGIS è ottimizzato per Microsoft Internet Explorer
  Versione 11.0 e successive versioni, Microsoft Edge versione 25.1 e
  immediatamente successive, Mozilla Firefox versione 50.0 e successive, Chrome versione 40.0 o successiva, Opera versione 48.0 o successiva e Safari versione 9.0 o successiva.
  
.. _WordArt: https://wordart.com/   
.. _Read The Docs: https://docs.readthedocs.io/en/latest/index.html
.. _lavoro: https://github.com/pigreco/HfcQGIS/blob/master/README.md
.. _@OpenDataSicilia: http://opendatasicilia.it/
.. _Andrea Borruso: https://twitter.com/aborruso
.. _Totò Fiandaca: https://twitter.com/totofiandaca
.. _Giovan Battista Vitrano: https://twitter.com/gbvitrano
.. _Ciro Spataro: https://twitter.com/cirospat
.. _Stefano Campus: https://twitter.com/skampus1967?lang=it
.. _QGIS.org: https://qgis.org/it/site/
.. _Documentazione di QGIS: https://qgis.org/it/docs/index.html#
.. _App di matematica GeoGebra: https://www.geogebra.org/?lang=it
.. _guida ufficiale di QGIS: https://qgis.org/it/docs/index.html#
