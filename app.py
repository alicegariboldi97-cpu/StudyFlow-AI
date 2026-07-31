# ==========================================================
# IMPORTAZIONE MODULI
# ==========================================================

from calcoli import calcola_carico_studio
from pdf import carica_pdf, estrai_testo, analizza_calendario, cerca_date
from planner import genera_piano_esami, crea_programma_studio, ricalcola_piano
from grafico import crea_grafico


# ==========================================================
# BENVENUTO
# ==========================================================

print("Benvenuti in StudyFlow AI")
print("Ti aiuterà a organizzare le tue sessioni di studio.")


# ==========================================================
# DATI PERSONALI
# ==========================================================

nome = "Alice"
universita = "Ecampus"
media_studio_ore_giornaliere = 4


# ==========================================================
# ESAMI
# ==========================================================

cfu_esami = { "neuropsicologia": 6,
    "psichiatria": 9,
    "psicologia_fisiologica_e_delle_emozioni": 9,
    "psicometria": 6,
    "psicologia_dello_sviluppo_tipico_e_atipico": 9,
    "filosofia_della_mente": 9,
    "psicologia_clinica": 9}


# ==========================================================
# CALCOLO CARICO STUDIO
# ==========================================================

esami = calcola_carico_studio(cfu_esami, media_studio_ore_giornaliere)

for esame in esami:
    print(esame)
