# open date -> id date-picker -> click
# date -> class first sc-jSMfEi jMdVvF -> click
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver import Chrome
import datetime as dt
from rich.console import Console

def inline():
    options = Options()
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    options.add_argument("--disable-notifications")
    # options.add_argument("--headless=new")
    options.add_argument('--log-level=1')
    options.add_argument("--start-maximized")
    # options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument(f'--user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    # options.add_experimental_option('excludeSwitches', ['enable-automation'])
    
    chrome = uc.Chrome(options=options)
    # chrome.maximize_window()
    chrome.implicitly_wait(10)
    wait = WebDriverWait(chrome, 10)
    
    chrome.get(f"https://inline.app/booking/-Nvug9oHcq7MmT4O-IR5:inline-live-3/-NvugA02lC3nxcfg2dG4?language=en")
    # test
    # chrome.get(f"https://inline.app/booking/-Lax5xrWRFYPhSt66KBB:inline-live-2a466/-MsYFYKzAnHNSYKGMfeo?language=en")

    # date
    chrome.save_screenshot("date.png")
    date_picker = chrome.find_element(By.XPATH, '//div[@id="date-picker"]')
    # a = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="date-picker"]')))
    chrome.execute_script("arguments[0].scrollIntoView(true);",date_picker)
    # chrome.execute_script("window.scrollBy(0,1000)")
    time.sleep(0.5)
    
    date_picker.click()
    
    time.sleep(0.2)
    defaut_day = chrome.find_element(By.XPATH, '//div[@class="sc-jSMfEi bTLjIu"]')
    next_day = chrome.find_element(By.XPATH, '//div[@class="sc-jSMfEi jMdVvF"]')
    chrome.execute_script("arguments[0].scrollIntoView(true);",defaut_day)
    time.sleep(0.2)
    if(defaut_day):
        try:
            time_slot = chrome.find_elements(By.XPATH, "//button[contains(@class, 'time-slot')]")
            for _ in time_slot:
                try:
                    print(_.text)
                    tmp = wait.until(EC.element_to_be_clickable(_))
                    tmp.click()
                    break
                except:
                    pass
            # confirm
            comfirm1 = chrome.find_element(By.XPATH, "//button[@data-cy='book-now-action-button']") 
            print('c1')
            comfirm1.click()
            user_input(chrome)
            return
        except:
            next_day.click()
    
    # time
    time_slot = chrome.find_elements(By.XPATH, "//button[contains(@class, 'time-slot')]")
    for _ in time_slot:
        try:
            print(_.text)
            tmp = wait.until(EC.element_to_be_clickable(_))
            tmp.click()
            break
        except:
            pass
    # confirm
    confirm2 = chrome.find_element(By.XPATH, "//button[@data-cy='book-now-action-button']") 
    print('c2')
    confirm2.click()
    user_input(chrome)
    
def user_input(chrome):
    # user input
    chrome.execute_script("window.scrollBy(0,400)")
    name = chrome.find_element(By.XPATH, "//input[@id='name']")
    name.send_keys("蔡旻哲")
    chrome.execute_script("window.scrollBy(0,400)")
    name = chrome.find_element(By.XPATH, "//input[@id='phone']")
    name.send_keys("0981519773")
    # submit
    sumbit = chrome.find_element(By.XPATH, "//button[@data-cy='submit']") 
    sumbit.click()

if __name__ == '__main__':
    # inline()
    # exit()
    today = dt.date.today() 
    target_time = today + dt.timedelta(days=1)
    c = Console()
    with c.status('[bold red]running') as _:
        # st_count = time.time()
        while True:
            while(today == target_time):
                st = time.time()
                print("start")
                inline()
                print("end")
                print(time.time()-st)
                target_time = today + dt.timedelta(days=1)
                print(today)
                print(target_time)
            today = dt.date.today() 
            # end = time.time()
            # if(end - st_count > 1):
            #     print(dt.datetime.now())
            #     st_count = end
            