from django.http import HttpResponse
from django.template import loader

from .models import EnergyStats


def index(request):
    data_type = request.GET.get('data_type', 1)
    year = request.GET.get('year', 2017)
    asc = request.GET.get('asc', None)

    data_type_list = EnergyStats.get_data_type_list(EnergyStats)

    year_list = EnergyStats.get_year_list(EnergyStats, data_type=data_type)
    if year in year_list:
        year_list.remove(int(year))

    data_type_by_year_list = EnergyStats.get_data_type_by_year(EnergyStats, data_type, year, asc)
    btc_address = "bc1qkyxe9lfjlmc2thwpkknxfvhmws6wdh3u00kupg"

    context = {
        "data_type": data_type,
        "data_type_name": EnergyStats.objects.filter(data_type_id=data_type).first().data_type,
        "year": year,
        "asc": asc,
        "btc_address": btc_address,
        "data_type_list": data_type_list,
        "year_list": year_list,
        "data_type_by_year_list": data_type_by_year_list
    }

    template = loader.get_template('stats/index.html')
    return HttpResponse(template.render(context, request))
