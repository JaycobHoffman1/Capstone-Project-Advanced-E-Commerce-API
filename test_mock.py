import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services.customerAccountService import login_customer

class TestLoginCustomer(unittest.TestCase):

    @patch('services.customerAccountService.db.session.execute')
    def test_login_customer(self, mock_customer): # Passing test
        faker = Faker()
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name = 'admin'), MagicMock(role_name='admin')]
        password = faker.password()
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)
        mock_customer.return_value.scalar_one_or_none.return_value = mock_user

        response = login_customer(mock_user.username, password)

        self.assertEqual(response['status'], 'Success')

if __name__ == '__main__':
    unittest.main()