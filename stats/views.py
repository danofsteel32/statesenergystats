from django.http import HttpResponse
from django.template import loader
import re

from .models import Stats

def index(request):
	data_type = request.GET.get('data_type', 'totalEnergyConsumption')
	state = request.GET.get('state', None)
	year = request.GET.get('year', 2017)
	asc = request.GET.get('asc', None)

	data_type_list = Stats.get_data_type_list(Stats)
	data_type_list.remove(data_type)

	year_list = Stats.get_year_list(Stats, data_type=data_type)
	if year in year_list:
		year_list.remove(int(year))

	data_type_by_year_list = Stats.get_data_type_by_year(Stats, data_type, year, asc)
	btc_address = "bc1qkyxe9lfjlmc2thwpkknxfvhmws6wdh3u00kupg"

	context = {
		"data_type": data_type,
		"data_type_name": re.sub(r"(\w)([A-Z])", r"\1 \2", data_type).title(),
		"year": year,
		"asc": asc,
		"btc_address": btc_address,
		"data_type_list": data_type_list,
		"year_list": year_list,
		"data_type_by_year_list": data_type_by_year_list
	}

	template = loader.get_template('stats/index.html')
	return HttpResponse(template.render(context, request))