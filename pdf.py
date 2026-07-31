# ==========================================================
# IMPORTAZIONE LIBRERIE
# ==========================================================

import fitz
import re
from google.colab import files


# ==========================================================
# CARICAMENTO PDF
# ==========================================================

def carica_pdf():

    file_caricato = files.upload()

    nome_pdf = list(file_caricato.keys())[0]

    documento = fitz.open(nome_pdf)

    return documento


# ==========================================================
# ESTRAZIONE TESTO DAL PDF
# ==========================================================

def estrai_testo(documento):

    testo_completo = ""

    for pagina in documento:

        testo_pagina = pagina.get_text()

        testo_completo += testo_pagina


    return testo_completo


# ==========================================================
# CONTROLLO PRESENZA ESAMI NEL PDF
# ==========================================================

def analizza_calendario(esami, testo_completo):

    testo_pdf = testo_completo.lower()


    for esame in esami:

        nome_esame = esame["nome"].replace("_", " ").lower()


        if nome_esame in testo_pdf:

            print("Trovato:", nome_esame)

        else:

            print("Non trovato:", nome_esame)


    return esami


# ==========================================================
# RICERCA DATE NEL PDF
# ==========================================================

def cerca_date(documento):

    pattern_data = r"\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}"

    date_trovate = []


    for numero_pagina, pagina in enumerate(documento):

        testo = pagina.get_text()

        date = re.findall(pattern_data, testo)


        for data in date:

            date_trovate.append(
                {
                    "pagina": numero_pagina + 1,
                    "data": data
                }
            )


    return date_trovate


# ==========================================================
# LETTURA TABELLE PDF
# ==========================================================

def leggi_tabelle(documento):

    tabelle_pdf = []


    for numero_pagina, pagina in enumerate(documento):

        tabelle = pagina.find_tables()


        for tabella in tabelle.tables:

            dati = tabella.extract()

            tabelle_pdf.append(
                {
                    "pagina": numero_pagina + 1,
                    "dati": dati
                }
            )


    return tabelle_pdf


# ==========================================================
# ASSOCIAZIONE ESAMI E DATE
# ==========================================================

def estrai_date_esami(documento, esami):

    pattern_data = r"\d{2}/\d{2}/\d{4}"

    date_correnti = []


    for esame in esami:

        esame["date_disponibili"] = []


    for pagina in documento:

        tabelle = pagina.find_tables()


        for tabella in tabelle.tables:

            righe = tabella.extract()


            for riga in righe:

                testo_riga = " ".join(
                    str(cella)
                    for cella in riga
                    if cella
                )


                if "Giorno" in testo_riga:

                    date_correnti = re.findall(pattern_data, testo_riga)


                for esame in esami:

                    nome_esame = esame["nome"].replace("_", " ").lower()


                    if nome_esame in testo_riga.lower():

                        for data in date_correnti:

                            if data not in esame["date_disponibili"]:

                                esame["date_disponibili"].append(data)


    return esami
