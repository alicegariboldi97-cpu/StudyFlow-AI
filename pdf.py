import fitz
import re
from difflib import SequenceMatcher


documento_globale = None


# ==============================
# CARICAMENTO PDF
# ==============================

def carica_pdf(percorso_pdf):

    global documento_globale

    documento_globale = fitz.open(percorso_pdf)

    return documento_globale



# ==============================
# ESTRAZIONE TESTO
# ==============================

def estrai_testo(documento):

    testo = ""

    for pagina in documento:

        testo += pagina.get_text()

    return testo



# ==============================
# NORMALIZZAZIONE NOMI
# ==============================

def normalizza(testo):

    testo = testo.lower()

    testo = testo.replace(
        "à","a"
    )

    testo = testo.replace(
        "è","e"
    )

    testo = testo.replace(
        "é","e"
    )

    testo = re.sub(
        r"[^a-z0-9 ]",
        "",
        testo
    )

    return testo.strip()



# ==============================
# TROVA NOME SIMILE
# ==============================

def trova_miglior_match(nome, testo):


    nome_norm = normalizza(nome)


    righe = testo.split("\n")


    migliore = None
    punteggio_migliore = 0


    for riga in righe:

        riga_norm = normalizza(riga)


        if len(riga_norm)<5:
            continue


        punteggio = SequenceMatcher(
            None,
            nome_norm,
            riga_norm
        ).ratio()


        if punteggio > punteggio_migliore:

            punteggio_migliore = punteggio
            migliore = riga


    if punteggio_migliore > 0.55:

        return migliore


    return None



# ==============================
# ESTRAZIONE DATE
# ==============================

def estrai_date_esami(testo, nome_esame):


    righe = testo.split("\n")


    date = []


    trovato = False


    for riga in righe:


        if normalizza(nome_esame) in normalizza(riga):

            trovato=True



        if trovato:


            risultati = re.findall(
                r"\d{2}/\d{2}/\d{4}",
                riga
            )


            date.extend(risultati)



            if len(date)>0:

                break



    return list(set(date))



# ==============================
# ANALISI CALENDARIO
# ==============================


def analizza_calendario(
        documento,
        esami
):


    testo = estrai_testo(documento)



    for esame in esami:


        nome_originale = esame["nome"]


        nome_pdf = trova_miglior_match(
            nome_originale,
            testo
        )



        if nome_pdf:


            date = estrai_date_esami(
                testo,
                nome_pdf
            )


            esame["date_disponibili"]=date


            print(
                "Trovato:",
                nome_originale,
                "->",
                nome_pdf,
                date
            )



        else:


            esame["date_disponibili"]=[]


            print(
                "Non trovato:",
                nome_originale
            )



    return esami
