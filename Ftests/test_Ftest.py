import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_start_list_and_retrieve_it(self):
		
		self.browser.get(self.live_server_url)
		self.assertIn('Order System', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('CUSTOMERS INFORMATION', headerText)
		
		inpCN = self.browser.find_element_by_id('Cusname')
		inpCT = self.browser.find_element_by_id('Cusnum')
		inpAD = self.browser.find_element_by_id('CusAD')
		btnsy_button = self.browser.find_element_by_id('btnsy')
		
		self.assertEqual(inpCN.get_attribute('placeholder'),'Enter your Name here.')
		self.assertEqual(inpCT.get_attribute('placeholder'),'Enter your Number here.')
		self.assertEqual(inpAD.get_attribute('placeholder'),'Enter your Address here.')


		inpCN.send_keys('Sy Ilano')
		time.sleep(1)

		inpCT.send_keys('09945123678')
		time.sleep(1)

		inpAD.send_keys('Salitran 2 Dasma Cavite')
		time.sleep(1)

		cusX = self.browser.find_element_by_id('cusX')
		cusX.click()

		inihaw_checkbox = self.browser.find_element_by_id('inihaw_id')
		inihaw_checkbox.click()


		btnsy_button.click()
		time.sleep(1)


		table = self.browser.find_element_by_id('registryTable')
		rowData = table.find_element_by_tag_name('td')
		self.assertIn('1: Sy Ilano' , rowData.text)
		
		inpCN = self.browser.find_element_by_id('Cusname')
		inpCT = self.browser.find_element_by_id('Cusnum')
		inpAD = self.browser.find_element_by_id('CusAD')
		btnsy_button = self.browser.find_element_by_id('btnsy')
		
		self.assertEqual(inpCN.get_attribute('placeholder'),'Enter your Name here.')
		self.assertEqual(inpCT.get_attribute('placeholder'),'Enter your Number here.')
		self.assertEqual(inpAD.get_attribute('placeholder'),'Enter your Address here.')


		inpCN.send_keys('Kath Mae')
		time.sleep(1)

		inpCT.send_keys('0977567277')
		time.sleep(1)

		inpAD.send_keys('Bacoor Cavite')
		time.sleep(1)

		cusX = self.browser.find_element_by_id('cusX')
		cusX.click()

		inihaw_checkbox = self.browser.find_element_by_id('inihaw_id')
		inihaw_checkbox.click()


		btnsy_button.click()
		time.sleep(1)


		table = self.browser.find_element_by_id('registryTable')
		rowData = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Sy Ilano, 09945123678, Salitran 2 Dasma Cavite, Male, Inihaw' ,[row.text for row in rowData])

# if __name__=='__main__':
# 	unittest.main(warnings='ignore'