# ==========================================================
# IMPORTAZIONE MODULI
# ==========================================================

from calcoli import calcola_carico_studio
from pdf import (
    carica_pdf,
    estrai_testo,
    analizza_calendario,
    estrai_date_esami
)
from planner import (
    genera_piano_esami,
    ricalcola_piano,
    crea_programma_studio
)
from grafico import crea_grafico


# ==========================================================
# BENVENUTO
# ==========================================================

print("================================")
print("        StudyFlow AI")
print("================================")

print(
    "Ti aiuterà a organizzare le tue sessioni di studio.\n"
)


# ==========================================================
# DATI STUDENTE
# ==========================================================

print("DATI STUDENTE")
print("--------------------")


nome = input(
    "Inserisci nome: "
)


universita = input(
    "Inserisci università: "
)


media_studio_ore_giornaliere = float(
    input(
        "Ore di studio giornaliere: "
    )
)


print("\nDATI INSERITI")
print("--------------------")

print(
    "Nome:",
    nome
)

print(
    "Università:",
    universita
)

print(
    "Ore studio giornaliere:",
    media_studio_ore_giornaliere
)



# ==========================================================
# INSERIMENTO ESAMI
# ==========================================================

print("\nINSERIMENTO ESAMI")
print("--------------------")


numero_esami = int(
    input(
        "Quanti esami vuoi inserire? "
    )
)


cfu_esami = {}


for i in range(numero_esami):

    print(
        "\nEsame",
        i + 1
    )


    nome_esame = input(
        "Nome esame: "
    )


    cfu = int(
        input(
            "CFU: "
        )
    )


    cfu_esami[nome_esame] = cfu



print("\nESAMI INSERITI")
print("--------------------")


for esame, cfu in cfu_esami.items():

    print(
        esame,
        "|",
        cfu,
        "CFU"
    )



# ==========================================================
# CALCOLO CARICO DI STUDIO
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
# CARICAMENTO CALENDARIO PDF
# ==========================================================

print(
    "\nCaricamento calendario esami..."
)

percorso_pdf = input(
    "Inserisci il nome del file PDF: "
)


documento = carica_pdf(
    percorso_pdf
)

# ==========================================================
# ANALISI CALENDARIO
# ==========================================================

testo_completo = estrai_testo(
    documento
)


esami = analizza_calendario(
    esami,
    testo_completo
)

# ==========================================================
# GENERAZIONE PRIMO PIANO
# ==========================================================

esami = genera_piano_esami(
    esami
)


print(
    "\nPIANO ESAMI"
)

print(
    "--------------------"
)


for esame in esami:

    print(
        esame["nome"],
        "|",
        esame["data_consigliata"],
        "|",
        esame["tipo_piano"]
    )



crea_grafico(
    esami
)



# ==========================================================
# FEEDBACK UTENTE
# ==========================================================

print(
    "\nTi piace il piano di studio proposto?"
)


risposta = input(
    "Rispondi (si/no): "
).lower()



if risposta == "no":

    obiettivo_fine = input(
        "Inserisci mese e anno obiettivo (MM/AAAA): "
    )


    esami = ricalcola_piano(
        esami,
        obiettivo_fine
    )


    print(
        "\nPIANO OTTIMIZZATO"
    )

    print(
        "--------------------"
    )


    for esame in esami:

        print(
            esame["nome"],
            "|",
            esame["data_consigliata"],
            "|",
            esame["tipo_piano"]
        )



# ==========================================================
# PROGRAMMA STUDIO
# ==========================================================

esami = crea_programma_studio(
    esami,
    media_studio_ore_giornaliere
)



# ==========================================================
# GRAFICO FINALE
# ==========================================================

crea_grafico(
    esami
)
