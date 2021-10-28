import requests
import unittest


class TestStringMethods(unittest.TestCase):

    def test_result(self):
        url = "http://3.121.127.141/resultq"
        self.assertEqual(requests.get(url).status_code, 200)


    def test_create(self):
        url = "http://3.121.127.141/create_record"
        data = {"create_name": "test", "create_desc": "test", "create_number": 1, "create_price": 1, "create_rare": "N"}
        self.assertEqual(requests.post(url, data=data).status_code, 200)


    def test_get_n(self):
        url = "http://3.121.127.141/n_record"
        data = {"send_n": 1}
        self.assertEqual(requests.post(url, data=data).status_code, 200)

    def test_get_id(self):
        url = "http://3.121.127.141/id_record"
        global id
        data = {"send_id": 5}
        self.assertEqual(requests.post(url, data=data).status_code, 200)


if __name__ == '__main__':
    unittest.main()

