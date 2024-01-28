import data
import Function


# Аветисов Николай 12 кагорта, Меркурий, "Дипломный проект".
# Тест 1. Проверка создания нового заказа и получения его по треку
def test_create_and_get_order():
    # Создаем новый заказ через API
    response_new_order = Function.post_new_order(data.body)
    # Из JSON ответа получаем номер трека
    track = response_new_order.json()["track"]
    # По номеру трека получаем из API заказ
    response_order = Function.get_order_by_track(track)
    # Проверяем, что статус ответа == 200
    assert response_order.status_code == 200
