import json


def get_data(path):
    '''Get the path to the json file and return data as a list of dictionaries'''

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def select_data(data):
    '''Get transaction data and return a list of successfully completed transactions'''
    selected_data = []

    for transaction in data:
        if 'state' in transaction and transaction['state'] == 'EXECUTED':
            selected_data.append(transaction)

    return selected_data


def sort_data(data):
    '''Get transaction data and return a list of the last five transactions'''
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:5]


def format_data(data):
    pass

