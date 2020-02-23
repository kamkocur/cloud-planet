import pytest
import time


@pytest.mark.usefixtures('setup')
class TestInvoice:

    def test_invoice_sale_receipt(self, setup):
        time.sleep(2)
        self.invoice_feature.accept_cookie()
        self.invoice_feature.go_to_demo_invoice()
        time.sleep(4)
        self.invoice_feature.set_document_type()
        self.invoice_feature.set_product_name('abc')
        self.invoice_feature.create_invoice_click()
        time.sleep(5)
        self.invoice_feature.preview_invoice()
        time.sleep(10)


