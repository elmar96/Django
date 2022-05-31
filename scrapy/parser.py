import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://favorit-motors.ru/catalog/stock/"
HOST2 = "https://agromarket.ru/melkaja-fasovka-semjan.html"
HOST3 = "https://sushivesla.kg/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
}


@csrf_exempt
def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("article", class_="b_car_list__item")
    cars = []

    for item in items:
        cars.append(
            {
                "link": item.find("a").get("href"),
                "title": item.find(class_="b_car_list__name").get_text(strip=True),
                # "image": item.find("a").find("span").get("class"),

            }
        )
    return cars


@csrf_exempt
def parser_func():
    html = get_html(HOST)
    if html.status_code == 200:
        plants = []
        for i in range(0, 1):
            plants.extend(get_data(html.text))
        return plants
    else:
        raise Exception("Error is parser function")


@csrf_exempt
def get_data_agro(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="col-md-3")
    agro = []

    for item in items:
        agro.append(
            {
                "link": item.find("a").get("href"),
                "title": item.find("a").find("img").get("alt"),
                "image": item.find("a").find("img").get("src")
            }
        )
    return agro

@csrf_exempt
def parser_func_agro():
    html = get_html(HOST2)
    if html.status_code == 200:
        agro = []
        for i in range(0, 1):
            agro.extend(get_data_agro(html.text))
        return agro
    else:
        raise Exception("Error is parser function agro")

html = get_html(HOST2)
get_data_agro(html.text)


@csrf_exempt
def get_data_eda(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="col-xs-12 col-sm-4 no-margin catalog-item-holder")
    eda = []

    for item in items:
        eda.append(
            {
                "link": item.find("a").get("href"),
                "title": item.find(class_="title").get_text(strip=True),
                "image": item.find("a").find("img").get("src"),
            }
        )
    return eda

@csrf_exempt
def parser_func_eda():
    html = get_html(HOST2)
    if html.status_code == 200:
        eda = []
        for i in range(0, 1):
            eda.extend(get_data_eda(html.text))
        return eda
    else:
        raise Exception("Error is parser function agro")


html = get_html(HOST3)
get_data_eda(html.text)
