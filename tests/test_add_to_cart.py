from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


class TestAdNabuStore:

    def setup_method(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        self.wait = WebDriverWait(self.driver, 30)

    def teardown_method(self):

        self.driver.quit()

    def test_search_and_add_to_cart(self):

        driver = self.driver
        wait = self.wait

        try:

            # Open Website
            driver.get(
                "https://adnabu-store-assignment1.myshopify.com"
            )

            # Enter Password
            password_input = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, "password")
                )
            )

            password_input.send_keys("AdNabuQA")

            # Click Enter
            enter_button = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[contains(.,'Enter')]"
                    )
                )
            )

            enter_button.click()

            # Wait Homepage
            wait.until(
                EC.presence_of_element_located(
                    (By.TAG_NAME, "body")
                )
            )

            time.sleep(5)

            # Click Search Icon
            search_icon = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//summary[contains(@aria-label,'Search')]"
                    )
                )
            )

            search_icon.click()

            # Search Product
            search_input = wait.until(
                EC.visibility_of_element_located(
                    (By.NAME, "q")
                )
            )

            search_input.send_keys(
                "Multi-location Snowboard"
            )

            search_input.send_keys(Keys.ENTER)

            time.sleep(5)

            # Get Product Link
            product = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//a[contains(@href,'multi-location-snowboard')]"
                    )
                )
            )

            # Extract Product URL
            product_url = product.get_attribute("href")

            print("Product URL:", product_url)

            # Open Product URL Directly
            driver.get(product_url)

            time.sleep(5)

            # Wait For Add To Cart
            add_to_cart = wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[@name='add']"
                    )
                )
            )

            # Scroll To Button
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                add_to_cart
            )

            time.sleep(2)

            # Click Add To Cart
            driver.execute_script(
                "arguments[0].click();",
                add_to_cart
            )

            time.sleep(5)

            # Verify Product Added
            body_text = driver.find_element(
                By.TAG_NAME,
                "body"
            ).text

            assert "Multi-location Snowboard" in body_text

            print("Product added successfully")

        except Exception as e:

            driver.save_screenshot(
                "screenshots/failure.png"
            )

            print("Test Failed")
            print(e)

            raise