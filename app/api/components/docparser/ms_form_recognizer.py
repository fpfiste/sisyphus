from pprint import pprint

from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import datetime as dt
import dateutil.parser
class FormRecognizer():
    def __init__(self, endpoint, key):
        self.endpoint  = endpoint
        self.key = key
        self.client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))


    def analyse_invoice(self, file, locale='de-CH'):
        response = self.client.begin_analyze_document("prebuilt-invoice", document=file, locale=locale)

        result = response.result()

        data = {
            'invoice_nr' : None,
            'vendor_name' : None,
            'vendor_address' : None,
            'net_total' : 0,
            'tax' : 0,
            'payment_term' : None,
            'invoice_total' : None,
            'items' : '',
            'currency' : ''
        }



        for page in result.documents:
            data['invoice_nr']  = page.fields.get('InvoiceId').value.replace('\n', '')  if page.fields.get('InvoiceId') != None else None
            data['vendor_name'] = page.fields.get('VendorName').value.replace('\n', '') if page.fields.get('VendorName') != None else None
            data['vendor_address'] = page.fields.get('VendorAddressRecipient').content if page.fields.get('VendorAddressRecipient') != None else None
            data['net_total'] = page.fields.get('SubTotal').to_dict() if page.fields.get('SubTotal') != None else None
            data['tax'] = page.fields.get('TotalTax').to_dict() if page.fields.get('TotalTax') != None else None
            data['payment_term'] = page.fields.get('PaymentTerm').content if page.fields.get('PaymentTerm') != None else None
            data['invoice_total'] = page.fields.get('InvoiceTotal').to_dict() if page.fields.get('InvoiceTotal') != None else None
            data['currency'] = page.fields.get('CurrencyCode').content if page.fields.get('CurrencyCode') != None else None
            data['due_date'] = page.fields.get('DueDate').value if page.fields.get('DueDate') != None else None
            data['invoice_date'] = page.fields.get('InvoiceDate').value if page.fields.get('InvoiceDate') != None else None

            if page.fields.get("Items"):
                items = {'item0':None}
                for idx, item in enumerate(page.fields.get("Items").value):
                    print(idx)
                    line = [str(item.value.get("Date").content) if item.value.get("Date") != None else '',
                            str(item.value.get("Description").content) if item.value.get("Description") != None else '',
                            str(item.value.get("Amount").content) if item.value.get("Amount") != None else '',
                            str(item.value.get("UnitPrice").content) if item.value.get("UnitPrice") != None else '',
                            str(item.value.get("TaxRate").content) if item.value.get("TaxRate") != None else '']


                    items['item' + str(idx)] = '||'.join(line)
            data['items'] = items


        return data








