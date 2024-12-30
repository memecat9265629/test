from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the desired FPS value
fps_value = 120  # Change this to 30 or 240 as needed

# Initialize the WebDriver (using Chrome here, you can use other browsers too)
driver = webdriver.Chrome()  # Or webdriver.Firefox()

# Open the target URL
url = "https://gamaverse.com/c/f/g/last-seen-online-1703798580/"
driver.get(url)

# Give the page some time to load
time.sleep(3)  # Adjust this if necessary

# Find the FPS setting button (assuming the FPS control is inside a settings or menu element)
fps_buttons = driver.find_elements(By.XPATH, '//button[contains(text(), "FPS") or contains(text(), "settings")]')

# Click to open the FPS options if needed
for button in fps_buttons:
    if button.text.lower() == f"{fps_value} FPS":
        button.click()
        break

# Allow some time for changes to take effect
time.sleep(5)

# Optionally, verify the FPS setting was applied
fps_applied = driver.find_element(By.XPATH, f'//span[contains(text(), "{fps_value} FPS applied")]')
if fps_applied:
    print(f"FPS set to {fps_value}.")
else:
    print("Failed to apply FPS setting.")

# Close the browser window
driver.quit()
