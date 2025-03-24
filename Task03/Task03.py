from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Путь к chromedriver
chromedriver_path = 'D:\\Study\\Univercity\\6k2s\\Popov\\chromedriver.exe'  # Укажите путь к вашему chromedriver
service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Базовый URL для тестов
base_url = "https://www.ubisoft.com/en-gb/game/rainbow-six/siege/marketplace?route=buy"

print("Для корректной работы скрипта, пользователь должен быть авторизован на сайте.")




# Тест-кейс 1: Поиск товара по ключевому слову
try:
    driver.get(base_url)
    driver.maximize_window()
    # Время для авторизации
    # time.sleep(60)
    time.sleep(5)
    
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys("MP5 Black Ice")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    
    results = driver.find_elements(By.CSS_SELECTOR, ".marketplace-card")  # предполагаемый класс карточки товара
    assert len(results) > 0, "Результаты поиска не найдены"
    print("Тест-кейс 1 успешно выполнен.")
except Exception as e:
    print(f"Ошибка в тест-кейсе 1: {e}")

# Тест-кейс 2: Просмотр деталей товара
try:
    driver.get(base_url)
    time.sleep(3)
    
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys("MP5 Black Ice")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    
    product_cards = driver.find_elements(By.CSS_SELECTOR, ".marketplace-card")
    assert len(product_cards) > 0, "Товар не найден для детального просмотра"
    product_cards[0].click()
    time.sleep(3)
    
    # Проверяем, открылась ли страница с деталями товара (например, наличие кнопки покупки или описания)
    detail_view = driver.find_elements(By.CSS_SELECTOR, ".item-detail")  # предполагаемый класс детали товара
    assert len(detail_view) > 0, "Детали товара не отображаются"
    print("Тест-кейс 2 успешно выполнен.")
except Exception as e:
    print(f"Ошибка в тест-кейсе 2: {e}")

# Тест-кейс 3: Попытка поиска некорректного ключевого слова
try:
    driver.get(base_url)
    time.sleep(3)
    
    search_box = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys("!@#$%^&*()")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    
    # Ожидаем либо отсутствие результатов, либо сообщение об ошибке
    no_results_message = driver.find_elements(By.XPATH, "//*[contains(text(), 'No results')]")
    assert len(no_results_message) > 0, "Система выполнила поиск по некорректному слову или не вывела сообщение об ошибке"
    print("Тест-кейс 3 успешно выполнен.")
except Exception as e:
    print(f"Ошибка в тест-кейсе 3: {e}")

# Закрытие браузера
driver.quit()
print("Скрипт завершён.")
