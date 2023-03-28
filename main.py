import visual
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def parser(url):
    """Принимает URL поиск-запроса. Из VISUAL BUTTON_CLICK
    Возврашает Список значений [цена, цена за м2]
    Передает в MAIN CONVERT"""

    """запуск вэб драйвера и ананимность"""
    options = webdriver.ChromeOptions()
    headers = "User-Agent=" + """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
     (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"""
    options.add_argument(headers)
    # фоновый режим
    options.add_argument("--headless")

    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(executable_path="C:\\Users\\oilers\\PycharmProjects\\parserweb\\chrome_driver\\chromedriver.exe", )
    driver = webdriver.Chrome(service=service, options=options)


    """Перебор по странице"""
    list_price = []
    try:
        driver.get(url=url)
        time.sleep(5)

        for element in driver.find_elements(By.CLASS_NAME, "iva-item-priceStep-uq2CQ"):
            time.sleep(3)
            temp = element.text
            list_price.append(temp)
            # print(list_price)
            time.sleep(4)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

    convert(parser_result=list_price)


def convert(parser_result):
    """Принимет необработанный список цен из PARSER
    Убирает все лишнее, переводиn в INT
    Передает в MAIN AVERAGE_PRICE"""

    parser_result = [x.split('\n')[1] for x in parser_result]
    parser_result = [x.split(' ')[0:2] for x in parser_result]

    list_result = []
    for i in parser_result:
        parser_result = "".join(i)
        list_result.append(parser_result)

    list_result = [int(x) for x in list_result]

    average_price(convert_result=list_result)


def average_price(convert_result):
    """Принмает список из MAIN CONVERT
    высчитывает среднию
    Передает в VISUAL RESULT_PRICE"""

    """подсчет средней цены"""
    ave_price = sum(convert_result) // len(convert_result)

    """подсчет средневзвешенной цены"""
    hi_stop = (sum(convert_result) // len(convert_result)) * 1.2
    lo_stop = (sum(convert_result)) // len(convert_result) * 0.8
    list_fair_price = []
    for i in convert_result:
        if i < hi_stop and i > lo_stop:
            list_fair_price.append(i)

    fair_price = sum(list_fair_price) // len(list_fair_price)

    visual.result_price(average=ave_price, fair=fair_price)


def main():
    """1"""
    visual.windows()


if __name__ == "__main__":
    main()
