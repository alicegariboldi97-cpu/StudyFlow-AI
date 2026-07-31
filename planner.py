#==========================================
#generazione del piano di studio
#==========================================

from datetime import datetime

date_assegnate = []

for esame in esami:
    scelta = None

    date_esame = sorted(esame["date_disponibili"], key=lambda x: datetime.strptime(x, "%d/%m/%Y"))

    for data in date_esame:
        data_prova = datetime.strptime(data, "%d/%m/%Y")
        disponibile = True

        for data_occupata in date_assegnate:
            distanza = abs((data_prova - data_occupata).days)

            if distanza < 21:
                disponibile = False
                break

        if disponibile:
            scelta = data_prova
            break

    if scelta is None:
        scelta = datetime.strptime(date_esame[0], "%d/%m/%Y")
        esame["tipo_piano"] = "Sessione ravvicinata"
    else:
        esame["tipo_piano"] = "Distribuito"

    esame["data_consigliata"] = scelta.strftime("%d/%m/%Y")
    date_assegnate.append(scelta)

print("\nPIANO ANNUALE ESAMI\n")

esami_ordinati = sorted(esami, key=lambda x: datetime.strptime(x["data_consigliata"], "%d/%m/%Y"))

for esame in esami_ordinati:
    print(esame["nome"], "|", esame["cfu"], "CFU |", esame["data_consigliata"], "|", esame["tipo_piano"])

#specifica tempistiche di studio per esame#

from datetime import datetime, timedelta

for esame in esami:
    data_esame = datetime.strptime(esame["data_consigliata"], "%d/%m/%Y")
    ore_totali = esame["ore_studio"]
    giorni = esame["giorni_preparazione"]

    inizio = data_esame - timedelta(days=giorni)
    esame["inizio_studio"] = inizio.strftime("%d/%m/%Y")

    calendario = []
    ore_rimanenti = ore_totali
    giorno = inizio

    while giorno < data_esame and ore_rimanenti > 0:
        ore_oggi = min(media_studio_ore_giornaliere, ore_rimanenti)

        calendario.append({"giorno": giorno.strftime("%d/%m/%Y"),
            "ore": ore_oggi})

        ore_rimanenti -= ore_oggi
        giorno += timedelta(days=1)

    esame["programma_studio"] = calendario

for esame in esami:
    print("\n====================")
    print("Esame:", esame["nome"])
    print("CFU:", esame["cfu"])
    print("Ore totali:", esame["ore_studio"])
    print("Inizio studio:", esame["inizio_studio"])
    print("Data esame:", esame["data_consigliata"])
