import requests
import main
import config


class Test:

    def test_rest_api(self):
        main.create_folder()
        response = requests.get(config.API_BASE_URL + 'resources/',
                                headers=main.headers, params={'path': 'new_folder'})
        assert response.status_code == 200
