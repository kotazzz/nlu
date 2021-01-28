import requests

history = {}
id_counter = 0


def req_get(url, params={}):
    """
    Type: get
    :return: code of history if response.code != 404
    """
    params_coverted = []
    for param in params:
        params_coverted.append(f"{param}={params[param]}")
    url_out = f'{url}?{"&".join(params_coverted)}'
    resp = requests.get(url_out)
    global id_counter
    history[id_counter] = {"url": url_out, resp: "resp"}
    id_counter += 1
