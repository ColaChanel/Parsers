import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
UserAgent().chrome
# URL страницы, которую мы хотим спарсить
url = f"https://platesmania.com/ru/gallery"

# Отправляем GET-запрос к странице
response = requests.get(url, headers={'User-Agent': UserAgent().chrome})
# for key, value in response.request.headers.items():
#     print(key+": "+value)
# print(response)
# Проверяем успешность запроса
if response.status_code == 200:
    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Находим все теги <img> на странице
    images = soup.find_all("img")
    print(images)
#     # Создаем папку для сохранения изображений, если она не существует
#     if not os.path.exists("plates_images"):
#         os.makedirs("plates_images")
    
#     # Проходимся по каждому найденному изображению
#     for idx, img in enumerate(images):
#         # Получаем ссылку на изображение
#         img_url = img.get("src")
#         # Получаем имя файла из URL
#         filename = os.path.join("plates_images", f"image_{idx}.jpg")
        
#         # Сохраняем изображение
#         with open(filename, "wb") as f:
#             f.write(requests.get(img_url).content)
        
#         print(f"Изображение сохранено: {filename}")
# else:
#     print("Ошибка при получении страницы")