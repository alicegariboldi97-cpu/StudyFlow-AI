#==========================================
#visualizzazione del piano
#==========================================

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

esami_ordinati = sorted(esami, key=lambda x: datetime.strptime(x["inizio_studio"], "%d/%m/%Y"))

nomi = []
inizi = []
durate = []
date_esame = []

for esame in esami_ordinati:
    inizio = datetime.strptime(esame["inizio_studio"], "%d/%m/%Y")
    fine = datetime.strptime(esame["data_consigliata"], "%d/%m/%Y")

    nomi.append(esame["nome"].replace("_", " "))
    inizi.append(inizio)
    durate.append((fine - inizio).days)
    date_esame.append(fine)

fig, ax = plt.subplots(figsize=(12, 7))

for i in range(len(nomi)):
    ax.barh(i, durate[i], left=inizi[i], height=0.5)
    ax.axvline(date_esame[i], linewidth=1)

ax.set_yticks(range(len(nomi)))
ax.set_yticklabels(nomi)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))

plt.xticks(rotation=45)

ax.set_title("Piano annuale di studio")
ax.set_xlabel("Periodo di preparazione")
ax.set_ylabel("Esami")

ax.grid(axis="x")

plt.tight_layout()
plt.show()
