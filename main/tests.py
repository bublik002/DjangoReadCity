import unittest
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.urls import resolve
from .models import *



class UrlsTest(TestCase):

    def test_main(self):
        response = self.client.get(reverse('api'))
        self.assertEqual(response.statuc_code, 200)

    def test_library(self):
        slug_category_list = [i for i in CategoryModel.objects.all()]
        for slug in slug_category_list:

            response = self.client.get(reverse(f'library/{slug}'))
            self.assertEqual(response.statuc_code, 200)




# def setUpModule():
#     print('Running setUpModule')
#
#
# def tearDownModule():
#     print('Running tearDownModule')
#
#
# class TestMyModule(unittest.TestCase):
#     def test_case_1(self):
#         self.assertEqual(5+5, 10)
#
#     def test_case_2(self):
#         self.assertEqual(1+1, 2)