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
    cons_eur = Conso_eur.objects.filter(client_id=client_id)
    cons_wat = Conso_watt.objects.filter(client_id=client_id)

    for i in range(2):
        conso_euro.append(cons_eur[i].janvier)
        conso_euro.append(cons_eur[i].fevrier)
        conso_euro.append(cons_eur[i].mars)
        conso_euro.append(cons_eur[i].avril)
        conso_euro.append(cons_eur[i].mai)
        conso_euro.append(cons_eur[i].juin)
        conso_euro.append(cons_eur[i].juillet)
        conso_euro.append(cons_eur[i].aout)
        conso_euro.append(cons_eur[i].septembre)
        conso_euro.append(cons_eur[i].octobre)
        conso_euro.append(cons_eur[i].novembre)
        conso_euro.append(cons_eur[i].decembre)
        conso_watt.append(cons_wat[i].janvier)
        conso_watt.append(cons_wat[i].fevrier)
        conso_watt.append(cons_wat[i].mars)
        conso_watt.append(cons_wat[i].avril)
        conso_watt.append(cons_wat[i].mai)
        conso_watt.append(cons_wat[i].juin)
        conso_watt.append(cons_wat[i].juillet)
        conso_watt.append(cons_wat[i].aout)
        conso_watt.append(cons_wat[i].septembre)
        conso_watt.append(cons_wat[i].octobre)
        conso_watt.append(cons_wat[i].novembre)
        conso_watt.append(cons_wat[i].decembre)

    annual_costs[0] = round(sum(conso_euro[0:12]),2)
    annual_costs[1] = round(sum(conso_euro[12:24]),2)

    js_data_chart = json.dumps(conso_watt[12:24])

    winter_average = (conso_watt[0] + conso_watt[1] + conso_watt[11] + conso_watt[12] + conso_watt[13] + conso_watt[23])/6;
    summer_average = (conso_watt[4] + conso_watt[5] + conso_watt[6] + conso_watt[7] + conso_watt[8] + conso_watt[16] + conso_watt[17] + conso_watt[18] + conso_watt[19] + conso_watt[20])/10

    if (winter_average/summer_average) < 1.8:
        is_elec_heating = False

    conso_2016 = sum(conso_watt[0:12])
    conso_2017 = sum(conso_watt[12:24])

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
