# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

ID_JSON = {
    "DE": 1,
    "PA": 2,
    "NJ": 3,
    "GA": 4,
    "CT": 5,
    "MA": 6,
    "MD": 7,
    "SC": 8,
    "NH": 9,
    "VA": 10,
    "NY": 11,
    "NC": 12,
    "RI": 13,
    "VT": 14,
    "KY": 15,
    "TN": 16,
    "OH": 17,
    "LA": 18,
    "IN": 19,
    "MS": 20,
    "IL": 21,
    "AL": 22,
    "ME": 23,
    "MO": 24,
    "AR": 25,
    "MI": 26,
    "FL": 27,
    "TX": 28,
    "IA": 29,
    "WI": 30,
    "CA": 31,
    "MN": 32,
    "OR": 33,
    "KS": 34,
    "WV": 35,
    "NV": 36,
    "NE": 37,
    "CO": 38,
    "ND": 39,
    "SD": 40,
    "MT": 41,
    "WA": 42,
    "ID": 43,
    "WY": 44,
    "UT": 45,
    "OK": 46,
    "NM": 47,
    "AZ": 48,
    "AK": 49,
    "HI": 50,
    "Total Energy Consumption": 1,
    "Energy Consumption Per Capita": 2,
    "Residential Consumption": 3,
    "Commercial Consumption": 4,
    "Industrial Consumption": 5,
    "Transportation Consumption": 6,
    "Electric Power Consumption": 7,
    "NetElectricity Generation": 8,
    "Retail Sales Electricity": 9,
    "Electric Accounts": 10,
    "Electricity Prices": 11,
    "Hydro Electricity Generation": 12,
    "Nuclear Electricity Generation": 13,
    "Solar Electricity Generation": 14,
    "Wind Electricity Generation": 15,
    "Net Interstate Flow Electricity": 16,
    "Total Energy Production": 17,
    "Energy Production Average Price": 18,
    "Total Renewable Production": 19,
    "Population": 20,
    "GDP": 21,
    "Co2 Emissions": 22
}

class Stats(models.Model):
    #id = models.AutoField()
    state_id = models.IntegerField()
    year = models.IntegerField()
    data_type_id = models.IntegerField()
    data_type = models.TextField(max_length=200)
    data_value = models.IntegerField()
    data_unit = models.TextField(max_length=200)
    state = models.TextField(max_length=200)  # This field type is a guess.

    def __str__(self):
        ret_dict = {
            "id": self.id,
            "state_id": self.state_id,
            "year": self.year,
            "data_type_id": self.data_type_id,
            "data_type": self.data_type,
            "data_value": self.data_value,
            "data_unit": self.data_unit,
            "state": self.state
        }
        return str(ret_dict)


    def get_year_list(self, data_type):
        data_type_id = ID_JSON[data_type]
        results = self.objects.filter(data_type_id=data_type_id).distinct().filter(state_id=1).order_by('-year')
        year_list = []
        for i in results:
            year_list.append(i.year)
        return year_list


    def get_data_type_by_year(self, data_type, year, asc):
        data_type_id = ID_JSON[data_type]

        if asc == "True":
            results = self.objects.filter(data_type_id=data_type_id, year=year).order_by('data_value')
            data_type_by_year = []
            rank = 50
            for i in results:
                _dict = {
                    "rank": rank,
                    "state": i.state,
                    "data_value": i.data_value,
                    "data_unit": i.data_unit.replace('_', ' ')
                }
                rank -= 1
                data_type_by_year.append(_dict)
        else:
            results = self.objects.filter(data_type_id=data_type_id, year=year).order_by('-data_value')
            data_type_by_year = []
            rank = 1
            for i in results:
                _dict = {
                    "rank": rank,
                    "state": i.state,
                    "data_value": i.data_value,
                    "data_unit": i.data_unit.replace('_', ' ')
                }
                rank += 1
                data_type_by_year.append(_dict)

        return data_type_by_year

    def get_state_data_by_year(self, state, year):
        state_id = ID_JSON[state]
        results = self.objects.filter(state_id=state_id, year=year).order_by('-data_type_id')
        state_data_by_year = []
        for i in results:
            _dict = {
                "data_type": i.data_type,
                "data_value": i.data_value,
                "data_unit": i.data_unit
            }
            state_data_by_year.append(_dict)
        return state_data_by_year

    def get_data_type_list(self):
        results = self.objects.filter(state_id=1, year=2016).distinct()
        data_type_list = []
        for i in results:
            data_type_list.append(i.data_type)
        return data_type_list

    class Meta:
        managed = False
        db_table = 'stats'
        unique_together = (("state_id", "year", "data_type_id"),)
