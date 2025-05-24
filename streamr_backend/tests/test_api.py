import unittest
import json
from app import app # Assuming your Flask app instance is named 'app' in app/__init__.py

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_featured_content_api(self):
        response = self.app.get('/api/featured_content')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)
        if data:
            self.assertIn('id', data[0])
            self.assertIn('title', data[0])
            self.assertIn('description', data[0])
            self.assertIn('image_url', data[0])
            self.assertIn('type', data[0])

    def test_subscription_plans_api(self):
        response = self.app.get('/api/subscription_plans')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)
        if data:
            self.assertIn('id', data[0])
            self.assertIn('name', data[0])
            self.assertIn('price_monthly', data[0])
            self.assertIn('features', data[0])
            self.assertIsInstance(data[0]['features'], list)
            self.assertIn('most_popular', data[0])

if __name__ == '__main__':
    unittest.main()
