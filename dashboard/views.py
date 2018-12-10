from django.shortcuts import render, redirect
from django.views.generic import View
import json


from .forms import ClientForm
from .models import Conso_eur, Conso_watt


class ClientFormView(View):
    def get(self, request):
        return render(request, 'dashboard/accueil.html')

    def post(self, request):
        form = ClientForm(request.POST)

        if form.is_valid():
            client_id = form.cleaned_data['client']
            return redirect('dashboard:results', client_id=client_id)

def results(request, client_id):
    conso_euro = []
    conso_watt = []
    annual_costs = [0, 0]
    is_elec_heating = True
    dysfunction_detected = False

    ###################################
    ## Recupération des données dans la BDD pour l'utilisateur concerné.
    consommation_euro = Conso_eur.objects.filter(client_id=client_id).order_by('year')
    consommation_watt = Conso_watt.objects.filter(client_id=client_id).order_by('year')

    ## conso_eur et conso_watt remplis avec les donnéees,les 12 premières cases pour 2016, les 12 suivantes pour 2017
    ## Il y sans doute mieux à faire que cette boucle pour recupérer les valeurs
    for i in range(2):
        conso_euro.append(consommation_euro[i].janvier)
        conso_euro.append(consommation_euro[i].fevrier)
        conso_euro.append(consommation_euro[i].mars)
        conso_euro.append(consommation_euro[i].avril)
        conso_euro.append(consommation_euro[i].mai)
        conso_euro.append(consommation_euro[i].juin)
        conso_euro.append(consommation_euro[i].juillet)
        conso_euro.append(consommation_euro[i].aout)
        conso_euro.append(consommation_euro[i].septembre)
        conso_euro.append(consommation_euro[i].octobre)
        conso_euro.append(consommation_euro[i].novembre)
        conso_euro.append(consommation_euro[i].decembre)
        conso_watt.append(consommation_watt[i].janvier)
        conso_watt.append(consommation_watt[i].fevrier)
        conso_watt.append(consommation_watt[i].mars)
        conso_watt.append(consommation_watt[i].avril)
        conso_watt.append(consommation_watt[i].mai)
        conso_watt.append(consommation_watt[i].juin)
        conso_watt.append(consommation_watt[i].juillet)
        conso_watt.append(consommation_watt[i].aout)
        conso_watt.append(consommation_watt[i].septembre)
        conso_watt.append(consommation_watt[i].octobre)
        conso_watt.append(consommation_watt[i].novembre)
        conso_watt.append(consommation_watt[i].decembre)

    ## Facture des années 2016 et 2017
    annual_costs[0] = round(sum(conso_euro[0:12]),2)
    annual_costs[1] = round(sum(conso_euro[12:24]),2)

    ## Données de consommation de 2017 à envoyer au fichier js pour le graphique
    js_data_chart = json.dumps(conso_watt[12:24])

    ## Consommation moyenne sur les mois de janvier, février et décembre.
    winter_average = (conso_watt[0] + conso_watt[1] + conso_watt[11] + conso_watt[12] + conso_watt[13] + conso_watt[23])/6;

    ## Consommation moyenne sur les mois de mai, juin, juillet, aout et septembre
    summer_average = (conso_watt[4] + conso_watt[5] + conso_watt[6] + conso_watt[7] + conso_watt[8]
    + conso_watt[16] + conso_watt[17] + conso_watt[18] + conso_watt[19] + conso_watt[20])/10

    ## Ratio empirique de 1.8 pour déterminer si il y chauffage électrique
    if (winter_average/summer_average) < 1.8:
        is_elec_heating = False

    conso_2016 = sum(conso_watt[0:12])
    conso_2017 = sum(conso_watt[12:24])

    ## Un écart de consommation de 15% entre 2 années consécutives est suspect
    if (conso_2016/conso_2017) > 1.15 or (conso_2017/conso_2016) > 1.15:
        dysfunction_detected = True

    ###################################

    context = {
        "conso_euro": conso_euro,
        "conso_watt": conso_watt,
        "annual_costs": annual_costs,
        "is_elec_heating": is_elec_heating,
        "dysfunction_detected": dysfunction_detected,
        "js_data_chart": js_data_chart
    }
    return render(request, 'dashboard/results.html', context)
