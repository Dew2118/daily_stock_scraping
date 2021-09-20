import pandas as pd
from html_table_parser import HTMLTableParser
from datetime import date
import os
from pathlib import Path
from selenium import webdriver

#change
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://siamchart.com/stock/")
cwd = f'file:///{Path.cwd()}/Thai Stock Chart List [ข้อมูลหุ้นไทยทั้งหมด พร้อมกราฟหุ้นและเครื่องมือช่วยวิเคราะห์หุ้น และคัดกรองหุ้น] - SiamChart.html'
COL_LIST = ["Name",
            "No.",
            "Links",
            "Sign",
            "Last",
            "Chg%",
            "Volume",
            "Value (k)",
            "MCap (M)",
            "P/E",
            "P/BV",
            "D/E",
            "DPS",
            "EPS",
            "ROA%",
            "ROE%",
            "NPM%",
            "Yield%",
            "FFloat%",
            "MG%",
            "Magic1",
            "Magic2",
            "PEG",
            "CG"]

def extract_date(html):
    start = html.find("<div class=\"column\" style=\"font-weight: bold; color:#FFFF00; background:#008800; width:100%;\">") + len("<div class=\"column\" style=\"font-weight: bold; color:#FFFF00; background:#008800; width:100%;\">")
    end = html.find("</div>", start)
    print(end)
    txt = html[start:end]
    date = txt[1:11]
    print(txt)
    return date

htmlSource = driver.page_source
p = HTMLTableParser()
p.feed(htmlSource)
df = pd.DataFrame(columns=COL_LIST)
tt = p.tables[2]
# skip first line in tt
temp_data = [dict(zip(COL_LIST,list)) for list in tt[1:]]
df = df.append(temp_data, ignore_index=True)
date = extract_date(htmlSource)
# df.to_csv(f'{Path.cwd()}\\Siamchart\\{date}_siam_chart.csv', header=False, index=False)
df.to_csv('C:/Users/kavin/Documents/daily_stock_scraping/Siamchart/{date}_siam_chart.csv')
driver.quit()