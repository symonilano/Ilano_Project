from django.test import TestCase
from Ilano_app.views import ilano_view
from .models import CustomerInformations


class HomePageTest(TestCase):
    def test_mainpage_as_seen_client(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'mainpage.html')

    # def test_responding_POST_request(self):
    #     resp = self.client.post('/', data={'CN': 'Cusname','AD': 'CusAD','CT': 'Cusnum', 'CX': 'cusX','CK': 'chkX','CP': 'chkX'})
        
    #     self.assertIn('CN', 'AD','CT', 'CX', 'CK','CP', resp.content.decode())
    #     self.assertTemplateUsed(resp,'mainpage.html')

    def test_save_POST_request(self):
        response = self.client.post('/', {'Cusname': 'Symon',
            'Cusnum':'639090909',
            'CusAD':'Cavite Salitran',
            'cusXs':'male',
            'chxX':'Inihaw'})
        self.assertEqual(CustomerInformations.objects.count(),1)
        SyData = CustomerInformations.objects.first()
        self.assertEqual(SyData.CustomerName, 'Symon')
        self.assertEqual(SyData.CustomerContact, '639090909')
        self.assertEqual(SyData.CustomerAddress, 'Cavite Salitran')
        self.assertEqual(SyData.CustomerGender, 'male')
        self.assertEqual(SyData.CustomerPackageType, 'Inihaw')

    def test_only_saves_items_if_necessary(self):
        self.client.get('/')
        self.assertEqual(CustomerInformations.objects.count(), 0)


class ORMTEST(TestCase):
    def test_saving_retrive(self):
        copy_of_CustomerInformations = CustomerInformations()
        copy_of_CustomerInformations.CustomerName = 'Symon'
        copy_of_CustomerInformations.CustomerContact = '639090909'
        copy_of_CustomerInformations.CustomerAddress = 'Cavite Salitran'
        copy_of_CustomerInformations.CustomerGender = 'male'
        copy_of_CustomerInformations.CustomerPackageType = 'Inihaw'
        copy_of_CustomerInformations.save()

        copy_of_CustomerInformations2 = CustomerInformations()
        copy_of_CustomerInformations2.CustomerName = 'MonSy'
        copy_of_CustomerInformations2.CustomerContact = '639090908'
        copy_of_CustomerInformations2.CustomerAddress = 'Cavite Salitran 1'
        copy_of_CustomerInformations2.CustomerGender = 'Female'
        copy_of_CustomerInformations2.CustomerPackageType = 'Other'
        copy_of_CustomerInformations2.save()

        lists_of_CustomerInfo = CustomerInformations.objects.all()

        self.assertEqual(lists_of_CustomerInfo.count(), 2)

        info1 = lists_of_CustomerInfo[0]
        info2 = lists_of_CustomerInfo[1]

        self.assertEqual(info1.CustomerName, 'Symon')
        self.assertEqual(info1.CustomerContact, '639090909')
        self.assertEqual(info1.CustomerAddress, 'Cavite Salitran')
        self.assertEqual(info1.CustomerGender, 'male')
        self.assertEqual(info1.CustomerPackageType, 'Inihaw')

        self.assertEqual(info2.CustomerName, 'MonSy')
        self.assertEqual(info2.CustomerContact, '639090908')
        self.assertEqual(info2.CustomerAddress, 'Cavite Salitran 1')
        self.assertEqual(info2.CustomerGender, 'Female')
        self.assertEqual(info2.CustomerPackageType, 'Other')

    def test_template_display_list(self):
        CustomerInformations.objects.create(CustomerName='Silver',
            CustomerContact='6399999',
            CustomerAddress='Bacoor',
            CustomerGender='male',
            CustomerPackageType='Other')

        CustomerInformations.objects.create(CustomerName='Kath',
            CustomerContact='6399998',
            CustomerAddress='Quezon',
            CustomerGender='Female',
            CustomerPackageType='Inihaw')
        
        response = self.client.get('/')
        self.assertIn('Silver, 6399999, Bacoor, male, Other', response.content.decode())
        self.assertIn('Kath, 6399998, Quezon, Female, Inihaw', response.content.decode())
        




