import pandas as pd
year = []
month = []
day = []
weather = []
high_temp = []
low_temp = []

def weatherfunc(area):
    from selenium import webdriver
    import re
    import time
    driver = webdriver.Chrome('C:/work/chromedriver')
    driver.get("https://www.accuweather.com/")
    time.sleep(1)
    driver.find_element_by_css_selector("div.searchbar-content > form > input").send_keys(area)
    driver.find_element_by_css_selector("div.searchbar-content > svg.icon-search.search-icon").click()

    time.sleep(2)
    try:
        driver.find_element_by_css_selector("div.page-column-1 > div:nth-child(1) > div > a:nth-child(1)").click()
    except:
        driver.refresh()
        driver.find_element_by_css_selector("div.page-column-1 > div:nth-child(1) > div > a:nth-child(1)").click()

    time.sleep(2)
    try:
        driver.find_element_by_css_selector("div.subnav-items > a[data-gaid='monthly']").click()
#         body > div > div.page-subnav > div > div.subnav-items > a:nth-child(6)
    except:
        driver.refresh()
        driver.find_element_by_css_selector("div.page-column-1 > div:nth-child(1) > div > a:nth-child(1)").click()
        try:
            driver.find_element_by_css_selector("div.subnav-items > a[data-gaid='monthly']").click()
        except:
            driver.find_element_by_css_selector("div.subnav-items > a[data-gaid='monthly']").click()
    
    time.sleep(2)
    ydata = int(''.join(re.findall("\d+",driver.find_elements_by_css_selector("div.monthly-dropdowns > div:nth-child(2) > div.map-dropdown-toggle > h2")[0].text)))
    mdata = int(''.join(re.findall("\d+",driver.find_elements_by_css_selector("div.monthly-dropdowns > div:nth-child(1) > div.map-dropdown-toggle > h2")[0].text)))
    month_data = driver.find_elements_by_css_selector("a.monthly-daypanel:not(.is-past)")
    for i in range(len(month_data)):
        ddata = int(month_data[i].find_element_by_css_selector("div.date").text)
        if i > 0 and ddata < day[-1]:
            break
        wdata = int(''.join(re.findall("\d+", month_data[i].find_element_by_css_selector("img.weather-icon") .get_attribute('data-src'))))
        high = int(''.join(re.findall("\d+", month_data[i].find_element_by_css_selector("div.high").text)))
        low = int(''.join(re.findall("\d+", month_data[i].find_element_by_css_selector("div.low").text)))
        year.append(ydata)
        month.append(mdata)
        day.append(ddata)
        weather.append(wdata)
        high_temp.append(high)
        low_temp.append(low)
#     print(len(year),len(month),len(day),len(weather),len(high_temp),len(low_temp))   
    weather_data = {'year':year, 'month':month, 'day':day, 'weather':weather, 'high_temp':high_temp, 'low_temp':low_temp}
    wdf = pd.DataFrame(weather_data)
    print(wdf)
    driver.quit()