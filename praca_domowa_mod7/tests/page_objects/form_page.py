from helpers.support_functions import *

form_tab = '//*[@id="form-header"]'
form_content = '//*[@id="form-content"]'
first_name_input = '//*[@id="fname"]'
last_name_input = '//*[@id="lname"]'
submit_button = '//*[@id="formSubmitButton"]'


def click_form_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, form_tab)
    elem.click()


def form_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, form_content)
    return elem.is_displayed()


def send_correct_keys_to_form(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name_input, time_to_wait=1)
    first_name = driver_instance.find_element(By.XPATH, first_name_input)
    last_name = driver_instance.find_element(By.XPATH, last_name_input)
    submit = driver_instance.find_element(By.XPATH, submit_button)
    first_name.send_keys('John')
    last_name.send_keys('Doe')
    submit.click()


def get_alert_text(driver_instance):
    return driver_instance.switch_to.alert.text


def is_alert_present(driver_instance):
    try:
        driver_instance.switch_to.alert
    except NoAlertPresentException:
        return False


def accept_success_message(driver_instance):
    driver_instance.switch_to.alert.accept()


def submit_empty_form(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name_input, time_to_wait=1)
    submit = driver_instance.find_element(By.XPATH, submit_button)
    submit.click()


def submit_only_first_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name_input, time_to_wait=1)
    first_name = driver_instance.find_element(By.XPATH, first_name_input)
    last_name = driver_instance.find_element(By.XPATH, last_name_input)
    submit = driver_instance.find_element(By.XPATH, submit_button)
    first_name.send_keys('John')
    submit.click()


def submit_only_last_name(driver_instance):
    wait_for_visibility_of_element(driver_instance, first_name_input, time_to_wait=1)
    first_name = driver_instance.find_element(By.XPATH, first_name_input)
    last_name = driver_instance.find_element(By.XPATH, last_name_input)
    submit = driver_instance.find_element(By.XPATH, submit_button)
    last_name.send_keys('Doe')
    submit.click()




