<h1
    align="center"
>
    🕵️‍♂️ Universal Web Scanner & Data Extractor
</h1>


![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458)
![Status](https://img.shields.io/badge/Status-Active-success)


---

A robust Python automation tool designed to perform **Web Reconnaissance**, **SEO Audits**, and **Data Mining** on *any* given URL.

Unlike simple scrapers that break when website layouts change, this tool focuses on extracting universal HTML structures, making it resilient and applicable to 99% of websites.

---

## 🚀 Key Features.

* **🌐 Universal Compatibility:** Works on any URL provided by the user (E-commerce, Blogs, Corporate sites).
* **🤖 Headless Automation:** Runs silently in the background using Selenium (Chrome Driver) for maximum speed.
* **📊 SEO & Meta Data Extraction:** Automatically grabs Page Titles and Meta Descriptions.
* **🔗 Structural Mapping:** Extracts all Headers (H1, H2, H3), Links, and Image sources to map the site's architecture.
* **📂 Dual Export Format:**
    * **JSON:** A structured report for developers and NoSQL databases.
    * **CSV:** A clean spreadsheet of all extracted links ready for Excel/Analysis.


## 🛠️ Tech Stack.

* **Python:** Core logic and scripting.
* **Selenium:** Dynamic web navigation and JavaScript rendering.
* **BeautifulSoup4:** High-speed HTML parsing.
* **Pandas:** Data cleaning, transformation, and CSV export.
* **WebDriver Manager:** Automated Chrome driver management.

---


## ⚙️ Installation & Usage.

### 1. Clone the Repository.
```bash
git clone https://github.com/armando-desouza/universal-web-scraper.git

cd universal-web-scraper
```

### 2. Install Dependencies.

<p
    align="justify"
>
    Make sure you have Python installed, then run:
</p>

```bash
    pip install -r requirements.txt
```

### 3. Run the Scanner.

```bash
    python universal_scraper.py
```

### 4. Enter a Target URL.

<p
    align="justify"
>
    The terminal will prompt you for a URL. Example:
</p>

```bash
    🌐 Cole a URL que deseja raspar: [https://www.python.org](https://www.python.org)
```

### 📂 Outputs Example.

<p
    align="justify"
>
    The tool generates two files automatically:
</p>

1. <code>web_scan_report.json</code> (Structured Data).

```json
    {
        "target_url": "[https://www.python.org](https://www.python.org)",
        "scraped_at": "2024-01-14 10:30:00",
        "page_title": "Welcome to Python.org",
        "meta_description": "The official home of the Python Programming Language",
        "total_links_found": 145,
        "headers_structure": [
            "Get Started",
            "Downloads",
            "Docs"
        ],
        "images_extracted": [
            {"alt": "Python Logo", "src": "/static/img/python-logo.png"}
        ]
    }
```

2. <code>extracted_links.csv</code> (Excel Ready).

<table>
  <thead>
    <tr>
      <th>text</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>About</td>
      <td>/about/</td>
    </tr>
    <tr>
      <td>Downloads</td>
      <td>/downloads/</td>
    </tr>
    <tr>
      <td>Documentation</td>
      <td>/document/</td>
    </tr>
  </tbody>
</table>


### 💡 Why this tool?

<p
    align="justify"
>
    I built this tool to automate the initial phase of <strong>Data Extraction projects</strong>. Before building a custom bot for a specific client, I use this scanner to:
</p>

1. Understand the target website's structure (DOM).

2. Check for anti-bot measures.

2. Audit internal linking strategies.

### 👨‍💻 Author

<p
    align="center"
>
    <strong>Francisco A. de Souza</strong> <i>Python Developer & Data Scientist</i>
</p>

---

### ⚠️ Don't forget the `requirements.txt` file.

<p
    align="justify"
>
    For the installation command to work, make sure the `requirements.txt` file is in the same folder and contains exactly the following:
</p>

```text
    selenium
    beautifulsoup4
    pandas
    webdriver-manager
```