import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import json
import datetime

class UniversalWebScanner:
    def __init__(self, headless=True):
        # Configurações do Navegador
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        # User-Agent para evitar bloqueios simples
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.scraped_data = {}
        print("🤖 Bot Universal Iniciado!")

    def get_url_from_user(self):
        """Solicita a URL ao usuário"""
        url = input("\n🌐 Cole a URL que deseja raspar (ex: https://www.python.org): ").strip()
        if not url.startswith("http"):
            url = "https://" + url
        return url

    def scan_page(self, url):
        """Acessa a página e extrai dados gerais"""
        print(f"⏳ Acessando: {url} ...")
        self.driver.get(url)
        sleep(3) # Espera carregar scripts dinâmicos
        
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # 1. Extração de Metadados (SEO)
        title = soup.title.string if soup.title else "Sem Título"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"] if meta_desc else "Sem Descrição"

        # 2. Extração de Links (Hrefs)
        links = []
        for link in soup.find_all('a', href=True):
            links.append({
                'text': link.get_text(strip=True),
                'url': link['href']
            })

        # 3. Extração de Imagens
        images = []
        for img in soup.find_all('img', src=True):
            images.append({
                'alt': img.get('alt', 'Sem Alt'),
                'src': img['src']
            })

        # 4. Extração de Cabeçalhos (Estrutura do conteúdo)
        headers = [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]

        # Compilar os dados
        self.scraped_data = {
            'target_url': url,
            'scraped_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'page_title': title,
            'meta_description': description,
            'total_links_found': len(links),
            'total_images_found': len(images),
            'headers_structure': headers[:10], # Mostra apenas os 10 primeiros
            'links_extracted': links, # Salva todos
            'images_extracted': images # Salva todas
        }
        
        print(f"\n✅ Sucesso! Título da página: {title}")
        print(f"🔗 Links encontrados: {len(links)}")
        print(f"🖼️ Imagens encontradas: {len(images)}")

    def save_report(self):
        """Salva os dados em JSON e CSV"""
        if not self.scraped_data:
            print("❌ Nada para salvar.")
            return

        # Salvar JSON completo (Estruturado - NoSQL Style)
        filename_json = "web_scan_report.json"
        with open(filename_json, 'w', encoding='utf-8') as f:
            json.dump(self.scraped_data, f, indent=4, ensure_ascii=False)
        print(f"📄 Relatório JSON salvo em: {filename_json}")

        # Salvar CSV apenas com os Links (Excel Style)
        if self.scraped_data['links_extracted']:
            df = pd.DataFrame(self.scraped_data['links_extracted'])
            filename_csv = "extracted_links.csv"
            df.to_csv(filename_csv, index=False, encoding='utf-8-sig')
            print(f"📊 Planilha de Links salva em: {filename_csv}")

    def close(self):
        self.driver.quit()

# Execução
if __name__ == "__main__":
    bot = UniversalWebScanner(headless=True) # Mude para False se quiser ver o navegador abrindo
    
    try:
        target_url = bot.get_url_from_user()
        bot.scan_page(target_url)
        bot.save_report()
    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")
    finally:
        bot.close()