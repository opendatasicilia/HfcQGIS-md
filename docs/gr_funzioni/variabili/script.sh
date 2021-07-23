#!/bin/bash
set -x

for i in $(cat elenco_variabili320.txt)
do
	touch $i.md
	cp _file_tipo.md $i.md
done
