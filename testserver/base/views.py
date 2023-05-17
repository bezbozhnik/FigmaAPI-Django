from django.shortcuts import render
import requests
import json
def startPage(request):
    def get_figma_data(file_id, token, ids):
        headers = {
            'X-Figma-Token': token,
        }
        url = f'https://api.figma.com/v1/images/{file_id}?ids={"-".join(ids)}&format=png'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        return None

    file_id = 'zcT79Jh6OR2g591cx1XoUX'
    ids = ["0", "4"]
    token = 'urtoken'

    figma_data = get_figma_data(file_id, token, ids)
    if figma_data:
        context = {
            'design_url' : figma_data['images'][':'.join(ids)]
        }
        return render(request, 'home.html', context)
    else:
        return None