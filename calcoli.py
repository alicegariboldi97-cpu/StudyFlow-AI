# ==========================================================
# CALCOLO DEL CARICO DI STUDIO
# ==========================================================

def calcola_carico_studio(cfu_esami, media_studio_ore_giornaliere):

    ore_per_cfu = 15
    esami = []

    for nome_esame, cfu in cfu_esami.items():

        ore_studio = cfu * ore_per_cfu
        giorni_base = ore_studio / media_studio_ore_giornaliere
        giorni_preparazione = round(giorni_base * 1.5)

        esame = { "nome": nome_esame,
            "cfu": cfu,
            "ore_studio": ore_studio,
            "giorni_base": giorni_base,
            "giorni_preparazione": giorni_preparazione,
            "date_disponibili": []}

        esami.append(esame)

    return esami
