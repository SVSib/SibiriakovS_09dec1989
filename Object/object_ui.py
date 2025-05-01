from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Object_UI:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://altaivita.ru/")

    def enter_search(self, product):
        """
                Поиск товара
        """

        search = self._driver.find_element(By.CSS_SELECTOR, "input[placeholder='Поиск товаров']")
        search.send_keys(product)
        self._driver.find_element(
            By.CSS_SELECTOR, "div[class='header__search'] div[class='searchpro__field-button js-searchpro__field-button']").click()
        self._driver.implicitly_wait(5)

    def add_prod(self, locator):
        """
                Добавление товара в корзину
        """

        self._driver.find_element(By.XPATH, locator).click()

    def del_prod(self):
        """
                Удаление товара из корзины
        """

        delete_prod = self._driver.find_element(By.CSS_SELECTOR, "div[class='basket__delete js-item-delete']")
        delete_prod.click()
        WebDriverWait(self._driver, 10).until_not(EC.visibility_of_element_located(
        (By.XPATH, "div[class='basket__delete js-item-delete']")))

    def enter_to_cart(self):
        """
                Открытие корзины
        """

        self._driver.find_element(
            By.CSS_SELECTOR, ".header__basket-link.ga_link_to_cart.grid_container_mobile_menu.pdd_cart").click()
        cart_enter = self._driver.find_element(
            By.XPATH, "//div[@class='header__right']//a[@class='dropdown-go-over link-gray ga_link_to_cart'][contains(text(),'Перейти в корзину')]")
        cart_enter.click()
        self._driver.implicitly_wait(10)
        webdriver.ActionChains(self._driver).send_keys(Keys.ESCAPE).perform()
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='basket__delete js-item-delete']//i[@class='fal fa-times']")))


    def count_prod(self):
        """
                Длина списка товаров в корзине
        """

        count = len(self._driver.find_elements(By.CSS_SELECTOR, ".basket__item.js-cart-item"))
        return count
