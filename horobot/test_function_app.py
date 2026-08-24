import unittest
import azure.functions as func # type: ignore

from function_app import HttpTrigger # type: ignore

class TestFunction(unittest.TestCase):
  def test_my_function(self):
    # Construct a mock HTTP request.
    req = func.HttpRequest(method='GET',
                           body=None,
                           url='/api/http_trigger',
                           params={'name': 'Test User'})
    # Call the function.
    func_call = HttpTrigger.build().get_user_function()
    resp = func_call(req)
    # Check the output.
    self.assertEqual(
        resp.get_body(),
        b'Hello, Test User. This HTTP triggered function executed successfully.',
    )