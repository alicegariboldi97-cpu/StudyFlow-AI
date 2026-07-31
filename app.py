# ==========================================================
# IMPORTAZIONE MODULI
# ==========================================================

from calcoli import calcola_carico_studio
from pdf import carica_pdf, estrai_testo, analizza_calendario, estrai_date_esami
from planner import genera_piano_esami, crea_programma_studio, ricalcola_piano
from grafico import crea_grafico


# ==========================================================
# BENVENUTO
# ==========================================================

print("Benvenuti in StudyFlow AI")
print("Ti aiuterà a organizzare le tue sessioni di studio.")


# ==========================================================
# DATI PERSONALI
# ==========================================================

nome = "Alice"
universita = "Ecampus"
media_studio_ore_giornaliere = 4


print("\nDATI STUDENTE")
print("--------------------")
print("Nome:", nome)
print("Università:", universita)
print("Ore studio giornaliere:", media_studio_ore_giornaliere)


# ==========================================================
# DATI ESAMI
# ==========================================================

cfu_esami = {
    "neuropsicologia": 6,
    "psichiatria": 9,
    "psicologia_fisiologica_e_delle_emozioni": 9,
    "psicometria": 6,
    "psicologia_dello_sviluppo_tipico_e_atipico": 9,
    "filosofia_della_mente": 9,
    "psicologia_clinica": 9
}


# ==========================================================
# CALCOLO CARICO STUDIO
# ==========================================================

esami = calcola_carico_studio(
    cfu_esami,
    media_studio_ore_giornaliere
)


print("\nCARICO DI STUDIO")
print("--------------------")

for esame in esami:

    print(
        esame["nome"],
        "|",
        esame["cfu"],
        "CFU |",
        esame["ore_studio"],
        "ore"
    )


# ==========================================================
# CARICAMENTO PDF
# ==========================================================

print("\nCaricamento calendario esami...")

documento = carica_pdf()


# ==========================================================
# ANALISI PDF
# ==========================================================

testo_completo = estrai_testo(documento)

analizza_calendario(esami, testo_completo)


# ==========================================================
# ASSOCIAZIONE DATE AGLI ESAMI
# ==========================================================

esami = estrai_date_esami(documento, esami)


# ==========================================================
# CREAZIONE PIANO ESAMI
# ==========================================================

esami = genera_piano_esami(esami)


esami = crea_programma_studio(
    esami,
    media_studio_ore_giornaliere
)


print("\nPIANO ESAMI")
print("--------------------")

for esame in esami:

    print(
        esame["nome"],
        "|",
        esame["data_consigliata"],
        "|",
        esame["tipo_piano"]
    )


# ==========================================================
# VISUALIZZAZIONE GRAFICO
# ==========================================================

crea_grafico(esami)


# ==========================================================
# FEEDBACK UTENTE
# ==========================================================

risposta = input(
    "\nTi piace il piano di studio proposto? (si/no): "
).lower()


if risposta == "si":

    print("\nOttimo! Buono studio!")


elif risposta == "no":

    obiettivo_fine = input(
        "Inserisci il mese e anno obiettivo (MM/AAAA): "
    )


    esami = ricalcola_piano(
        esami,
        obiettivo_fine
    )


    esami = crea_programma_studio(
        esami,
        media_studio_ore_giornaliere
    )


    print("\nPIANO OTTIMIZZATO")
    print("--------------------")

    for esame in esami:

        print(
            esame["nome"],
            "|",
            esame["data_consigliata"],
            "|",
            esame["tipo_piano"]
        )


    crea_grafico(esami)


else:

    print("\nRisposta non valida.")
