import requests
import os

def get_news():
    api_key = os.getenv('NEWS_API_KEY')
    # Usamos una URL un poco más amplia para asegurar resultados
    url = f'https://newsapi.org/v2/top-headlines?country=ar&apiKey={api_key}'
    
    print("Consultando a NewsAPI...")
    response = requests.get(url)
    data = response.json()
    
    # Esto nos va a mostrar en los logs de GitHub si la API tiró error
    if data.get('status') != 'ok':
        print(f"Error de la API: {data.get('message', 'Error desconocido')}")
        report = f"Error al obtener noticias: {data.get('message')}"
    else:
        articles = data.get('articles', [])
        print(f"Se encontraron {len(articles)} noticias.")
        
        report = "TOP NOTICIAS ARGENTINA DEL DÍA\n"
        report += "==============================\n\n"
        
        if not articles:
            report += "No se encontraron noticias destacadas en este momento."
        else:
            for art in articles[:10]:
                title = art.get('title', 'Sin título')
                url_news = art.get('url', '#')
                report += f"• {title}\n  Link: {url_news}\n\n"
    
    with open("informe_noticias.txt", "w") as f:
        f.write(report)

if __name__ == "__main__":
    get_news()