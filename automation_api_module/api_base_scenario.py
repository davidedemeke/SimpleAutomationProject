import json


class APIBaseScenario:
    """
    Utility class for cross functions that can be used by importing this class from anywhere.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_pets_from_file():
        with open('../utiles/list_of_pets.json', "r") as data:
            list_of_pets = json.load(data)
        return list_of_pets
