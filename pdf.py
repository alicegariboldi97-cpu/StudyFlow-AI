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

        testo = pagina.get_text()

        testo_completo += testo


    return testo_completo



# ==========================================================
# NORMALIZZAZIONE NOMI
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
# CONFRONTO NOMI ESAMI
# ==========================================================

def nome_simile(nome1, nome2):

    nome1 = normalizza_testo(nome1)

    nome2 = normalizza_testo(nome2)


    rapporto = SequenceMatcher(
        None,
        nome1,
        nome2
    ).ratio()


    return rapporto >= 0.75



# ==========================================================
# ANALISI CALENDARIO ESAMI
# ==========================================================

def analizza_calendario(esami, testo_completo):


    testo_pdf = normalizza_testo(
        testo_completo
    )


    for esame in esami:


        trovato = False


        nome_esame = esame["nome"]



        parole_pdf = testo_pdf.split()



        for parola in parole_pdf:


            if nome_simile(
                nome_esame,
                parola
            ):


                trovato = True

                break



        if trovato:

            print(
                "Trovato:",
                nome_esame
            )


        else:

            print(
                "Non trovato:",
                nome_esame
            )


        esame["date_disponibili"] = []



    return esami



# ==========================================================
# ESTRAZIONE DATE DAL PDF
# ==========================================================

def estrai_date_esami(documento):


    pattern_data = r"\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}"


    date_trovate = []



    for numero_pagina, pagina in enumerate(documento):


        testo = pagina.get_text()


        date = re.findall(
            pattern_data,
            testo
        )



        for data in date:


            data_pulita = data.replace(
                "-",
                "/"
            ).replace(
                ".",
                "/"
            )


            date_trovate.append(
                {
                    "pagina": numero_pagina + 1,
                    "data": data_pulita
                }
            )



    return date_trovate
