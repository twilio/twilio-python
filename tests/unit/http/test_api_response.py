import unittest
from twilio.base.api_response import ApiResponse


class TestApiResponse(unittest.TestCase):
    def test_initialization(self):
        """Test ApiResponse initialization"""
        data = {'sid': 'AC123', 'friendly_name': 'Test'}
        response = ApiResponse(
            data=data,
            status_code=200,
            headers={'Content-Type': 'application/json'}
        )

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_repr(self):
        """Test string representation"""
        response = ApiResponse(data={'test': 'data'}, status_code=201, headers={})
        repr_str = repr(response)
        self.assertIn('201', repr_str)
        self.assertIn('dict', repr_str)

    def test_str(self):
        """Test human-readable string representation"""
        response = ApiResponse(data={'test': 'data'}, status_code=200, headers={})
        str_repr = str(response)
        self.assertIn('200', str_repr)
        self.assertIn('dict', str_repr)

    def test_with_list_data(self):
        """Test ApiResponse with list data"""
        data = [{'sid': 'AC1'}, {'sid': 'AC2'}]
        response = ApiResponse(data=data, status_code=200, headers={})
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, 200)

    def test_with_boolean_data(self):
        """Test ApiResponse with boolean data (delete operations)"""
        response = ApiResponse(data=True, status_code=204, headers={})
        self.assertTrue(response.data)
        self.assertEqual(response.status_code, 204)

    def test_with_different_status_codes(self):
        """Test ApiResponse with various status codes"""
        # Test 201 Created
        response_201 = ApiResponse(data={'created': True}, status_code=201, headers={})
        self.assertEqual(response_201.status_code, 201)

        # Test 204 No Content
        response_204 = ApiResponse(data=True, status_code=204, headers={})
        self.assertEqual(response_204.status_code, 204)

        # Test 200 OK
        response_200 = ApiResponse(data={'ok': True}, status_code=200, headers={})
        self.assertEqual(response_200.status_code, 200)

    def test_headers_access(self):
        """Test accessing various headers"""
        headers = {
            'Content-Type': 'application/json',
            'X-RateLimit-Remaining': '100',
            'X-RateLimit-Limit': '1000'
        }
        response = ApiResponse(data={'test': 'data'}, status_code=200, headers=headers)

        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.headers['X-RateLimit-Remaining'], '100')
        self.assertEqual(response.headers['X-RateLimit-Limit'], '1000')

    def test_empty_headers(self):
        """Test ApiResponse with empty headers"""
        response = ApiResponse(data={'test': 'data'}, status_code=200, headers={})
        self.assertEqual(response.headers, {})

    def test_data_attribute_types(self):
        """Test that data attribute can hold various types"""
        # Dictionary data
        dict_response = ApiResponse(data={'key': 'value'}, status_code=200, headers={})
        self.assertIsInstance(dict_response.data, dict)

        # List data
        list_response = ApiResponse(data=[1, 2, 3], status_code=200, headers={})
        self.assertIsInstance(list_response.data, list)

        # Boolean data
        bool_response = ApiResponse(data=True, status_code=204, headers={})
        self.assertIsInstance(bool_response.data, bool)

        # None data
        none_response = ApiResponse(data=None, status_code=204, headers={})
        self.assertIsNone(none_response.data)


if __name__ == '__main__':
    unittest.main()
