# ==========================================================
# IMPORTAZIONE LIBRERIE
# ==========================================================

from datetime import datetime, timedelta


# ==========================================================
# GENERAZIONE PIANO ESAMI
# ==========================================================

def genera_piano_esami(esami):

    date_assegnate = []


    for esame in esami:

        scelta = None


        date_esame = sorted(
            esame["date_disponibili"],
            key=lambda x: datetime.strptime(
                x,
                "%d/%m/%Y"
            )
        )


        for data in date_esame:

            data_prova = datetime.strptime(
                data,
                "%d/%m/%Y"
            )


            disponibile = True


            for data_occupata in date_assegnate:

                distanza = abs(
                    (data_prova - data_occupata).days
                )


                if distanza < 21:

                    disponibile = False
                    break


            if disponibile:

                scelta = data_prova
                break



        if scelta is None:

            scelta = datetime.strptime(
                date_esame[0],
                "%d/%m/%Y"
            )

            esame["tipo_piano"] = (
                "Sessione ravvicinata"
            )


        else:

            esame["tipo_piano"] = (
                "Distribuito"
            )



        esame["data_consigliata"] = (
            scelta.strftime("%d/%m/%Y")
        )


        date_assegnate.append(
            scelta
        )


    return esami



# ==========================================================
# CREAZIONE PROGRAMMA DI STUDIO
# ==========================================================

def crea_programma_studio(
    esami,
    media_studio_ore_giornaliere
):


    for esame in esami:


        if esame["data_consigliata"] == "Nessuna data disponibile":

            continue



        data_esame = datetime.strptime(
            esame["data_consigliata"],
            "%d/%m/%Y"
        )


        giorni_preparazione = (
            esame["giorni_preparazione"]
        )


        ore_totali = (
            esame["ore_studio"]
        )


        inizio = data_esame - timedelta(
            days=giorni_preparazione
        )


        esame["inizio_studio"] = (
            inizio.strftime("%d/%m/%Y")
        )


        calendario = []

        ore_rimanenti = ore_totali

        giorno = inizio



        while (
            giorno < data_esame
            and ore_rimanenti > 0
        ):


            ore_giornaliere = min(
                media_studio_ore_giornaliere,
                ore_rimanenti
            )


            calendario.append(
                {
                    "giorno": giorno.strftime(
                        "%d/%m/%Y"
                    ),
                    "ore": ore_giornaliere
                }
            )


            ore_rimanenti -= ore_giornaliere


            giorno += timedelta(
                days=1
            )



        esame["programma_studio"] = (
            calendario
        )


    return esami



# ==========================================================
# RICALCOLO PIANO DOPO FEEDBACK UTENTE
# ==========================================================

def ricalcola_piano(
    esami,
    obiettivo_fine
):


    mese, anno = obiettivo_fine.split("/")


    data_limite = datetime(
        int(anno),
        int(mese),
        28
    )


    date_scelte = []



    for esame in esami:


        data_scelta = None



        date_disponibili = sorted(
            esame["date_disponibili"],
            key=lambda x: datetime.strptime(
                x,
                "%d/%m/%Y"
            )
        )



        for data in date_disponibili:


            data_appello = datetime.strptime(
                data,
                "%d/%m/%Y"
            )



            if data_appello > data_limite:

                continue



            disponibile = True



            for altra_data in date_scelte:


                distanza = abs(
                    (
                        data_appello -
                        altra_data
                    ).days
                )



                if distanza < 21:

                    disponibile = False
                    break



            if disponibile:


                data_scelta = data_appello

                break



        if data_scelta:


            esame["data_consigliata"] = (
                data_scelta.strftime("%d/%m/%Y")
            )


            esame["tipo_piano"] = (
                "Distribuito"
            )


            date_scelte.append(
                data_scelta
            )


        else:


            esame["data_consigliata"] = (
                "Nessuna data disponibile"
            )


            esame["tipo_piano"] = (
                "Oltre obiettivo"
            )



    return esami
