from utils.web_element import WebElement

logo = WebElement(id='logo')
page_body = WebElement(tag_name='body')
doc_convert_title_link = WebElement(link_text="Document converter")
doc_convert_dropdown = WebElement(id="box_selection_document")
doc_convert_ok_button = WebElement(name="submit_button")

file_upload = WebElement(id='file')
