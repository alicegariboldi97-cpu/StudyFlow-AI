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
            key=lambda x: datetime.strptime(x, "%d/%m/%Y")
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

            esame["tipo_piano"] = "Sessione ravvicinata"


        else:

            esame["tipo_piano"] = "Distribuito"



        esame["data_consigliata"] = scelta.strftime(
            "%d/%m/%Y"
        )


        date_assegnate.append(scelta)



    return esami


# ==========================================================
# CREAZIONE PROGRAMMA DI STUDIO
# ==========================================================

def crea_programma_studio(
    esami,
    media_studio_ore_giornaliere
):


    for esame in esami:


        data_esame = datetime.strptime(
            esame["data_consigliata"],
            "%d/%m/%Y"
        )


        giorni = esame["giorni_preparazione"]

        ore_totali = esame["ore_studio"]


        inizio = data_esame - timedelta(
            days=giorni
        )


        esame["inizio_studio"] = inizio.strftime(
            "%d/%m/%Y"
        )


        calendario = []

        ore_rimanenti = ore_totali

        giorno = inizio



        while giorno < data_esame and ore_rimanenti > 0:


            ore_oggi = min(
                media_studio_ore_giornaliere,
                ore_rimanenti
            )


            calendario.append(
                {
                    "giorno": giorno.strftime(
                        "%d/%m/%Y"
                    ),
                    "ore": ore_oggi
                }
            )


            ore_rimanenti -= ore_oggi

            giorno += timedelta(days=1)



        esame["programma_studio"] = calendario



    return esami


# ==========================================================
# RICALCOLO PIANO DOPO FEEDBACK UTENTE
# ==========================================================

def ricalcola_piano(esami, obiettivo_fine):

    mese, anno = obiettivo_fine.split("/")

    data_limite = datetime(
        int(anno),
        int(mese),
        28
    )


    esami_assegnati = []


    for esame in esami:


        punteggio_migliore = -999

        data_migliore = None



        for data in esame["date_disponibili"]:


            data_appello = datetime.strptime(
                data,
                "%d/%m/%Y"
            )


            if data_appello > data_limite:

                continue



            punteggio = 0



            giorni_disponibili = (
                data_appello - datetime.today()
            ).days



            # tempo sufficiente per preparare l'esame

            if giorni_disponibili >= esame["giorni_preparazione"]:

                punteggio += 50

            else:

                punteggio -= 50



            # peso CFU

            if esame["cfu"] >= 9:

                punteggio += 20

            else:

                punteggio += 10



            # evita sovrapposizioni

            for altro_esame in esami_assegnati:


                distanza = abs(
                    (
                        data_appello -
                        altro_esame
                    ).days
                )


                if distanza < 21:

                    punteggio -= 100



            if punteggio > punteggio_migliore:


                punteggio_migliore = punteggio

                data_migliore = data_appello



        if data_migliore:


            esame["data_consigliata"] = data_migliore.strftime(
                "%d/%m/%Y"
            )


            esame["tipo_piano"] = "Distribuito"


            esami_assegnati.append(
                data_migliore
            )



        else:


            esame["data_consigliata"] = (
                "Nessuna data disponibile"
            )


            esame["tipo_piano"] = (
                "Oltre obiettivo"
            )


    return esami
