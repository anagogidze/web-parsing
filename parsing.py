import requests, csv, time
from bs4 import BeautifulSoup

file = open('movies.csv', 'w', encoding='utf-8_sig', newline= '\n')
write_obj = csv.writer(file)
write_obj.writerow(['Title','Genre'])

ind = 1

while ind < 6:
    print(f"================================ Page {ind} ===============================")

    url = "https://srulad.com/movies"

    if ind != 1:
        url = f"{url}/page/{ind}"

    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')

    movie_items = soup.find_all(class_="movie-item")

    for item in movie_items:
        title = item.find(class_="card-title").text
        genre = item.find(class_="card-genre").text
        write_obj.writerow([title, genre])
        print(f"{title} {genre}")

    ind += 1
    time.sleep(15)

