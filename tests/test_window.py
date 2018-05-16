from pages import home_page
from ui_map import home_page_elements


def test_window():
    home = home_page.HomePage()
    home.wait_for_home_page()
    link = home_page_elements.doc_convert_title_link.element()
    original_window = home.open_link_in_new_window(link)
    home.close_active_window()

    home.browser.driver.switch_to.window(original_window)

test_window()
