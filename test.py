from datetime import datetime
from data import data_customer_order_status, data_seasons_problem, data_detecting_change
from index import customer_order_status, seasons_problem, detecting_change
import unittest
import pandas as pd
from pandas._testing import assert_frame_equal


class TestPandas(unittest.TestCase):

    def test_customer_order_status(self):
        result_customer_order_status = pd.DataFrame([
            {
                "order_number": "ORD_1234",
                "status": "SHIPPED"
            },
            {
                "order_number": "ORD_1567",
                "status": "PENDING"
            },
            {
                "order_number": "ORD_7654",
                "status": "CANCELLED"
            },
            {
                "order_number": "ORD_9834",
                "status": "SHIPPED"
            }
        ])
        result = pd.DataFrame(customer_order_status(data_customer_order_status))
        assert_frame_equal(result_customer_order_status, result)
    

    def test_seasons_problem(self):
        result_seasons_problem = pd.DataFrame([
            {
                "ORD_ID": "113-8909896-6940269",
                "SEASON": "Fall"
            },
            {
                "ORD_ID": "114-0291773-7262677",
                "SEASON": "Winter"
            },
            {
                "ORD_ID": "114-0291773-7262697",
                "SEASON": "Fall"
            },
            {
                "ORD_ID": "114-9900513-7761000",
                "SEASON": "Fall"
            },
            {
                "ORD_ID": "112-5230502-8173028",
                "SEASON": "Winter"
            },
            {
                "ORD_ID": "112-7714081-3300254",
                "SEASON": "Spring"
            },
            {
                "ORD_ID": "114-5384551-1465853",
                "SEASON": "Spring"
            },
            {
                "ORD_ID": "114-7232801-4607440",
                "SEASON": "Fall"
            }
        ])
        result = pd.DataFrame(seasons_problem(data_seasons_problem))
        assert_frame_equal(result_seasons_problem, result)

    def test_detecting_change(self):
        result_detecting_change = pd.DataFrame([
            {
                "date": datetime(2020, 1, 2),
                "was_rainy": True
            },
            {
                "date": datetime(2020, 1, 6),
                "was_rainy": True
            },
            {
                "date": datetime(2020, 1, 8),
                "was_rainy": True
            }
        ])
        result = pd.DataFrame(detecting_change(data_detecting_change))
        assert_frame_equal(result_detecting_change, result)









