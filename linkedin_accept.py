from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# ====== SETUP CHROME PROFILE (IMPORTANT) ======
options = Options()
options.add_argument("user-data-dir=C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Default")

# Optional: reduce automation detection
options.add_argument("--disable-blink-features=AutomationControlled")

# ====== START DRIVER ======
driver = webdriver.Chrome(options=options)

# ====== OPEN LINKEDIN ======
driver.get("https://www.linkedin.com/")
time.sleep(50)

# ====== GO TO MY NETWORK ======
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
time.sleep(5)

# ====== ACCEPT CONNECTION REQUESTS ======
while True:
    try:
        buttons = driver.find_elements(By.XPATH, "//button[.//span[text()='Accept']]")

        if not buttons:
            print("No more requests found.")
            break

        for btn in buttons:
            try:
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(2)
                print("Accepted one request")
            except:
                pass

        time.sleep(3)

    except Exception as e:
        print("Error:", e)
        break

print("Done ✅")
driver.quit()