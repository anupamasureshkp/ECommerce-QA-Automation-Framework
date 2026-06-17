from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupLoginPage:
    SIGNUP_LOGIN_LINK = (By.LINK_TEXT, "Signup / Login")
    NEW_USER_SIGNUP_TEXT = (By.XPATH, "//h2[text()='New User Signup!']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_homepage(self):
        self.driver.get("https://automationexercise.com")

    def close_overlay_if_present(self):
        overlay_selectors = [
            ".fc-dialog-overlay",
            ".fc-consent-root"
        ]

        for selector in overlay_selectors:
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            for element in elements:
                self.driver.execute_script("arguments[0].remove();", element)

    def click_signup_login(self):
        self.close_overlay_if_present()
        signup_login = self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP_LOGIN_LINK)
        )
        signup_login.click()

    def is_new_user_signup_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NEW_USER_SIGNUP_TEXT)
        ).is_displayed()