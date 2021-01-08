import requests

url = "http://127.0.0.1:5000/api/"

#Data
Gender = 1   # Le sexe de la personne 
Age = 22 # L'age de la personne
family_history_with_overweight = 0 # Antécédent familliale lié à l'obésité
FAVC = 0  # Nourriture calorique
FCVC = 0  # légumes
NCP = 4  # nombre de repas
CAEC = 0  # grignotage
SMOKE = 0  # fume
CH2O = 1.5  # consommation d'eau
SCC = 1  #surveillance des caloris
FAF = 2  #frequence d'activité physique
TUE = 5  # temps d'écran
CALC = 2  # consommation d'alcool
MTRANS = 1 # moyen de transport

#Creation du  JSON
data = [[Gender,Age,family_history_with_overweight,FAVC,FCVC,NCP,CAEC,SMOKE,CH2O,SCC,FAF,TUE,CALC,MTRANS]]
j_data = str(data)

headers = {
  'Content-Type': 'application/json'
}

#Envoi d'une requête post à l'API
response = requests.request("POST", url, headers=headers, data=j_data)
#DAffichage de la réponse
print(response.text)