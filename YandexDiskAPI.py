import requests

token_ya = 'Ваш токен Яндекс.Диск'

def new_folder():
    url_ya = f'https://cloud-api.yandex.net/v1/disk/'
    headers = {'Authorization': f'OAuth {token_ya}'}
    response = requests.put(f'{url_ya}resources?path=PhotosFromVK', headers=headers)
    return response
