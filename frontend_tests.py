import os
import frontend
import unittest

class FrontendTestCase(unittest.TestCase):
  def setUp(self):
    frontend.app.config['TESTING'] = True
    self.app = frontend.app.test_client()

  def tearDown(self):
    pass

if __name__ == '__main__':
  unittest.main()