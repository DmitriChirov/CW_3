import json


def get_data(path):
    '''Get the path to the json file and return data as a list of dictionaries'''

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def select_data(data):
    pass


def sort_data(data):
    pass


def format_data(data):
    pass

