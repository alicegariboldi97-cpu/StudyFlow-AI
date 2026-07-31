# ==========================================================
# IMPORTAZIONE LIBRERIE
# ==========================================================

from calcoli import calcola_carico_studio

from pdf import (
    carica_pdf,
    estrai_testo,
    analizza_calendario
)

from planner import (
    genera_piano_esami,
    crea_programma_studio,
    ricalcola_piano
)

from grafico import crea_grafico



# ==========================================================
# INIZIO PROGRAMMA
# ==========================================================

print("""
================================
        StudyFlow AI
================================
Ti aiuterà a organizzare le tue sessioni di studio.
""")



# ==========================================================
# DATI STUDENTE
# ==========================================================

print("\nDATI STUDENTE")
print("--------------------")


nome = input(
    "Inserisci nome: "
)


universita = input(
    "Inserisci università: "
)


ore_studio = float(
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
    ore_studio
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



esami = []



for i in range(numero_esami):


    print(
        f"\nEsame {i + 1}"
    )


    nome_esame = input(
        "Nome esame: "
    )


    cfu = int(
        input(
            "CFU: "
        )
    )


    esami.append(
        {
            "nome": nome_esame,
            "cfu": cfu
        }
    )



print("\nESAMI INSERITI")
print("--------------------")


for esame in esami:

    print(
        esame["nome"],
        "|",
        esame["cfu"],
        "CFU"
    )



# ==========================================================
# CARICO DI STUDIO
# ==========================================================

esami = calcola_carico_studio(
    esami,
    ore_studio
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

print("\nCaricamento calendario esami...")
print("--------------------")


nome_pdf = input(
    "Inserisci il nome del file PDF: "
)



documento = carica_pdf(
    nome_pdf
)



testo_completo = estrai_testo(
    documento
)



# ==========================================================
# COLLEGAMENTO ESAMI PDF
# ==========================================================

esami = analizza_calendario(
    esami,
    documento
)



# ==========================================================
# GENERAZIONE PIANO ESAMI
# ==========================================================

esami = genera_piano_esami(
    esami
)



print("\nPIANO ESAMI")
print("--------------------")


for esame in esami:

    print(
        esame["nome"],
        "|",
        esame.get(
            "data_consigliata",
            "Nessuna data disponibile"
        ),
        "|",
        esame.get(
            "tipo_piano",
            ""
        )
    )



# ==========================================================
# GRAFICO
# ==========================================================

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
)



if risposta.lower() == "no":


    obiettivo = input(
        "Inserisci mese e anno obiettivo (MM/AAAA): "
    )


    esami = ricalcola_piano(
        esami,
        obiettivo
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



    crea_grafico(
        esami
    )



# ==========================================================
# PROGRAMMA DI STUDIO
# ==========================================================

esami = crea_programma_studio(
    esami,
    ore_studio
)



print("\nPROGRAMMA DI STUDIO CREATO")
print("--------------------")


print(
    "StudyFlow AI completato."
)
