from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as playwright:
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()

    try:
        # Открываем страницу
        page.goto('https://www.saucedemo.com/')
        page.wait_for_load_state('load')

        # Логинимся
        page.wait_for_selector("#user-name")
        page.fill(selector='#user-name', value='standard_user')
        page.fill(selector="#password", value='secret_sauce')
        page.click(selector='#login-button')

        # Ждем загрузки инвентаря
        page.wait_for_url('https://www.saucedemo.com/inventory.html')
        page.wait_for_selector(".btn.btn_primary.btn_small.btn_inventory")

        # Проверяем и добавляем товар в корзину
        page.click(selector='[id="add-to-cart-sauce-labs-backpack"]')

        # Переходим в корзину и оформляем заказ
        page.click('[data-test="shopping-cart-link"]')
        page.click('[id="checkout"]')

        # Заполняем информацию о покупателе
        page.type(selector='#first-name', text='first_name', delay=100)
        page.type(selector='#last-name', text='last_name', delay=100)
        page.type(selector='input[name="postalCode"]', text='311933', delay=100)

        page.click('[id = "continue"]')
        page.click('[id="finish"]')

        page.wait_for_url('https://www.saucedemo.com/checkout-complete.html')

        page.click('[id = "react-burger-menu-btn"]', delay=100)

        page.click('[id = "logout_sidebar_link"]', delay=100)

        time.sleep(2)

    finally:
        # Закрываем браузер
        browser.close()