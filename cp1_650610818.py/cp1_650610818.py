# cp1_YourStudentCode.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_login_test(headless=False, take_screenshot=True, screenshot_path="result.png"):
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    # webdriver-manager will auto download correct ChromeDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(1)

        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        time.sleep(1)
        msg = driver.find_element(By.ID, "flash").text

        assert "You logged into a secure area!" in msg

        if take_screenshot:
            driver.save_screenshot(screenshot_path)

        print("✅ Login test passed.")

    finally:
        driver.quit()

def run_negative_test(headless=False, take_screenshot=True, screenshot_path="invalid.png"):
    """
    Negative Test:
    Attempt login with wrong credentials.
    Expected message: 'Your username is invalid!'
    """
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(1)

        # Incorrect credentials
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        username.send_keys("baduser")
        password.send_keys("badpassword")

        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_button.click()

        time.sleep(1)

        # Check message
        msg = driver.find_element(By.ID, "flash").text
        assert "Your username is invalid!" in msg, \
            f"Expected invalid login message, but got: {msg}"

        # Save screenshot
        if take_screenshot:
            driver.save_screenshot(screenshot_path)

        print("❌ Negative Test Passed — Invalid credentials detected correctly.")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_login_test(headless=False, take_screenshot=True)
    run_negative_test(headless=False, take_screenshot=True)
