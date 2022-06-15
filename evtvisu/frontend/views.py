import datetime
import json

from django.shortcuts import render

# Create your views here.
from core.models import EnYear


def dashboard(request):
    print(EnYear.objects)


    dia_data = [{'labels': [], 'name': [], 'data': [[], [], []]},
                {'labels': [], 'name': [], 'data': [[], [], [], []]},
                {'labels': [], 'name': [], 'data': [[], [], []]}
                ]
    """
    for point in data_almemo:
        t = point[0]
        dia_data[2]['labels'].append(t.timestamp() * 1000)
        dia_data[2]['data'][0].append(point[1])
        dia_data[2]['data'][1].append(point[2])
        dia_data[2]['data'][2].append(point[3])
        dia_data[2]['name'] = ['m1_rz_actual', 'm2_rz_actual', 'm1_rl_actual', 'm2_rl_actual']
    """
    context = {
        'data_set': dia_data
    }

    return render(request, 'dashboard.html', context)
