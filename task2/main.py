import config
import requests
import json

headers = {
    'Accept': 'application/json',
    'Authorization': f'OAuth { config.TOKEN}'
}


def create_folder():
    response = requests.put(config.API_BASE_URL + 'resources/',
                 headers=headers, params={'path': 'new_folder'})


if __name__ == '__main__':
    create_folder()
