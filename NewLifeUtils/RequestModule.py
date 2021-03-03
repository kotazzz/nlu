import requests

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
