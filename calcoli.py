#==========================================
#calcolo del carico di studio
#==========================================

ore_per_cfu=15
esami=[]
for nome_esame, cfu in cfu_esami.items():
  ore_studio=cfu*ore_per_cfu
  giorni_base=ore_studio/media_studio_ore_giornaliere
  giorni_preparazione=round(giorni_base*1.5)
  esame={"nome": nome_esame,
         "cfu": cfu,
         "ore_studio": ore_studio,
         "giorni_base": giorni_base,
         "giorni_preparazione": giorni_preparazione}
  esami.append(esame)
for esame in esami:
  print(esame)
