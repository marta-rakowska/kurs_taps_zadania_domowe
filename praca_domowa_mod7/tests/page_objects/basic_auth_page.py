from helpers.support_functions import *

basic_auth_tab = '//*[@id="basicauth-header"]'
basic_auth_content = '//*[@id="basicauth-content"]'
username_input = '//*[@id="ba_username"]'
password_input = '//*[@id="ba_password"]'
login_button = '//*[@id="content"]/button'
invalid_credentials_info = '//*[@id="loginFormMessage"]'


def click_basic_auth_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, basic_auth_tab)
    elem.click()


def basic_auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, basic_auth_content)
    return elem.is_displayed()


def send_correct_credentials_to_basic_auth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    username = driver_instance.find_element(By.XPATH, username_input)
    password = driver_instance.find_element(By.XPATH, password_input)
    login = driver_instance.find_element(By.XPATH, login_button)
    username.send_keys('admin')
    password.send_keys('admin')
    login.click()


def invalid_credentials_info_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, invalid_credentials_info)
    return elem.is_displayed()


def send_incorrect_credentials_to_basic_auth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    username = driver_instance.find_element(By.XPATH, username_input)
    password = driver_instance.find_element(By.XPATH, password_input)
    login = driver_instance.find_element(By.XPATH, login_button)
    username.send_keys('123456')
    password.send_keys('123456')
    login.click()


def send_only_username_to_basic_auth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    username = driver_instance.find_element(By.XPATH, username_input)
    login = driver_instance.find_element(By.XPATH, login_button)
    username.send_keys('admin')
    login.click()


def send_only_password_to_basic_auth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    password = driver_instance.find_element(By.XPATH, password_input)
    login = driver_instance.find_element(By.XPATH, login_button)
    password.send_keys('admin')
    login.click()


def send_incorrect_password_to_basic_auth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    username = driver_instance.find_element(By.XPATH, username_input)
    password = driver_instance.find_element(By.XPATH, password_input)
    login = driver_instance.find_element(By.XPATH, login_button)
    username.send_keys('admin')
    password.send_keys('123456')
    login.click()


def send_incorrect_username_to_basic_auth(driver_instance):
    wait_for_visibility_of_element(driver_instance, username_input, time_to_wait=1)
    username = driver_instance.find_element(By.XPATH, username_input)
    password = driver_instance.find_element(By.XPATH, password_input)
    login = driver_instance.find_element(By.XPATH, login_button)
    username.send_keys('123456')
    password.send_keys('admin')
    login.click()




