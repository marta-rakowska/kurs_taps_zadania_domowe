from helpers.support_functions import *

status_codes_tab = '//*[@id="statuscodes-header"]'
status_codes_content = '//*[@id="statuscodes-content"]'
elem_200 = '//*[@id="200siteAnchor"]'
elem_305 = '//*[@id="305siteAnchor"]'
elem_404 = '//*[@id="404siteAnchor"]'
elem_500 = '//*[@id="500siteAnchor"]'


def click_status_codes_tab(driver_instance):
    elem = driver_instance.find_element(By.XPATH, status_codes_tab)
    elem.click()


def status_codes_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, status_codes_content)
    return elem.is_displayed()


def click_status_200(driver_instance):
    wait_for_visibility_of_element(driver_instance, elem_200, time_to_wait=1)
    elem = driver_instance.find_element(By.XPATH, elem_200)
    elem.click()


def click_status_305(driver_instance):
    wait_for_visibility_of_element(driver_instance, elem_305, time_to_wait=1)
    elem = driver_instance.find_element(By.XPATH, elem_305)
    elem.click()


def click_status_404(driver_instance):
    wait_for_visibility_of_element(driver_instance, elem_404, time_to_wait=1)
    elem = driver_instance.find_element(By.XPATH, elem_404)
    elem.click()


def click_status_500(driver_instance):
    wait_for_visibility_of_element(driver_instance, elem_500, time_to_wait=1)
    elem = driver_instance.find_element(By.XPATH, elem_500)
    elem.click()



