# ==========================================================
# STUDYFLOW AI - GRAFICO
# ==========================================================

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta



def crea_grafico(esami):

    print("\nCreazione grafico StudyFlow AI...")


    dati = []


    print("\nDATI RICEVUTI DAL GRAFICO:")

    for e in esami:
        print(e)



    for esame in esami:


        nome = esame.get(
            "nome",
            "Esame"
        )


        data_esame = esame.get(
            "data_consigliata"
        )


        inizio = esame.get(
            "inizio_studio"
        )


        # Se manca l'inizio studio
        # crea un periodo stimato
        if not inizio:

            if data_esame and data_esame != "Nessuna data disponibile":

                try:

                    fine = datetime.strptime(
                        data_esame,
                        "%d/%m/%Y"
                    )


                    inizio_data = fine - timedelta(
                        days=20
                    )


                    dati.append(
                        (
                            nome,
                            inizio_data,
                            20
                        )
                    )


                except:

                    pass


            continue



        try:

            data_inizio = datetime.strptime(
                inizio,
                "%d/%m/%Y"
            )


            if data_esame:

                data_fine = datetime.strptime(
                    data_esame,
                    "%d/%m/%Y"
                )

            else:

                data_fine = data_inizio + timedelta(
                    days=20
                )


            giorni = (
                data_fine - data_inizio
            ).days


            if giorni <= 0:

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
                "Errore:",
                nome,
                errore
            )



    print("\nDATI GRAFICO FINALI:")
    print(dati)



    if len(dati) == 0:

        print(
            "Nessun dato disponibile per il grafico"
        )

        return None




    nomi = [
        x[0]
        for x in dati
    ]


    date_inizio = [
        x[1]
        for x in dati
    ]


    durata = [
        x[2]
        for x in dati
    ]



    fig, ax = plt.subplots(
        figsize=(12,7)
    )



    ax.barh(
        nomi,
        durata,
        left=date_inizio
    )



    ax.set_title(
        "StudyFlow AI - Piano di studio"
    )


    ax.set_xlabel(
        "Periodo di preparazione"
    )


    ax.set_ylabel(
        "Esami"
    )



    ax.xaxis.set_major_formatter(
        mdates.DateFormatter(
            "%d/%m/%Y"
        )
    )


    plt.xticks(
        rotation=45
    )


    plt.tight_layout()


    plt.show()



    return fig
