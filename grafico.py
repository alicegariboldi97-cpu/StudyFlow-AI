import matplotlib.pyplot as plt
from datetime import datetime


def crea_grafico(esami):

    print("\nCreazione grafico StudyFlow AI...")

    nomi = []
    date_inizio = []
    durate = []


    for esame in esami:

        if esame.get("data_consigliata") in [
            None,
            "Nessuna data disponibile"
        ]:
            continue

        if "inizio_studio" not in esame:
            continue


        try:

            inizio = datetime.strptime(
                esame["inizio_studio"],
                "%d/%m/%Y"
            )

            fine = datetime.strptime(
                esame["data_consigliata"],
                "%d/%m/%Y"
            )


            giorni = (fine - inizio).days


            if giorni <= 0:
                giorni = 1


            nomi.append(esame["nome"])
            date_inizio.append(inizio)
            durate.append(giorni)


        except Exception as e:

            print(
                "Errore grafico per",
                esame.get("nome"),
                ":",
                e
            )


    if len(nomi) == 0:

        print(
            "Nessun esame disponibile per il grafico"
        )

        return



    fig, ax = plt.subplots(figsize=(12,7))


    ax.barh(
        nomi,
        durate,
        left=date_inizio
    )


    ax.set_title(
        "Piano di studio StudyFlow AI"
    )

    ax.set_xlabel(
        "Periodo di preparazione"
    )

    ax.set_ylabel(
        "Esami"
    )


    plt.xticks(rotation=45)

    plt.tight_layout()


    # MOSTRA IL GRAFICO IN COLAB
    plt.show()


    # evita che Colab mostri solo Figure(...)
    return fig
