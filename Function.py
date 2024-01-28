from DiplomAvetisovNikolay12Mercury import configuration, data
import requests


# Низкоуровневый запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json=body, headers=data.headers)


# Низкоуровневый запрос на получение заказа по номеру трека
def get_order_by_track(track_number):
    # Добаляем в URL GET параметр track
    url = configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + "?t=" + str(track_number)
    return requests.get(url)
