from pages import home_page
from ui_map import home_page_elements
# import autoit


def test_file():
    home = home_page.HomePage()
    home.wait_for_home_page()
    home.select_from_dropdown(home_page_elements.doc_convert_dropdown.element(), "Convert to DOC")
    home.wait_for_element(home_page_elements.file_upload.element())
    # autoit.win_wait_active("File Upload", 5)
    # autoit.send(os.path.join(mpath, "1.jpg"))
    # autoit.send("{ENTER}")

test_file()