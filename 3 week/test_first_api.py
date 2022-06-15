import pytest
import requests

# Первый апи тест
class TestFirstApi:
    names = [
        ("Dima"),
        ("Mary"),
        ("")
    ]

    @pytest.mark.parametrize("name", names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}
        response = requests.get(url, params=data)

        # проверка что бы статус код = 200 если нет то это ошибка
        assert response.status_code == 200, "Wrong response code"

        #  проверка что наш запрос не пустой, проверка поля/ключа answer что оно в принципе есть
        response_dict = response.json()
        print(response_dict)
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        # проверка что поле/ключ answer не пусто и проверка на корректность заполнения
        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual textin the response is not correct"