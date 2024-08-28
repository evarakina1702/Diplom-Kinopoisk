import pytest
import requests 
import allure
from config_base_api_ui import url_api, HEADERS

@allure.feature('API Responses')
@pytest.mark.parametrize("endpoint, expected_status", [
    ("/search?page=1&limit=1&query=Король Лев", 200),
    ("/535341", 200),
    ("?type=movie&year=2001", 200),
    ("/?year=1850", 400),
    ("/?rating.kp=-5", 400),
    ("/?status=анонс", 400)
])

def test_api_responses(endpoint, expected_status):
    
    """Универсальный тест для проверки статуса ответа API по различным endpoint'ам"""

    with allure.step(f"Отправка GET запроса на {endpoint}"):
        response = requests.get(f"{url_api}{endpoint}", headers=HEADERS)

    with allure.step(f"Проверка, что статус ответа равен {expected_status}"):
        assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"

@allure.feature('Search movie by title')
def test_search_movie_by_title():

    """Тест API на поиск фильма по названию"""

    with allure.step("Отправка GET запроса на https://api.kinopoisk.dev/v1.4/movie//search?page=1&limit=1&query=Король Лев"):
        response = requests.get(f"{url_api}/search?page=1&limit=1&query=Король Лев", headers=HEADERS)

    with allure.step("Проверка, что статус ответа равен 200"):
        assert response.status_code == 200

@allure.feature('Search movie by ID')
def test_search_movie_by_id():

    """Тест API на поиск фильма по ID"""

    with allure.step("Отправка GET запроса на https://api.kinopoisk.dev/v1.4/movie/535341"):
        response = requests.get(f"{url_api}/535341", headers=HEADERS)

    with allure.step("Проверка, что статус ответа равен 200"):
        assert response.status_code == 200


@allure.feature('Search for a movie by year of release')
def test_search_release():
    
    """Тест API на поиск фильма по году выпуска"""

    with allure.step("Отправка GET запроса на https://api.kinopoisk.dev/v1.4/movie/?type=movie&year=2001"):
        response = requests.get(f"{url_api}?type=movie&year=2001", headers=HEADERS)

    with allure.step("Проверка, что статус ответа равен 200"):
        assert response.status_code == 200

@allure.feature('Search for a movie with a non-existent release year')
def test_search_year_negative():
    
    """Тест API на поиск фильма с несуществующим годом выпуска"""

    with allure.step("Отправка GET запроса на https://api.kinopoisk.dev/v1.4/movie/?year=1850"):
        response = requests.get(f"{url_api}/?year=1850", headers=HEADERS)

    with allure.step("Проверка, что статус ответа равен 400"):
        assert response.status_code == 400

@allure.feature('Search for a movie with negative ratings')
def test_search_negative_rating():
   
    """Тест API на поиск фильма с отрицательным рейтингом"""

    with allure.step("Отправка GET запроса на https://api.kinopoisk.dev/v1.4/movie/?rating.kp=-5"):
        response = requests.get(f"{url_api}/?rating.kp=-5", headers=HEADERS)

    with allure.step("Проверка, что статус ответа равен 400"):
        assert response.status_code == 400

@allure.feature('Search for movie with invalid status')
def test_search_invalid_status():

    """Тест API на поиск фильма с некорректным статусом"""

    with allure.step("Отправка GET запроса на https://api.kinopoisk.dev/v1.4/movie/?status=анонс"):
        response = requests.get(f"{url_api}/?status=анонс", headers=HEADERS)

    with allure.step("Проверка, что статус ответа равен 400"):
        assert response.status_code == 400