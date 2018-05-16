from ui_map import home_page_elements
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from driver import Driver


class HomePage(object):

    def __init__(self, driver=None):
        self.browser = Driver() if not driver else driver

    def wait_for_home_page(self):
        driver = self.browser.driver
        driver.get(self.browser.base_url)
        self.wait_for_element(home_page_elements.logo.element())

    def wait_for_element(self, element):
        driver = self.browser.driver
        ui.WebDriverWait(driver, 15).until(
            lambda driver: element)

    def open_link_in_new_tab(self, element):
        element.send_keys(Keys.CONTROL + Keys.RETURN)
        home_page_elements.page_body.element().send_keys(Keys.CONTROL + Keys.TAB)

    def change_active_window(self, window):
        self.browser.driver.switch_to_window(window)

    def close_current_tab(self):
        self.wait_for_element(home_page_elements.page_body.element())
        home_page_elements.page_body.element().send_keys(Keys.CONTROL + 'w')

    def open_link_in_new_window(self, locator, activate=True):
        known_handles = set(self.browser.driver.window_handles)
        original_handle = self.browser.driver.current_window_handle
        action = ActionChains(self.browser.driver)
        # Open link in new window (shift-click element)
        action.move_to_element(locator).key_down(Keys.SHIFT).click(locator).key_up(
            Keys.SHIFT).perform()

        # Find the new window handle.  ..anyone know a better way?
        new_handles = set(self.browser.driver.window_handles) - known_handles
        if not new_handles or len(new_handles) != 1:
            msg = "Expected one handle, found {}"
            raise RuntimeError(msg.format(len(new_handles)), new_handles)
        new_handle = new_handles.pop()
        if activate:
            self.browser.driver.switch_to.window(new_handle)
        return original_handle

    def close_active_window(self):
        action = ActionChains(self.browser.driver)
        action.key_down(Keys.CONTROL).send_keys('w').perform()

    def select_from_dropdown(self, element, text):
        ui.Select(element).select_by_visible_text(text)
