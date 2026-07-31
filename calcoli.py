# ==========================================================
# CALCOLO CARICO DI STUDIO
# ==========================================================


def calcola_carico_studio(esami, media_studio_ore_giornaliere):


    for esame in esami:


        cfu = esame["cfu"]


        # ogni CFU = 15 ore di studio

        ore_totali = cfu * 15


        esame["ore_studio"] = ore_totali



        # giorni necessari

        giorni = ore_totali / media_studio_ore_giornaliere


        esame["giorni_preparazione"] = int(
            giorni
        )



    return esami
