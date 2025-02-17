from helpers.support_functions import *
from selenium.webdriver.common.keys import Keys

key_pressed_tab = '//*[@id="keypresses-header"]'
key_presses_content = '//*[@id="keypresses-content"]'
key_presses_input = '//*[@id="target"]'
message = '//*[@id="keyPressResult"]'


def click_key_presses_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, key_pressed_tab)
    elem.click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, key_presses_content)
    return elem.is_displayed()


def press_enter_key(driver_instance):
    wait_for_visibility_of_element(driver_instance, key_presses_input, time_to_wait=1)
    elem = driver_instance.find_element(By.XPATH, key_presses_input)
    pressed_key_info = driver_instance.find_element(By.XPATH, message)
    elem.send_keys(Keys.ENTER)
    value = 'You entered: ENTER'
    if pressed_key_info.text == value:
        return True
    else:
        return False



