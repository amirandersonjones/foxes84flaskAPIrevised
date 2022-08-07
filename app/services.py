#additional classes and functions I wrote to make my routes easier
#must install the requests package in our venv to use it

import requests as r

def getEmpireData():
    response = r.get(
        'https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations')
    if response.status_code == 200:
        data = response.json()
    else:
        return response.status_code
    # start producing our dictionary
    civilizatons = []
    for data in data['civilizations']:
        if data['id']:
            civilizatons.append(
                (data['name'], data['expansion'], data['army_type'], data['team_bonus']))
            # print(data['name'], data['expansion'], data['army_type'], data['team_bonus'])
    return civilizatons
