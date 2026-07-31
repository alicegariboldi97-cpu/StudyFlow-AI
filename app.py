# ==========================================================
# STUDYFLOW AI - APP PRINCIPALE
# ==========================================================


from calcoli import calcola_carico_studio
from pdf import (
    carica_pdf,
    analizza_calendario
)
from planner import (
    genera_piano_esami,
    crea_programma_studio,
    ricalcola_piano
)
from grafico import crea_grafico



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


nome = input("Inserisci nome: ")

universita = input(
    "Inserisci università: "
)


ore_giornaliere = float(
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
    ore_giornaliere
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
        f"\nEsame {i+1}"
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


for e in esami:

    print(
        e["nome"],
        "|",
        e["cfu"],
        "CFU"
    )




# ==========================================================
# CARICO STUDIO
# ==========================================================


esami = calcola_carico_studio(
    esami,
    ore_giornaliere
)



print("\nCARICO DI STUDIO")
print("--------------------")


for e in esami:

    print(
        e["nome"],
        "|",
        e["cfu"],
        "CFU |",
        e["ore_studio"],
        "ore"
    )





# ==========================================================
# PDF CALENDARIO
# ==========================================================


print("\nCaricamento calendario esami...")
print("--------------------")


nome_pdf = input(
    "Inserisci il nome del file PDF: "
)



documento = carica_pdf(
    nome_pdf
)



esami = analizza_calendario(
    documento,
    esami
)




# ==========================================================
# CREAZIONE PIANO
# ==========================================================


esami = genera_piano_esami(
    esami
)



print("\nPIANO ESAMI")
print("--------------------")


for e in esami:


    print(
        e["nome"],
        "|",
        e.get(
            "data_consigliata",
            "Nessuna data"
        ),
        "|",
        e.get(
            "tipo_piano",
            ""
        )
    )




# grafico iniziale

crea_grafico(
    esami
)





# ==========================================================
# FEEDBACK UTENTE
# ==========================================================


print(
"""
Ti piace il piano di studio proposto?
"""
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



    print(
        "\nPIANO OTTIMIZZATO"
    )

    print(
        "--------------------"
    )



    for e in esami:

        print(
            e["nome"],
            "|",
            e.get(
                "data_consigliata"
            ),
            "|",
            e.get(
                "tipo_piano"
            )
        )



    crea_grafico(
        esami
    )



else:


    print(
        "\nPerfetto! Piano confermato."
    )




# ==========================================================
# PROGRAMMA DI STUDIO
# ==========================================================


esami = crea_programma_studio(
    esami,
    ore_giornaliere
)



print(
"""
===============================
PROGRAMMA DI STUDIO GENERATO
===============================
"""
)



for e in esami:


    print(
        "\n",
        e["nome"]
    )


    print(
        "Inizio:",
        e.get(
            "inizio_studio",
            ""
        )
    )


    print(
        "Giorni:",
        len(
            e.get(
                "programma_studio",
                []
            )
        )
    )



print(
"""
===============================
      StudioFlow AI terminato
===============================
"""
)
