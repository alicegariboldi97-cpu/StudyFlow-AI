#==========================================
#caricamento del pdf
#==========================================

from google.colab import files
uploaded=files.upload()
#==========================================
#software lettura pdf
#==========================================

!pip install pymupdf

#==========================================
#trascrizione documento
#==========================================

import fitz
nome_pdf=list(uploaded.keys())[0]
documento=fitz.open(nome_pdf)
for pagina in documento:
    testo=pagina.get_text()
    print(testo)

#lettura testo in toto#

testo_completo=""
for pagina in documento:
  testo_completo+=pagina.get_text()
print(testo_completo)

#==========================================
#analisi del calendario esami
#==========================================

for esame in esami:
    nome_esame = esame["nome"].replace("_", " ").lower()
    if nome_esame in testo_completo.lower():
        print("Trovato:", nome_esame)
    else:
        print("Non trovato:", nome_esame)
      
#ricerca delle date presenti nel pdf#

import re
pattern_data = r"\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}"
date_trovate = []
for numero_pagina, pagina in enumerate(documento):
    testo = pagina.get_text()
    date = re.findall(pattern_data, testo)
    for data in date:
        date_trovate.append({"pagina": numero_pagina + 1,
                             "data": data})

print(date_trovate)

#lettura delle tabelle#

for numero_pagina, pagina in enumerate(documento):
  tabelle = pagina.find_tables()
  
  print("Pagina:", numero_pagina+1)
  print("Numero tabelle:", len(tabelle.tables))
  
  for tabella in tabelle.tables: dati = tabella.extract()

  for riga in dati[:5]:
    print(riga)
    print("----------------")

#==========================================
#generazione del calendario esami
#==========================================

import re

pattern_data = r"\d{2}/\d{2}/\d{4}"

for esame in esami:
    esame["date_disponibili"] = []

date_correnti = []

for pagina in documento:
    tabelle = pagina.find_tables()

    for tabella in tabelle.tables:
        righe = tabella.extract()

        for riga in righe:
            testo_riga = " ".join(str(cella) for cella in riga if cella)

            if "Giorno" in testo_riga:
                date_correnti = re.findall(pattern_data, testo_riga)
                print("Nuovo blocco date:", date_correnti)

            for esame in esami:
                nome_esame = esame["nome"].replace("_", " ").lower()

                if nome_esame in testo_riga.lower():
                    print("Trovato:", nome_esame, "->", date_correnti)

                    for data in date_correnti:
                        if data not in esame["date_disponibili"]:
                            esame["date_disponibili"].append(data)

for esame in esami:
    print("\n", esame["nome"])
    print(esame["date_disponibili"])
