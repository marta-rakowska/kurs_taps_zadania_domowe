from helpers.support_functions import *
import datetime

date_picker_tab = '//*[@id="datepicker-header"]'
date_picker_content = '//*[@id="datepicker-content"]'
date_picker = '//*[@id="start"]'


def click_date_picker_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, date_picker_tab)
    elem.click()


def date_picker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, date_picker_content)
    return elem.is_displayed()


def send_correct_value_to_date_picker(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker)
    elem = driver_instance.find_element(By.XPATH, date_picker)
    elem.send_keys('2020-12-22')


def get_selected_date(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker)
    elem = driver_instance.find_element(By.XPATH, date_picker)
    return elem.get_attribute("value")


def send_value_to_date_picker_less_than_min(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker)
    elem = driver_instance.find_element(By.XPATH, date_picker)
    elem.send_keys('2019-12-22')


def send_value_to_date_picker_greater_than_max(driver_instance):
    wait_for_visibility_of_element(driver_instance, date_picker)
    elem = driver_instance.find_element(By.XPATH, date_picker)
    elem.send_keys('2022-12-22')

