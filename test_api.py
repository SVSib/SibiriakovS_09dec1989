import requests
import allure


base_url = "https://altaivita.ru/"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://altaivita.ru',
    'Referer': 'https://altaivita.ru/?srsltid=AfmBOopLHDyE2VSyABvTx4-JEY5SyRpuRAonN_esDz6RhBm5M7pfYRL9&digiSearch=true&term=%D0%BC%D0%B5%D0%B4%20%D1%81%20%D0%BC%D1%83%D0%BC%D0%B8%D0%B5&params=%7Csort%3DDEFAULT',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Cookie': 'PHPSESSID=sobn71rjoeu8tb9ke1fgptq701; CID=5d04309412a5cd6fe39aedfc68198459; _userGUID=0:m9sge49v:fXoO0bHNWW0ndF4Zu9xzMcQaZESmtAIg; _userGUID=0:m9sge49v:fXoO0bHNWW0ndF4Zu9xzMcQaZESmtAIg; _ym_uid=1745323237111852536; _ym_d=1745323237; _ga=GA1.1.1790324159.1745323237; _ym_isad=2; site_countryID=247; site_country_name=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F; dSesn=a0f5d8a1-c341-3854-2f6c-4a863d06684e; _dvs=0:m9spfy8z:M4WoXq1Ia0L_d2u5PTPq~otrHp9OQCr8; _ga_2JB65Y3D22=GS1.1.1745338281.3.1.1745338438.0.0.0; _ym_visorc=w; digi_uc=|s:174533:5648'
    }

data = 'product_id=7186&LANG_key=ru&S_wh=1&S_CID=5d04309412a5cd6fe39aedfc68198459&S_cur_code=rub&S_koef=1&S_hint_code=&S_customerID='


@allure.title("Проверка добавления продукта в корзину")
@allure.feature("READ")
@allure.severity("critical")
def test_add_prod():
    resp = requests.post(base_url+'engine/cart/add_products_to_cart_from_preview.php', headers=headers, data=data).json()
    requests.post(base_url + 'engine/cart/delete_products_from_cart_preview.php', headers=headers, data=data).json()

    with allure.step("Успешность выполнения запроса"):
        assert resp["status"] == "ok"


@allure.title("Проверка удаления продукта из  корзины")
@allure.feature("READ")
@allure.severity("critical")
def test_del_prod():
    requests.post(base_url + 'engine/cart/add_products_to_cart_from_preview.php', headers=headers, data=data).json()
    resp = requests.post(base_url+'engine/cart/delete_products_from_cart_preview.php', headers=headers, data=data).json()

    with allure.step("Успешность выполнения запроса"):
        assert resp["status"] == "ok"
