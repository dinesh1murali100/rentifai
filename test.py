from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div[1]/ul/li[7]"))
    )
    button.click()
    print("Button clicked successfully!")
except Exception as e:
    print("Error: Button not found!", e)

input("Click on enter key")

# Print the title of the page
print(driver.title)

# Close the browser
# driver.quit()
