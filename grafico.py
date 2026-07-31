from datetime import datetime
import matplotlib.pyplot as plt


def crea_grafico(esami):

    esami_validi = []

    for esame in esami:

        if (
            "data_consigliata" not in esame
            or esame["data_consigliata"] == "Nessuna data disponibile"
        ):
            continue

        if "inizio_studio" not in esame:
            continue

        esami_validi.append(esame)


    if not esami_validi:
        print("Nessun dato disponibile per il grafico")
        return


    esami_ordinati = sorted(
        esami_validi,
        key=lambda x: datetime.strptime(
            x["inizio_studio"],
            "%d/%m/%Y"
        )
    )


    nomi = []
    inizi = []
    durate = []


    for esame in esami_ordinati:

        inizio = datetime.strptime(
            esame["inizio_studio"],
            "%d/%m/%Y"
        )

        fine = datetime.strptime(
            esame["data_consigliata"],
            "%d/%m/%Y"
        )

        giorni = (fine - inizio).days


        nomi.append(esame["nome"])
        inizi.append(inizio)
        durate.append(giorni)



    fig, ax = plt.subplots(figsize=(12,7))


    ax.barh(
        nomi,
        durate,
        left=inizi
    )


    ax.set_xlabel("Periodo di studio")
    ax.set_ylabel("Esami")
    ax.set_title("Piano di studio StudyFlow AI")


    plt.tight_layout()

    plt.show()
