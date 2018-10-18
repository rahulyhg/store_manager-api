"""Flask API Test doc for store manager"""

from copy import deepcopy

import unittest
import json
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from api import app

BASE_URL_PRODUCTS = 'http://127.0.0.1:5000/storemanager/api/v1.0/products'
BAD_ITEM_URL_PRODUCTS = '{}/16'.format(BASE_URL_PRODUCTS)
GOOD_ITEM_URL_PRODUCTS = '{}/10'.format(BASE_URL_PRODUCTS)

BASE_URL_SALES = 'http://127.0.0.1:5000/storemanager/api/v1.0/sales'
BAD_ITEM_URL_SALES = '{}/4'.format(BASE_URL_SALES)
GOOD_ITEM_URL_SALES = '{}/3'.format(BASE_URL_SALES)

class TestStoreManagerApi(unittest.TestCase):
    """TestStoreManagerApi(unittest.TestCase)--holds all tests we shall perform"""
    def setUp(self):
        """setUp(self)---"""
        self.backup_products = deepcopy(app.PRODUCTS)
        self.backup_sales = deepcopy(app.SALES)
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all_products(self):
        """test_get_all_products(self)---"""
        response_products = self.app.get(BASE_URL_PRODUCTS)
        data_products = json.loads(response_products.get_data())
        print(data_products)
        self.assertEqual(response_products.status_code, 200, msg="Found Products")
        self.assertEqual(len(data_products['products']), 12)

    def test_get_all_sales(self):
        """test_get_all_sales(self)---"""
        response_sales = self.app.get(BASE_URL_SALES)
        data_sales = json.loads(response_sales.get_data())
        print(data_sales)
        self.assertEqual(response_sales.status_code, 200, msg="Found Sales")
        self.assertEqual(len(data_sales['sales']), 3)

    def test_get_one_product(self):
        """test__get_one_product(self)---"""
        response_product = self.app.get(BASE_URL_PRODUCTS)
        data_products = json.loads(response_product.get_data())
        print(data_products)
        self.assertEqual(response_product.status_code, 200, msg="Found Product")
        self.assertEqual(data_products['products'][0]['product_name'], 'Sugar')

    def test_product_not_exist(self):
        """test_product_not_exist(self) --"""
        response_product = self.app.get(BAD_ITEM_URL_PRODUCTS)
        self.assertEqual(response_product.status_code, 404, msg="Didn't find product")

    def test_sale_not_exist(self):
        """test_sale_not_exist(self) --"""
        response_sale = self.app.get(BAD_ITEM_URL_SALES)
        self.assertEqual(response_sale.status_code, 404, msg="Didn't find sale")

    def test_post_product(self):
        """test_post_product(self)"""
        # valid: all required fields, value takes int
        product = {"product_id": 20, "product_name": "Pencil",
                   "category": "Scholastic Materials", "unit_price": 2000,
                   "quantity": "26", "measure": "Boxes"}
        response_product = self.app.post(BASE_URL_PRODUCTS,
                                         data=json.dumps(product),
                                         content_type='application/json')
        self.assertEqual(response_product.status_code, 201, msg="product added")
        data = json.loads(response_product.get_data())
        print(data)
        # cannot add item with same name again
        product = {"product_id": 20, "product_name": "Pencil",
                   "category": "Scholastic Materials", "unit_price": 2000,
                   "quantity": "26", "measure": "Boxes"}
        response_product = self.app.post(BASE_URL_PRODUCTS,
                                         data=json.dumps(product),
                                         content_type='application/json')
        self.assertEqual(response_product.status_code, 400, msg="Item already exists")

    def tearDown(self):
        """tearDown(self)---"""
        # reset app.products to initial state
        app.PRODUCTS = self.backup_products
        app.SALE = self.backup_sales
    
if __name__ == "__main__":
    unittest.main()