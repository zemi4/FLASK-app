import requests

url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
response = requests.get(url).json()


def name_cur():
    result = []
    for i in response:
        x = i['Cur_Name']
        result.append(x)
    return result


def cur():
    result = []
    for i in response:
        x = i['Cur_OfficialRate']
        result.append(x)
    return result

# print(cur())
