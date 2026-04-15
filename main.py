import requests
import os
from datetime import datetime

def get_news():
    api_key = os.getenv('NEWS_API_KEY')
    # Usamos 'everything' con búsqueda de palabra clave para asegurar resultados
    # 'language=es' asegura que vengan en español
    url = f'https://newsapi.org/v2/everything?q=Argentina&language=es&sortBy=publishedAt&pageSize=10&apiKey={api_key}'
    
    print(f"Consultando noticias de Argentina en: {url.replace(api_key, '***')}")
    response = requests.get(url)
    data = response.json()
    
    if data.get('status') != 'ok':
        report = f"Error de la API: {data.get('message')}"
    else:
        articles = data.get('articles', [])
        print(f"Se encontraron {len(articles)} noticias.")
        
        report = f"RESUMEN DE NOTICIAS: ARGENTINA\n"
        report += f"Fecha: {datetime.now().strftime('%d/%m/%Y')}\n"
        report += "==============================\n\n"
        
        if not articles:
            report += "No se encontraron menciones recientes para 'Argentina'."
        else:
            for art in articles:
                # Evitamos artículos que a veces vienen con contenido borrado
                if art['title'] != "[Removed]":
                    report += f"• {art['title']}\n"
                    report += f"  Fuente: {art['source']['name']}\n"
                    report += f"  Link: {art['url']}\n\n"
    
    with open("informe_noticias.txt", "w") as f:
        f.write(report)

if __name__ == "__main__":
    get_news()