from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()


@app.get("/news")
def get_news(page: int = 1, limit: int = 2):

    url = "https://indianexpress.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title = []

    for item in soup.find_all("a", class_="topblockNews__sidebarLink"):
        title.append(item.text.strip())

    # Pagination
    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "news": title[start:end]
    }
