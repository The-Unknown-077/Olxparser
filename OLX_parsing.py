# import requests
# from bs4 import BeautifulSoup


# url = "https://www.olx.uz/list/q-moshina/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')

# quotes = soup.find_all('div', class_ ='css-u2ayx9')
# quotes2 = soup.find_all('div', class_ ='css-13afqrm')

# # print(quotes, quotes2)

# for i in quotes:
#     title = i.find("h6")
#     print(title.text)

# for i in range(1, 4):
       

# url = "https://www.olx.uz/list/q-moshina/"


# response = requests.get(url)
# html_content = response.text

# soup = BeautifulSoup(html_content, 'html.parser')

# car_listings = soup.find_all('div', class_='css-19ucd76')  


# for i, car in enumerate(car_listings[:3]):
#         title = car.find('h6').text.strip()
#         price = car.find('p', class_='css-10b0gli').text.strip()  
#         location = car.find('span', class_='css-17y1s3p').text.strip()

#         print(f"Mashina {i+1}:")
#         print(f"Nomi: {title}")
#         print(f"Narxi: {price}")
#         print(f"Joylashgan joyi: {location}\n")


def my_function():
  print("This is code is pushed to the github repo by me")