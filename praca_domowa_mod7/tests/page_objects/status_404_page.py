from helpers.support_functions import *

status_info = '/html/body/pre'


def check_status_404(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_info)
    elem = driver_instance.find_element(By.XPATH, status_info)
    value = '404 Not Found'
    if elem.text == value:
        return True
    else:
        return False
