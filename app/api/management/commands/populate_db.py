from django.core.management.base import BaseCommand, CommandError
import api.models as models
from faker import Faker
import random




class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    faker = Faker()

    def populate_currencies(self):
        for i in range(5):
            curr = models.Currencies()
            curr.currency = self.faker.currency_name()
            curr.currency_account_nr = self.faker.iban()
            curr.currency_abbreviation = self.faker.currency_code()

            curr.save()

        print(curr)

    def populate_absence_codes(self):
    def populate_companies(self):

        rec_status = models.SysRecStates.objects.all().values_list('pk', flat=True)

        for i in range(100):
            comp = models.Companies()
            comp.company_name = self.faker.company()
            comp.company_street =  self.faker.street_name()
            comp.company_zipcode =  self.faker.postcode()
            comp.company_internal_alias = comp.company_name
            comp.fk_sys_rec_status = random.choice(rec_status)
            comp.company_email =  self.faker.company_email()
            comp.is_customer = random.choice([0,1])
            comp.is_supplier = random.choice([0,1])
            comp.is_subcontractor = random.choice([0,1])


        print(comp)




    def handle(self, *args, **options):
        self.populate_currencies()
        self.populate_companies()
        mod = list(map(models.__dict__.get, models.__all__))
        print(mod[2].__dict__.keys())


