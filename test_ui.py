import allure
from Object.object_ui import Object_UI


@allure.title("Проверка добавления в корзину нескольких продуктов")
@allure.feature("READ")
@allure.severity("critical")
def test_add_prod(driver):

    object_ui = Object_UI(driver)
    with allure.step("Вводим имя искомого продукта"):
        object_ui.enter_search("мед с мумие")
    with allure.step("Добавляем первый продукт в корзину"):
        object_ui.add_prod("//div[@class='digi-products']//div[2]//div[1]//div[4]//div[1]//div[1]//button[1]")
    with allure.step("Добавляем второй продукт в корзину"):
        object_ui.add_prod("//div[@id='digi-shield']//div[3]//div[1]//div[4]//div[1]//div[1]//button[1]")
    with allure.step("Открываем корзину"):
        object_ui.enter_to_cart()

    with allure.step("Проверяем количество товара в корзине"):
        assert object_ui.count_prod() == 2


@allure.title("Проверка удаления продукта из  корзины")
@allure.feature("READ")
@allure.severity("critical")
def test_delete_prod(driver):
    object_ui = Object_UI(driver)
    with allure.step("Вводим имя искомого продукта"):
        object_ui.enter_search("мед с мумие")
    with allure.step("Добавляем первый продукт в корзину"):
        object_ui.add_prod("//div[@class='digi-products']//div[2]//div[1]//div[4]//div[1]//div[1]//button[1]")
    with allure.step("Добавляем второй продукт в корзину"):
        object_ui.add_prod("//div[@id='digi-shield']//div[3]//div[1]//div[4]//div[1]//div[1]//button[1]")
    with allure.step("Открываем корзину"):
        object_ui.enter_to_cart()
    with allure.step("Удаляем первый товар из  корзины"):
        object_ui.del_prod()

    with allure.step("Проверяем количество товара в корзине после удаления"):
        assert object_ui.count_prod() == 1
