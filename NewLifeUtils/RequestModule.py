import requests
import json

history = []


def req_get(url, params={}):
    """
    Type: get
    :return: code of history if response.code != 404
    """
    params_coverted = [f"{param}={params[param]}" for param in params]
    url_out = f'{url}?{"&".join(params_coverted)}'
    resp = requests.get(url_out)
    global id_counter
    history.append({"url": url_out, resp: "resp"})



def vk_simple_get(method, args, gid, token, ver):
    url = f'https://api.vk.com/method/{method}?'
    for arg in args:
        url += f'{arg}={args[arg]}&'
    response = json.loads(requests.get(url + f'group_id={gid}&access_token={token}&v={ver}').text)
    return response
