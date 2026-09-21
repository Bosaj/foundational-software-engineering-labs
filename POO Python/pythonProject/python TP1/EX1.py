def convertir_temps(seconde):
    heures = seconde // 3600
    seconde_restantes = seconde % 3600
    minutes = seconde_restantes // 60
    secondes = seconde_restantes % 60
    return heures, minutes, secondes

temps_en_secondes = int(input("Entrez un temps en secondes : "))
heures, minutes, secondes = convertir_temps(temps_en_secondes)
print(f"{heures}H : {minutes}m : {secondes}s")