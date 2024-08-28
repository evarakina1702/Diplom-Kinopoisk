import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from SearchPageKinopoisk import SearchPage
from config_base_api_ui import url_ui

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def search_page(driver: WebDriver):
    driver.get(url_ui)
    return SearchPage(driver)

@allure.feature('Search movie by title')
def test_search_by_title(search_page: SearchPage):

    """Тест UI на поиск фильма по названию"""

   
    with allure.step("Поиск контента по названию '1+1'"):
        search_page.search_movie_by_title("1+1")

    with allure.step("Проверка, что найденный контент соответствует фильму 'Intouchables'"):
        is_content_found = search_page.wait_for_element_with_text(By.CLASS_NAME, "gray", "Intouchables, 112 мин")
        assert is_content_found, "Expected to find content 'Intouchables, 112 мин'"

@allure.feature('Search by year')
def test_search_by_year(search_page: SearchPage):
    
    """Тест UI на поиск по году"""

    with allure.step("Поиск по году 2011"):
        search_page.search_by_year(2011)

    with allure.step("Проверка, что найденный контент соответствует году 2011"):
        year_element = search_page.wait_for_element(By.CLASS_NAME, "year")
        assert year_element.text == "2011", f"Expected year to be 2011, but got {year_element.text}"

@allure.feature('Search by actor and movie title')
def test_search_by_actor_movie_title(search_page: SearchPage):
   
    """Тест UI на поиск фильма по названию фильма и актеру"""

    with allure.step("Поиск фильма по названию '1+1' и актеру 'Омар Си'"):
        search_page.search_by_actor_and_movie("1+1", "Омар Си")

    with allure.step("Проверка, что найденный фильм соответствует фильму 'Intouchables' с актером 'Омар Си'"):
        is_content_found = search_page.wait_for_element_with_text(By.CLASS_NAME, "gray", "Intouchables, 112 мин")
        assert is_content_found, "Expected to find content 'Intouchables, 112 мин''"

@allure.feature('Search by country')
def test_search_by_country(search_page: SearchPage):

    """Тест UI на поиск по стране"""

    with allure.step("Поиск контента по стране 'США'"):
        search_page.search_by_country("США")

    with allure.step("Проверка, что найденный контент соответствует стране 'США'"):
        country_element = search_page.wait_for_element(By.CLASS_NAME, "text-blue")
        assert country_element.text == "«США»", f"Expected country to be '«США»', but got {country_element.text}"

@allure.feature('Search by genre')
def test_search_by_genre(search_page: SearchPage):
    
    """Тест UI на поиск по жанру"""

    with allure.step("Поиск по жанру 'фантастика'"):
        search_page.search_by_genre("фантастика")

    with allure.step("Проверка, что найденный контент относится к жанру 'фантастика'"):
        is_genre_found = search_page.wait_for_element_with_text(By.XPATH, "//span[@class='gray' and contains(., 'фантастика')]", "фантастика")
        assert is_genre_found, "Expected to find content with genre 'фантастика'"
