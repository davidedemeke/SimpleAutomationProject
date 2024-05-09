import json
import requests


class PetsModule:

    def __init__(self):
        self._headers = None
        self.request = requests.Session()  # Initialize request session
        self._base_url = None
        self.api_key = None

    def base_url(self):
        if self._base_url is None:
            with open('../utiles/qa-config.json', "r") as configuration:
                data = json.load(configuration)
                self._base_url = data['project_base_url']['config']['my_project']['base_url']
        return self._base_url

    def headers(self):
        if self._headers is None:
            headers = {
                "Content-Type": "application/json"
            }
            # You may add more headers here if needed
            self._headers = headers
        return self._headers

    def get_pet_data(self, pet_id):
        path = f"/pet/{pet_id}"
        body = None
        return self.request.get(self.base_url() + path, headers=self.headers())

    def add_new_pet(self, pet_id=None, category=None, name=None, photoUrls=None, tags=None, status=None):
        """Add new pet based on data"""
        if pet_id is None:
            pet_id = 900
        if name is None:
            pet_id = 'TestName'
        if status is None:
            pet_id = 'status'
        if photoUrls is None:
            photoUrls = "https://example.com/photo.jpg"
        if tags is None:
            tags = {"id": 0, "name": "string"}
        if category is None:
            category = {"id": 0, "name": "string"}
        body = {
            "id": pet_id,
            "category": category,
            "name": name,
            "photoUrls": [photoUrls],
            "tags": [tags],
            "status": status
        }
        path = "/pet"
        return self.request.post(self.base_url() + path, json=body, headers=self.headers())

    def simple_add_new_pet(self):
        body = {
            "id": 123,
            "category": {
                "id": 0,
                "name": "PetNmaeTest"
            },
            "name": "zzzz",
            "photoUrls": [
                "www.google.com"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "PetNmaeTest_Tag"
                }
            ],
            "status": "available"
        }
        path = "/pet"
        return self.request.post(self.base_url() + path, json=body, headers=self.headers())
