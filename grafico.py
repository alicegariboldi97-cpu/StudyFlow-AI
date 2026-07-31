import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime


def crea_grafico(esami):

    print("\nCreazione grafico StudyFlow AI...")


    dati = []


    for esame in esami:

        nome = esame.get("nome", "Senza nome")
        inizio = esame.get("inizio_studio")
        fine = esame.get("data_consigliata")


        if not inizio or not fine:
            continue


        if fine == "Nessuna data disponibile":
            continue


        try:

            data_inizio = datetime.strptime(
                inizio,
                "%d/%m/%Y"
            )

            data_fine = datetime.strptime(
                fine,
                "%d/%m/%Y"
            )


            giorni = (
                data_fine - data_inizio
            ).days


            if giorni < 1:
                giorni = 1


            dati.append(
                (
                    nome,
                    data_inizio,
                    giorni
                )
            )


        except Exception as errore:

            print(
                "Errore nel grafico:",
                nome,
                errore
            )


    if not dati:

        print(
            "Nessun dato valido per creare il grafico"
        )

        return



    nomi = [
        x[0]
        for x in dati
    ]


    inizi = [
        x[1]
        for x in dati
    ]


    durate = [
        x[2]
        for x in dati
    ]



    fig, ax = plt.subplots(
        figsize=(12,7)
    )


    ax.barh(
        nomi,
        durate,
        left=inizi
    )


    ax.set_title(
        "Piano di studio StudyFlow AI"
    )


    ax.set_xlabel(
        "Periodo di studio"
    )


    ax.set_ylabel(
        "Esami"
    )


    ax.xaxis.set_major_formatter(
        mdates.DateFormatter("%d/%m/%Y")
    )


    plt.xticks(
        rotation=45
    )


    plt.tight_layout()


    # fondamentale per Colab
    plt.show()


    return fig
