from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SearchPage:
    def __init__(self, driver):
        self.driver = driver  # Инициализация драйвера
        self.search_button = (By.CSS_SELECTOR, "input[value='поиск']")

    #Метод для ввода текста в указанное поле
    def enter_text(self, by, identifier, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, identifier)))
        element.clear()
        element.send_keys(text)

    #Метод для нажатия на кнопку поиска
    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    #Метод выпадающего списка
    def select_dropdown_list(self, by, dropdown_id, option_xpath):
        dropdown = self.driver.find_element(by, dropdown_id)
        dropdown.click()
        option = self.driver.find_element(By.XPATH, option_xpath)
        option.click()

    #Метод ожидания элемента на странице
    def wait_for_element(self, by, value, timeout=8):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    #Метод ожидания появления текста в поле ввода на странице
    def wait_for_element_with_text(self, by, value, text, timeout=15):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element((by, value), text))
        except TimeoutException:
            #Сообщение об ошибке при отсутствии текста в течение заданного времени
            print(f"Элемент с локатором {by} и значением {value},"
                  "содержащий текст '{text}', "
                  "не найден после {timeout} секунд.")
            return False

    #Метод для поиска фильма по названию
    def search_movie_by_title(self, text):
        self.enter_text(By.ID, "find_film", text)
        self.click_search_button()

    #Метод для поиска году выпуска
    def search_by_year(self, year):
        self.enter_text(By.ID, "year", str(year))
        self.click_search_button()

    #Метод для поиска фильма по названию и актеру
    def search_by_actor_and_movie(self, title, actor):
        self.enter_text(By.ID, "find_film", title)
        self.enter_text(By.NAME, "m_act[actor]", actor)
        self.click_search_button()

    #Метод для поиска по стране производства (например, 'США')
    def search_by_country(self, country_value):
        # Выбор страны из выпадающего списка
        self.select_dropdown_list(
            By.ID,
            "country", f"//option[@value='{country_value}' or text()='США']"
            )
        self.driver.find_element(*self.search_button).click()

    #Метод для поиска по жанру (например, 'фантастика')
    def search_by_genre(self, genre_value):
        genre_option = self.driver.find_element(
            By.XPATH,
            f"//input[@value='{genre_value}'] | //option[text()='фантастика']")
        genre_option.click()
        self.click_search_button() 