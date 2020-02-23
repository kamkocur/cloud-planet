
class InvoiceFeature:

    def __init__(self, driver):
        self.driver = driver
        self.accept_cookie_button = '.js-cookie-policy-main-accept-button'
        self.check_demo_ing = '[href="https://www.demo.ingksiegowosc.pl"]'
        self.open_demo_ing = '#login-button'
        self.new_invoice = '.main-menu-options-list [href="/invoice/new/sale"]'
        self.set_invoice_see_more = '#content .col-mobile-12.toggle-button span'
        self.sale_receipt_radio_boxes = '.row .options .radio'
        self.input_fields_product = "div.row:nth-child(7) > div:nth-child(1) .form-control.input-search"
        self.product_name_input_field = ".hidden-mobile input[name='name-0']"
        self.create_invoice_button = 'button.btn-primary'
        self.accept_and_save = ".modal-footer .btn.btn-primary"
        self.preview_invoice_css = ".card .flex-1 > a"

    def scroll_and_point_on_element(self):
        self.driver.execute_script("window.scrollTo(0, 700)")

    def accept_cookie(self):
        self.driver.find_element_by_css_selector(self.accept_cookie_button).click()

    def go_to_demo_invoice(self):
        self.driver.find_element_by_css_selector(self.check_demo_ing).click()
        self.driver.find_element_by_css_selector(self.open_demo_ing).click()
        self.driver.find_element_by_css_selector(self.new_invoice).click()

    def set_document_type(self):
        self.driver.find_element_by_css_selector(self.set_invoice_see_more).click()
        document_type = self.driver.find_elements_by_css_selector(self.sale_receipt_radio_boxes)
        document_type[6].click()

    def set_product_name(self, name):
        self.scroll_and_point_on_element()
        input_fields = self.driver.find_elements_by_css_selector(self.input_fields_product)
        input_fields[0].click()
        self.driver.find_element_by_css_selector(self.product_name_input_field).send_keys(name)

    def create_invoice_click(self):
        self.driver.find_element_by_css_selector(self.create_invoice_button).click()
        self.driver.find_element_by_css_selector(self.accept_and_save).click()

    def preview_invoice(self):
        self.driver.find_element_by_css_selector(self.preview_invoice_css).click()
