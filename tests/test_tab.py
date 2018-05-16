from pages import home_page
from ui_map import home_page_elements


def test_tab():
    home = home_page.HomePage()
    home.wait_for_home_page()
    # Save the window opener (current window, do not mistaken with tab... not the same)
    main_window = home.browser.driver.current_window_handle
    # Open the link in a new tab by sending key strokes on the element
    home.open_link_in_new_tab(home_page_elements.doc_convert_title_link.element())
    # Put focus on current window which will, in fact, put focus on the current visible tab
    home.change_active_window(main_window)
    # Close current tab
    home.close_current_tab()
    # Put focus on current window which will be the window opener
    home.change_active_window(main_window)

test_tab()