#==========================================
# IMPORTAZZIONE MODULI
#==========================================

from calcoli import calcola_carico_studio

#==========================================
# BENVENUTO
#==========================================

print("Benvenuti in StudyFlow AI")
print("Ti aiuterà a organizzare le tue sessioni.")

#==========================================
# DATI PERSONALI
#==========================================

nome = "Alice"
universita = "Ecampus"
media_studio_ore_giornaliere = 4

#==========================================
# PIANO DI STUDI
#==========================================

cfu_esami = {
    "neuropsicologia": 6,
    "psichiatria": 9,
    "psicologia_fisiologica_e_delle_emozioni": 9,
    "psicometria": 6,
    "psicologia_dello_sviluppo_tipico_e_atipico": 9,
    "filosofia_della_mente": 9,
    "psicologia_clinica": 9
}

#==========================================
# CALCOLO DEL CARICO DI STUDIO
#==========================================

esami = calcola_carico_studio(
    cfu_esami,
    media_studio_ore_giornaliere
)

#==========================================
# FEEDBACK UTENTE
#==========================================

print("\nTi piace il piano di studio proposto?")
risposta = input("Rispondi (si/no): ").strip().lower()

if risposta == "si":

    print("\nOttimo! Buono studio!")

elif risposta == "no":

    print("\nEntro quando vorresti aver completato tutti gli esami?")
    obiettivo_fine = input("Inserisci mese e anno (MM/AAAA): ")

else:

    print("\nRisposta non valida.")
