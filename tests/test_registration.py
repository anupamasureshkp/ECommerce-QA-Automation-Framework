from pages.signup_login_page import SignupLoginPage


def test_new_user_signup_section_is_visible(driver):
    signup_page = SignupLoginPage(driver)

    signup_page.open_homepage()
    signup_page.click_signup_login()

    assert signup_page.is_new_user_signup_visible()