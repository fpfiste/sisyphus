import os
import tempfile

from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg
from qrbill.bill import QRBill




class QRGenerator():
    def __init__(self, invoice_id, debtor:dict, creditor:dict, amount:float, account:str, language:str):
        self.invoide_id = invoice_id
        self.debtor = debtor
        self.creditor = creditor
        self.amount = amount
        self.account = account
        self.language = language



    def generate(self):

        code = QRBill(
                    account= self.account,
                    creditor= self.creditor,
                    amount= str(self.amount),
                    language=self.language,
                    debtor= self.debtor
                )

        with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
            code.as_svg(temp)
            temp.seek(0)
            drawing = svg2rlg(temp)

            return drawing




