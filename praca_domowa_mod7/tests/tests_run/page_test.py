import unittest
from selenium import webdriver
from praca_domowa_mod7.config.test_settings import TestSettings
from praca_domowa_mod7.tests.page_objects import basic_auth_page, logged_in_page, key_presses_page, status_codes_page, \
    status_200_page, status_305_page, status_404_page, status_500_page, form_page, date_picker_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_10_basic_auth_correct_credentials(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_correct_credentials_to_basic_auth(self.driver)
        self.assertTrue(logged_in_page.logged_in_message_displayed(self.driver))

    def test_11_basic_auth_incorrect_credentials(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_incorrect_credentials_to_basic_auth(self.driver)
        self.assertTrue(basic_auth_page.invalid_credentials_info_visible(self.driver))

    def test_12_basic_auth_only_username(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_only_username_to_basic_auth(self.driver)
        self.assertTrue(basic_auth_page.invalid_credentials_info_visible(self.driver))

    def test_13_basic_auth_only_password(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_only_password_to_basic_auth(self.driver)
        self.assertTrue(basic_auth_page.invalid_credentials_info_visible(self.driver))

    def test_14_basic_auth_incorrect_password(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_incorrect_password_to_basic_auth(self.driver)
        self.assertTrue(basic_auth_page.invalid_credentials_info_visible(self.driver))

    def test_15_basic_auth_incorrect_username(self):
        basic_auth_page.click_basic_auth_tab(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_incorrect_username_to_basic_auth(self.driver)
        self.assertTrue(basic_auth_page.invalid_credentials_info_visible(self.driver))

    def test_16_key_presses_enter(self):
        key_presses_page.click_key_presses_tab(self.driver)
        self.assertTrue(key_presses_page.key_presses_content_visible(self.driver))
        key_presses_page.press_enter_key(self.driver)
        self.assertTrue(key_presses_page.press_enter_key(self.driver))

    def test_17_status_codes_200(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))
        status_codes_page.click_status_200(self.driver)
        self.assertTrue(status_200_page.check_status_200(self.driver))

    def test_18_status_codes_305(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))
        status_codes_page.click_status_305(self.driver)
        self.assertTrue(status_305_page.check_status_305(self.driver))

    def test_19_status_codes_404(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))
        status_codes_page.click_status_404(self.driver)
        self.assertTrue(status_404_page.check_status_404(self.driver))

    def test_20_status_codes_500(self):
        status_codes_page.click_status_codes_tab(self.driver)
        self.assertTrue(status_codes_page.status_codes_content_visible(self.driver))
        status_codes_page.click_status_500(self.driver)
        self.assertTrue(status_500_page.check_status_500(self.driver))

    def test_21_form_correct_inputs(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        form_page.send_correct_keys_to_form(self.driver)
        self.assertEqual(form_page.get_alert_text(self.driver), 'success')
        form_page.accept_success_message(self.driver)
        self.assertFalse(form_page.is_alert_present(self.driver))

    def test_22_form_submit_empty(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        form_page.submit_empty_form(self.driver)
        self.assertFalse(form_page.is_alert_present(self.driver))

    def test_23_form_submit_only_first_name(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        form_page.submit_only_first_name(self.driver)
        self.assertFalse(form_page.is_alert_present(self.driver))

    def test_24_form_submit_only_last_name(self):
        form_page.click_form_tab(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))
        form_page.submit_only_last_name(self.driver)
        self.assertFalse(form_page.is_alert_present(self.driver))

    def test_25_date_picker_send_value(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.date_picker_content_visible(self.driver))
        date_picker_page.send_correct_value_to_date_picker(self.driver)
        self.assertEqual(date_picker_page.get_selected_date(self.driver), '2020-12-20')

    def test_25_date_picker_send_value_less_than_min(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.date_picker_content_visible(self.driver))
        date_picker_page.send_value_to_date_picker_less_than_min(self.driver)
        self.assertNotEqual(date_picker_page.get_selected_date(self.driver), '2019-12-20')

    def test_25_date_picker_send_value_greater_than_max(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.date_picker_content_visible(self.driver))
        date_picker_page.send_value_to_date_picker_less_than_min(self.driver)
        self.assertNotEqual(date_picker_page.get_selected_date(self.driver), '2022-12-20')


if __name__ == "__main__":
    unittest.main()






