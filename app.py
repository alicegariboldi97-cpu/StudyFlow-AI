#==========================================
#benvenuto
#==========================================

print("Benvenuti in Studyflow AI",
      "Ti aiuterà a organizzare le tue sessioni")
#==========================================
#dati personali
#==========================================

nome="Alice"
universita="Ecampus"
media_studio_ore_giornaliere=4
inizio_studio="10-08-2026"
print(nome)
print(universita)
print(media_studio_ore_giornaliere)
print(inizio_studio)

#cfu e nome esame#

cfu_esami = {"neuropsicologia": 6,
            "psichiatria" : 9,
            "psicologia_fisiologica_e_delle_emozioni": 9,
            "psicometria": 6,
            "psicologia_dello_sviluppo_tipico_e_atipico": 9,
            "filosofia_della_mente": 9,
            "psicologia_clinica":9}
print (cfu_esami)
#==========================================
#feedback utente
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
