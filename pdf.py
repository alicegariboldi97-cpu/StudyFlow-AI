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
# ESTRAZIONE TESTO PDF
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

    testo = str(testo).lower()


    testo = testo.replace(
        "_",
        " "
    )


    testo = testo.replace(
        "-",
        " "
    )


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
# CONFRONTO NOMI ESAMI
# ==========================================================

def nome_simile(nome1, nome2):


    nome1 = normalizza_testo(nome1)

    nome2 = normalizza_testo(nome2)



    if nome1 in nome2 or nome2 in nome1:

        return True



    rapporto = SequenceMatcher(
        None,
        nome1,
        nome2
    ).ratio()



    return rapporto >= 0.55



# ==========================================================
# ANALISI CALENDARIO PDF
# ==========================================================

def analizza_calendario(esami, documento):


    pattern_data = r"\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}"



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



                testo_normale = normalizza_testo(
                    testo_riga
                )



                date_trovate = re.findall(
                    pattern_data,
                    testo_riga
                )



                for esame in esami:



                    if nome_simile(
                        esame["nome"],
                        testo_normale
                    ):



                        for data in date_trovate:


                            data = (
                                data
                                .replace("-", "/")
                                .replace(".", "/")
                            )



                            if data not in esame["date_disponibili"]:


                                esame["date_disponibili"].append(
                                    data
                                )



                        print(
                            "Trovato:",
                            esame["nome"],
                            "|",
                            esame["date_disponibili"]
                        )



    for esame in esami:


        if len(esame["date_disponibili"]) == 0:


            print(
                "Non trovato:",
                esame["nome"]
            )



    return esami



# ==========================================================
# ESTRAZIONE DATE GENERALE
# ==========================================================

def estrai_date_esami(documento):


    pattern_data = r"\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}"



    date_trovate = []



    for numero, pagina in enumerate(documento):


        testo = pagina.get_text()



        date = re.findall(
            pattern_data,
            testo
        )



        for data in date:


            data = (
                data
                .replace("-", "/")
                .replace(".", "/")
            )



            date_trovate.append(
                data
            )



    return date_trovate
