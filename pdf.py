# ==========================================================
# IMPORTAZIONE LIBRERIE
# ==========================================================

import fitz
import re
from difflib import SequenceMatcher



# ==========================================================
# CARICAMENTO PDF
# ==========================================================

def carica_pdf(percorso_pdf):

    documento = fitz.open(percorso_pdf)

    return documento



# ==========================================================
# ESTRAZIONE TESTO
# ==========================================================

def estrai_testo(documento):

    testo_completo = ""

    for pagina in documento:

        testo_completo += pagina.get_text()


    return testo_completo



# ==========================================================
# NORMALIZZAZIONE TESTO
# ==========================================================

def normalizza_testo(testo):

    testo = testo.lower()

    testo = testo.replace("_", " ")

    testo = re.sub(
        r"[^a-zàèéìòù\s]",
        "",
        testo
    )

    testo = " ".join(
        testo.split()
    )

    return testo



# ==========================================================
# CONFRONTO NOMI
# ==========================================================

def nome_simile(nome1, nome2):

    nome1 = normalizza_testo(nome1)

    nome2 = normalizza_testo(nome2)


    risultato = SequenceMatcher(
        None,
        nome1,
        nome2
    ).ratio()


    return risultato >= 0.70



# ==========================================================
# ANALISI CALENDARIO
# ==========================================================

def analizza_calendario(esami, testo_completo):


    for esame in esami:

        esame["date_disponibili"] = []


    data_corrente = []


    pattern_data = r"\d{2}/\d{2}/\d{4}"



    for pagina in documento_globale:


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


                    data_corrente = re.findall(
                        pattern_data,
                        testo_riga
                    )



                for esame in esami:


                    if nome_simile(
                        esame["nome"],
                        testo_riga
                    ):


                        for data in data_corrente:


                            if data not in esame["date_disponibili"]:

                                esame["date_disponibili"].append(
                                    data
                                )


                        print(
                            "Trovato:",
                            esame["nome"],
                            "->",
                            data_corrente
                        )



    return esami



# ==========================================================
# ESTRAZIONE DATE GENERALE
# ==========================================================

def estrai_date_esami(documento):

    date_trovate = []

    pattern_data = r"\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}"


    for pagina, numero in zip(documento, range(len(documento))):

        testo = pagina.get_text()


        date = re.findall(
            pattern_data,
            testo
        )


        for data in date:

            date_trovate.append(
                {
                    "pagina": numero + 1,
                    "data": data
                }
            )


    return date_trovate
