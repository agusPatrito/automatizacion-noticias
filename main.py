import requests
import os

def get_news():
    api_key = os.getenv('NEWS_API_KEY')
    url = f'https://newsapi.org/v2/top-headlines?country=ar&apiKey={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    articles = data.get('articles', [])
    report = "TOP NOTICIAS ARGENTINA DEL DÍA\n\n"
    
    for art in articles[:10]: # Las primeras 10
        report += f"- {art['title']}\n  Link: {art['url']}\n\n"
    
    with open("informe_noticias.txt", "w") as f:
        f.write(report)

if __name__ == "__main__":
    get_news()