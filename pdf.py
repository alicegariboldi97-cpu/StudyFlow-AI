#==========================================
# IMPORTAZIONE LIBRERIE
#==========================================

import fitz
import re
from google.colab import files


#==========================================
# CARICAMENTO DEL PDF
#==========================================

def carica_pdf():

    uploaded = files.upload()

    nome_pdf = list(uploaded.keys())[0]

    documento = fitz.open(nome_pdf)

    return documento


#==========================================
# TRASCRIZIONE DOCUMENTO
#==========================================

def estrai_testo(documento):

    testo_completo = ""

    for pagina in documento:

        testo = pagina.get_text()

        print(testo)

        testo_completo += testo

    print(testo_completo)

    return testo_completo


#==========================================
# ANALISI DEL CALENDARIO ESAMI
#==========================================

def analizza_calendario(esami, testo_completo):

    for esame in esami:

        nome_esame = esame["nome"].replace("_", " ").lower()

        if nome_esame in testo_completo.lower():

            print("Trovato:", nome_esame)

        else:

            print("Non trovato:", nome_esame)

    return esami


#==========================================
# RICERCA DELLE DATE PRESENTI NEL PDF
#==========================================

def cerca_date(documento):

    pattern_data = r"\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}"

    date_trovate = []

    for numero_pagina, pagina in enumerate(documento):

        testo = pagina.get_text()

        date = re.findall(pattern_data, testo)

        for data in date:

            date_trovate.append(
                {"pagina": numero_pagina + 1,
                    "data": data })

    print(date_trovate)

    return date_trovate


#==========================================
# LETTURA DELLE TABELLE
#==========================================

def leggi_tabelle(documento):

    for numero_pagina, pagina in enumerate(documento):

        tabelle = pagina.find_tables()

        print("Pagina:", numero_pagina + 1)

        print("Numero tabelle:", len(tabelle.tables))

        for tabella in tabelle.tables:

            dati = tabella.extract()

            for riga in dati[:5]:

                print(riga)

            print("----------------")


#==========================================
# GENERAZIONE DEL CALENDARIO ESAMI
#==========================================

def genera_calendario_esami(documento, esami):

    pattern_data = r"\d{2}/\d{2}/\d{4}"

    for esame in esami:

        esame["date_disponibili"] = []

    date_correnti = []

    for pagina in documento:

        tabelle = pagina.find_tables()

        for tabella in tabelle.tables:

            righe = tabella.extract()

            for riga in righe:

                testo_riga = " ".join(
                    str(cella)
                    for cella in riga
                    if cella)

                if "Giorno" in testo_riga:

                    date_correnti = re.findall(
                        pattern_data,
                        testo_riga)

                    print("Nuovo blocco date:", date_correnti)

                for esame in esami:

                    nome_esame = (
                        esame["nome"]
                        .replace("_", " ")
                        .lower())

                    if nome_esame in testo_riga.lower():

                        print("Trovato:",
                            nome_esame,
                            "->",
                            date_correnti )

                        for data in date_correnti:

                            if data not in esame["date_disponibili"]:

                                esame["date_disponibili"].append(data)

    for esame in esami:

        print()

        print(esame["nome"])

        print(esame["date_disponibili"])

    return esami
