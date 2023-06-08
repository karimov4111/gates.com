import time
import sys
import csv 
import pandas
from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
scraped_deta = []
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.gates.com/us/en/knowledge-center/resource-library/product-catalogs.html"
driver.get(url)
time.sleep(3)
button = driver.find_element(By.XPATH, '//div[@class="parts-nav navigation gor-nav tray"]/div/ul/li/a[@class="button button-default part-search parent vin-modal-trigger"]').click()
time.sleep(2)
vhile_class1 = driver.find_elements(By.XPATH, '//select[@name="equipment-clazz"]/option')
for clas in range(11)[1:]:
    vhile_class = driver.find_element(By.NAME, 'equipment-clazz').click()
    time.sleep(1)
    vhile_class1 = driver.find_elements(By.XPATH, '//select[@name="equipment-clazz"]/option')[clas].click()
    bir = vhile_class1 = driver.find_elements(By.XPATH, '//select[@name="equipment-clazz"]/option')[clas].text.strip()
    time.sleep(1)
    vhile_typ1 = driver.find_elements(By.XPATH, '//select[@name="vehicle-type"]/option')
    len_typ = len(vhile_typ1)
    vhile_stop = len_typ-1
    for typ in range(len_typ)[1:vhile_stop]:
        vhile_typ = driver.find_element(By.NAME, 'vehicle-type').click()
        time.sleep(1)
        vhile_typ1 = driver.find_elements(By.XPATH, '//select[@name="vehicle-type"]/option')[typ].click()
        time.sleep(1)
        ikki = driver.find_elements(By.XPATH, '//select[@name="vehicle-type"]/option')[typ].text.strip()

        year = driver.find_element(By.NAME, 'year').click()
        time.sleep(1)
        year1 = driver.find_elements(By.XPATH, '//select[@name="year"]/option')[1].click()
        time.sleep(1)
        uch = driver.find_elements(By.XPATH, '//select[@name="year"]/option')[1].text.strip()
        if str(uch) == "All":
            uch = '<All Applicable Years>'
        make1 = driver.find_elements(By.XPATH, '//select[@name="make"]/option')
        make1_len = len(make1)
        make_stop = make1_len-1
        for mak in range(make1_len)[1:make_stop]:
            make = driver.find_element(By.NAME, 'make').click()
            time.sleep(1)
            make1 = driver.find_elements(By.XPATH, '//select[@name="make"]/option')[mak].click()
            time.sleep(1)
            tort = driver.find_elements(By.XPATH, '//select[@name="make"]/option')[mak].text.strip()
            model1 = driver.find_elements(By.XPATH, '//select[@name="model"]/option')
            model_len = len(model1)
            model_stop = model_len-1
            for mod in range(model_len)[1:model_stop]:
                model = driver.find_element(By.NAME, 'model').click()
                time.sleep(1)
                model1 = driver.find_elements(By.XPATH, '//select[@name="model"]/option')[mod].click()
                time.sleep(1)
                besh = driver.find_elements(By.XPATH, '//select[@name="model"]/option')[mod].text.strip()
                engine1 = driver.find_elements(By.XPATH, '//select[@name="engine"]/option')
                engine_len = len(engine1)
                engine_stop = engine_len-1
                for eng in range(engine_len)[1:engine_stop]:
                    engine = driver.find_element(By.NAME, 'engine').click()
                    time.sleep(1)
                    engine1 = driver.find_elements(By.XPATH, '//select[@name="engine"]/option')[eng].click()
                    time.sleep(1)
                    olti = driver.find_elements(By.XPATH, '//select[@name="engine"]/option')[eng].text.strip()
                    print(olti)
                    if str(olti) == "All":
                        olti = '<All Applicable Engines>'
                    cookies = {
                        '__cf_bm': 'edzRXUwpll4wdHp5wBAdKVPQ21zMtMy0DwWrLSntVbw-1685432590-0-AcSbkS8y4P3b/+j0Xzf1MmgA/Fe56hHkTVg/LYUVMWMgGUcD0Bb2bj2L4Cf8y1CWkNHYtE3eW2vmrsTGxvXNdLg=',
                        'regionSelection': 'us:en',
                        '_ga': 'GA1.2.718952104.1685432593',
                        '_gid': 'GA1.2.380710921.1685432593',
                        '_gcl_au': '1.1.1575898531.1685432593',
                        'AMCVS_C2A9A7DB586C15A50A495DB8%40AdobeOrg': '1',
                        'userIp': '10.38.0.107',
                        'AMCV_C2A9A7DB586C15A50A495DB8%40AdobeOrg': '179643557%7CMCIDTS%7C19508%7CMCMID%7C30285823021793225054438239269373583233%7CMCAAMLH-1686037393%7C3%7CMCAAMB-1686037393%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1685439793s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
                        's_cc': 'true',
                        '_mkto_trk': 'id:439-CTA-171&token:_mch-gates.com-1685432593915-83545',
                        '_fbp': 'fb.1.1685432594045.1986109935',
                        'ln_or': 'eyI0MzAzNTMwIjoiZCJ9',
                        's_tp': '2379',
                        's_ppv': 'us%253Aen%253Asearch%253Avehicle%2520search%2520result%2C99%2C26%2C2348',
                        's_sq': 'gc.global%252Cgc.usa.prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dus%25253Aen%25253Asearch%25253Avehicle%252520search%252520result%2526link%253DAccept%252520Cookies%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dus%25253Aen%25253Asearch%25253Avehicle%252520search%252520result%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257BOptanon.TriggerGoogleAnalyticsEvent%252528%252527OneTrustCookieConsent%252527%25252C%252527BannerAcceptCook%2526oidt%253D2%2526ot%253DSUBMIT',
                        'OptanonAlertBoxClosed': '2023-05-30T07:46:28.724Z',
                        'OptanonConsent': 'isIABGlobal=false&datestamp=Tue+May+30+2023+12%3A46%3A28+GMT%2B0500+(Uzbekistan+Standard+Time)&version=6.1.0&landingPath=NotLandingPage&groups=0_83053%3A1%2C1%3A1%2C0_83064%3A1%2C0_81648%3A1%2C2%3A1%2C0_81651%3A1%2C0_83062%3A1%2C0_83055%3A1%2C3%3A1%2C0_83063%3A1%2C4%3A1%2C0_81653%3A1%2C0_83060%3A1%2C0_81654%3A1%2C0_83056%3A1%2C0_81647%3A1%2C0_81644%3A1%2C0_83273%3A1%2C0_83057%3A1%2C0_81641%3A1%2C0_83059%3A1%2C0_83206%3A1&AwaitingReconsent=false',
                        'AWSALB': 'q4x1Xbu7xSWaWZseb7wsTYf8siSIEddkdI+/9axtF8v70vALf9++le9aWrGZPaxzfouRAhkEoYynpSZpzSu18PIcV9tFoIyHSbyFWaw7I6vAg3RgGcaty6Zx9nhk',
                        'AWSALBCORS': 'q4x1Xbu7xSWaWZseb7wsTYf8siSIEddkdI+/9axtF8v70vALf9++le9aWrGZPaxzfouRAhkEoYynpSZpzSu18PIcV9tFoIyHSbyFWaw7I6vAg3RgGcaty6Zx9nhk',
                    }

                    headers = {
                        'authority': 'www.gates.com',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'uz-UZ,uz;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
                        'cache-control': 'max-age=0',
                        # 'cookie': '__cf_bm=edzRXUwpll4wdHp5wBAdKVPQ21zMtMy0DwWrLSntVbw-1685432590-0-AcSbkS8y4P3b/+j0Xzf1MmgA/Fe56hHkTVg/LYUVMWMgGUcD0Bb2bj2L4Cf8y1CWkNHYtE3eW2vmrsTGxvXNdLg=; regionSelection=us:en; _ga=GA1.2.718952104.1685432593; _gid=GA1.2.380710921.1685432593; _gcl_au=1.1.1575898531.1685432593; AMCVS_C2A9A7DB586C15A50A495DB8%40AdobeOrg=1; userIp=10.38.0.107; AMCV_C2A9A7DB586C15A50A495DB8%40AdobeOrg=179643557%7CMCIDTS%7C19508%7CMCMID%7C30285823021793225054438239269373583233%7CMCAAMLH-1686037393%7C3%7CMCAAMB-1686037393%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1685439793s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; s_cc=true; _mkto_trk=id:439-CTA-171&token:_mch-gates.com-1685432593915-83545; _fbp=fb.1.1685432594045.1986109935; ln_or=eyI0MzAzNTMwIjoiZCJ9; s_tp=2379; s_ppv=us%253Aen%253Asearch%253Avehicle%2520search%2520result%2C99%2C26%2C2348; s_sq=gc.global%252Cgc.usa.prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dus%25253Aen%25253Asearch%25253Avehicle%252520search%252520result%2526link%253DAccept%252520Cookies%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dus%25253Aen%25253Asearch%25253Avehicle%252520search%252520result%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257BOptanon.TriggerGoogleAnalyticsEvent%252528%252527OneTrustCookieConsent%252527%25252C%252527BannerAcceptCook%2526oidt%253D2%2526ot%253DSUBMIT; OptanonAlertBoxClosed=2023-05-30T07:46:28.724Z; OptanonConsent=isIABGlobal=false&datestamp=Tue+May+30+2023+12%3A46%3A28+GMT%2B0500+(Uzbekistan+Standard+Time)&version=6.1.0&landingPath=NotLandingPage&groups=0_83053%3A1%2C1%3A1%2C0_83064%3A1%2C0_81648%3A1%2C2%3A1%2C0_81651%3A1%2C0_83062%3A1%2C0_83055%3A1%2C3%3A1%2C0_83063%3A1%2C4%3A1%2C0_81653%3A1%2C0_83060%3A1%2C0_81654%3A1%2C0_83056%3A1%2C0_81647%3A1%2C0_81644%3A1%2C0_83273%3A1%2C0_83057%3A1%2C0_81641%3A1%2C0_83059%3A1%2C0_83206%3A1&AwaitingReconsent=false; AWSALB=q4x1Xbu7xSWaWZseb7wsTYf8siSIEddkdI+/9axtF8v70vALf9++le9aWrGZPaxzfouRAhkEoYynpSZpzSu18PIcV9tFoIyHSbyFWaw7I6vAg3RgGcaty6Zx9nhk; AWSALBCORS=q4x1Xbu7xSWaWZseb7wsTYf8siSIEddkdI+/9axtF8v70vALf9++le9aWrGZPaxzfouRAhkEoYynpSZpzSu18PIcV9tFoIyHSbyFWaw7I6vAg3RgGcaty6Zx9nhk',
                        'referer': 'https://www.gates.com/us/en/knowledge-center/resource-library/product-catalogs.html',
                        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    }

                    params = {
                        'equipment-clazz': str(bir),
                        'vehicle-type': str(ikki),
                        'year': str(uch),
                        'make': str(tort),
                        'model': str(besh),
                        'engine': str(olti),
                    }

                    response = requests.get(
                        'https://www.gates.com/us/en/ymm/search/vehicle/result.html',
                        params=params,
                        cookies=cookies,
                        headers=headers,
                    )
                    
                    soup = BeautifulSoup(response.content, 'html.parser')
                    try:
                        category = soup.find_all("h2", class_="nested-accordion__title")[0].text.strip()
                    except:
                        category = ""
                    try:
                        subcategory = soup.find_all("li", class_="nested-accordion__item nested-accordion__item--level2")[0].find("a", class_="nested-accordion__header nested-accordion__header--level2 accordion-header gor-active").text.strip()
                    except:
                        subcategory = ""
                    print(subcategory)
                    application = ""
                    product_type = ""
                    part = ""
                    comments = ""
                    divs = soup.find("div", class_="accordion-content-inner nested-accordion__content-inner").find("tbody").find_all("tr")
                    for div in divs:
                        application += f'{div.find_all("td")[0].text.strip()} \n' 
                        product_type += f'{div.find_all("td")[1].text.strip()} \n'
                        part += f'{div.find_all("td")[2].text.strip()} \n'
                        comments += f'{div.find_all("td")[3].text.strip()} \n'

                    scraped_deta.append(
                        {
                            "vhicle_class": bir,
                            "vhicle_deta": ikki,
                            "year": uch,
                            "make": tort,
                            "model": besh,
                            "engine": olti,
                            "category": category if category else "Na" ,
                            "subcategory": subcategory if subcategory else "Na" ,
                            "application": application if application else "Na" ,
                            "product_type": product_type if product_type else "Na" ,
                            "part": part if part else "Na" ,
                            "comments": comments if comments else "Na"
                        }
                    )
                    if len(scraped_deta)== 100:
                        break
                    else:
                        print(len(scraped_deta))



df = pandas.DataFrame(data=scraped_deta)
df.to_csv("sample.csv", index=False)