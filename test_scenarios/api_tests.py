import json
import allure
import pytest
from automation_api_module.pets import PetsModule
from automation_api_module.api_base_scenario import APIBaseScenario


class TestPetAPI:

    @pytest.fixture
    def pets_module(self):
        """
        Fixture to create an instance of PetsModule.
        """
        return PetsModule()

    @allure.title("Test API: Get Pet based on valid Id ")
    def test_get_pet_details_based_on_valid_id(self, pets_module):
        """
        Test the successful retrieval of pet details.

        Steps:
        1. Create an instance of PetsModule.
        2. Call the get_pet_data method with a valid pet ID.
        3. Assert that the response status code is 200.
        """
        pet_id = 1  # Change this to an existing pet ID in your pet store
        response = pets_module.get_pet_data(pet_id)
        assert response.status_code == 200, f'Response status expected to be {200} instead got {response.status_code}'

    @allure.title("Test API: Get Pet based on incorrect Id ")
    def test_get_pet_details_based_on_invalid_id(self, pets_module):
        """
        Test the behavior when an invalid pet ID is provided.

        Steps:
        1. Create an instance of PetsModule.
        2. Call the get_pet_data method with an invalid pet ID.
        3. Assert that the response status code is 404.
        4. Assert that the response type is 'error'.
        5. Assert that the response message is 'Pet not found'.
        """
        pet_id = 9999  # Assuming this ID does not exist in your pet store
        response = pets_module.get_pet_data(pet_id)
        response = response.__dict__
        assert response['status_code'] == 404, f'Response status expected to be {404} instead got {response["status_code"]}'
        assert json.loads(response['_content'].decode('utf-8'))['type'] == 'error', \
            f'Unexpected Response type data, got {json.loads(response["_content"].decode("utf-8"))["type"]}'
        assert json.loads(response['_content'].decode('utf-8'))['message'] == 'Pet not found', \
            f'Unexpected Response message data, got {json.loads(response["_content"].decode("utf-8"))["message"]}'

    @allure.title("Test API: Get Pet based on string Id ")
    def test_get_pet_details_based_on_str_id(self, pets_module):
        """
        Test the behavior when an invalid input (non-integer) pet ID is provided.

        Steps:
        1. Create an instance of PetsModule.
        2. Call the get_pet_data method with a non-integer pet ID.
        3. Assert that the response status code is 400.
        4. Assert that the response type is 'unknown'.
        5. Assert that the response message contains the expected error message.
        """
        pet_id = "AutomationTestingProject"  # Assuming an invalid input (non-integer) pet ID
        response = pets_module.get_pet_data(pet_id)
        response = response.__dict__
        assert response['status_code'] == 404, \
            f'Response status expected to be {404} instead got {response["status_code"]}'
        assert json.loads(response['_content'].decode('utf-8'))['type'] == 'unknown', \
            f'Unexpected Response type data, got {json.loads(response["_content"].decode("utf-8"))["type"]}'
        assert json.loads(response['_content'].decode('utf-8'))['message'] == \
               f"java.lang.NumberFormatException: For input string: \"{pet_id}\""
        f'Unexpected Response message data, got {json.loads(response["_content"].decode("utf-8"))["message"]}'

    @allure.title("Test API: Add new pet - success response ")
    def test_add_new_pet_success(self, pets_module):
        response = pets_module.simple_add_new_pet()
        assert response.status_code == 200, f'Response status expected to be {200} instead got {response.status_code}'

    @allure.title("Test API: Add new Pet based on invalid data ")
    def test_add_new_pet_based_on_invalid_data(self, pets_module):
        """
        Test adding a new pet with invalid data.

        Steps:
        1. Prepare invalid pet data JSON.
        2. Send a POST request to add the pet.
        3. Assert that the response status code is 400 (Bad Request).
        """
        invalid_data = 123445
        response = pets_module.add_new_pet(self, photoUrls=invalid_data)
        assert response.status_code == 404, f'Response status expected to be {404} instead got {response.status_code}'

    @allure.title("Test API: Add new Pet based on missing required fields ")
    def test_add_new_pet_missing_required_fields(self, pets_module):
        """
        Test adding a new pet with missing required fields.

        Steps:
        1. Prepare pet data JSON missing required fields.
        2. Send a POST request to add the pet.
        3. Assert that the response status code is 400 (Bad Request).
        """
        pet_data_missing_fields = {"name": "dog"}
        response = pets_module.add_new_pet(self, pet_data_missing_fields)
        assert response.status_code == 400
        f'Response status expected to be {400} instead got {response.status_code}'

    @allure.title("Test API: E2E Add and assert pet details after retrieving ")
    def test_e2e_add_and_retrieve_pets(self, pets_module):
        """
        Test adding and retrieving pets, validating the response.

        Steps:
        1. Generate pet data.
        2. Add a new pet.
        3. Assert successful addition.
        4. Retrieve the added pet.
        5. Assert successful retrieval.
        6. Validate pet's details match the added data.
        """

        add_new_pet = APIBaseScenario().get_pets_from_file()
        data = json.dumps(add_new_pet)
        # Parse JSON string into a dictionary
        json_data = json.loads(data)
        response = pets_module.add_new_pet(pet_id=json_data['id'],
                                           category=json_data['category'],
                                           name=json_data['name'],
                                           photoUrls=json_data['photoUrls'],
                                           tags=json_data['tags'],
                                           status=json_data['status'])
        assert response.status_code == 200, f'Response status expected to be {200} instead got {response.status_code}'

        # retrieve the created pet and validate response is as expected
        get_added_pet = json_data['id']
        response = pets_module.get_pet_data(get_added_pet)
        assert response.status_code == 200, f'Response status expected to be {200} instead got {response.status_code}'
        response = json.loads(response.content)
        assert response['id'] == json_data['id'], f'Added pat id does not match to the retrieved pat, instead got :{response["id"]}'
        assert response['category'] == json_data['category'], f'Added pat category does not match to the retrieved pat instead got :{response["category"]}'
        assert response['photoUrls'] == json_data['photoUrls'], f'Added pat photoUrls does not match to the retrieved pat instead got :{response["photoUrls"]}'
        assert response['tags'] == json_data['tags'], f'Added pat tags does not match to the retrieved pat instead got :{response["tags"]}'
        assert response['status'] == json_data['status'], f'Added pat status does not match to the retrieved pat instead got :{response["status"]}'
