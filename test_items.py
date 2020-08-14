link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    add_to_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    browser.implicitly_wait(10)
    assert add_to_basket, "Кнопка не найдена"