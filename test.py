from threading import Thread
import time
import pyautogui
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Prevents the browser from closing


# Initialize WebDriver (For Chrome)
driver = webdriver.Chrome()


# Open a website
driver.get("https://rentifaidev.coinbitwallet.com/")

driver.maximize_window()


driver.implicitly_wait(10)

# Wait for the login button to appear
try:
    # Wait until the Login button appears (max 10 sec)
    login_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Log In')]")))
    login_element.click()
    print("Login button clicked successfully!")
except Exception as e:
    print("Error: Element not found!", e)

username = driver.find_element(By.CSS_SELECTOR, "#app > div:nth-child(1) > div.fixed.top-0.left-0.right-0.z-50.bg-white > header > div.fixed.inset-0.z-50.overflow-hidden.transition-opacity.duration-300.opacity-100.pointer-events-auto > div > div.bg-white.rounded-lg.absolute.top-0.left-1\/2.transform.-translate-x-1\/2.translate-y-0.border-2.border-\[\#A64AC9\].w-full > div.bg-white.p-4.rounded-lg.flex.flex-col.items-center > div.mb-10 > input")
username.send_keys("muralikrish61@gmail.com")

pwd = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/header/div[2]/div/div[2]/div[2]/div[2]/input")
pwd.send_keys("Dineshmurali110598#")

login_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sign In')]")))
login_element.click()

# Click the "List Car" button using CSS Selector
try:
    list_car_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div.flex.relative.items-start.justify-center.h-full > div.lg\\:bg-\\[\\#ececec\\].max-lg\\:w-full.w-9\\/12.h-full.overflow-y-scroll > div > div > div > div > div.flex.flex-wrap.items-center.gap-4.justify-between.pb-\\[15px\\].max-sm\\:pb-\\[3px\\].max-sm\\:mt-2 > div.flex.items-center.border-\\[1px\\].border-\\[\\#707070\\].rounded-\\[29px\\].bg-white.max-sm\\:mt-\\[5px\\] > div.font-bold.text-\\[\\#A64AC9\\].max-sm\\:py-\\[5px\\].max-sm\\:px-\\[8px\\].py-\\[12px\\].px-\\[22px\\].inline-block.false.cursor-pointer"))
    )
    list_car_button.click()
    print("List Car button clicked successfully!")
except Exception as e:
    print("Error: List Car button not found!", e)


"""
list_car_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]')
list_car_button.click()
"""

# Wait and click the button using full XPath
try:
    rent_a_car = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/ul/li[7]"))
    )
    rent_a_car.click()
    print("Button clicked successfully!")
except Exception as e:
    print("Error: Button not found!", e)

list_now = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div/div[1]/ul/li[7]')

list_now.click()

enter_plate_number = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[1]/input')
enter_plate_number.send_keys("PCE34")

verify_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[2]/button')
verify_button.click()

enter_vehicle_type = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[4]/div[2]/div/input')
enter_vehicle_type.send_keys("Sedan")

petrol_type_dropdown_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[6]/div/div/select')
petrol_type_dd_class = Select(petrol_type_dropdown_element)
petrol_type_dd_class.select_by_index(1)

next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Next')]")))
next_button.click()

type_km_driven = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[4]/div/input")))
type_km_driven.send_keys("233")

next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Next')]")))
next_button.click()

type_cpp_day = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[1]/div/input")))
type_cpp_day.send_keys("34")

type_location = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/div/input")
type_location.send_keys("NZ")

location_select = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]")
location_select.click()

type_value_of_car = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div[3]/div/input")
type_value_of_car.send_keys("833")

next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Next')]")))
next_button.click()

select_to_date = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[6]/div[6]/span")))
select_to_date.click()

select_from_date = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[5]/div[3]/span")))
select_from_date.click()

next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Next')]")))
next_button.click()

Submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Submit')]")))
Submit_button.click()

confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Confirm & Next')]")))
confirm_button.click()

# Remove overlay (if blocking the click)
#driver.execute_script("document.querySelector('.fixed.inset-0').remove();")

#Wait for overlay to disappear
WebDriverWait(driver,10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "fixed.inset-0")))


interior_image_upload_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div/label')))
interior_image_upload_button.click()

time.sleep(2)

image_path = r"C:\Users\DELL\Downloads\shared image (6).jpg"
pyautogui.write(image_path)
pyautogui.press("enter")

time.sleep(10)

