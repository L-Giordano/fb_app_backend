from unittest import (
    TestCase,
    mock,
    )

from src.user.domain.errors import PasswordError, UserError
from src.user.domain.password_encrypter import PasswordEncrypter
from src.user.domain.user_enums import (
    UserPrivilege,
    UserStatus,
    )
from src.user.domain.user_model import User


class TestUser(TestCase):

    @mock.patch("src.user.domain.password_encrypter.PasswordEncrypter.new_ecrypted_password")
    def setup_user(mocked_hashed_password, other) -> User:

        mocked_hashed_password.return_value = 'password'

        first_name = 'Juan'
        last_name = 'Garcia'
        email = 'juangarcia@email.com'
        user_name = 'jgarcia'
        password = 'password'

        return User.create(first_name, last_name, email, user_name, password)

    @mock.patch("src.user.domain.password_encrypter.PasswordEncrypter.new_ecrypted_password")
    def test_when_create_user_success(self, mocked_hashed_password):

        mocked_hashed_password.return_value = 'password'

        first_name = 'Juan'
        last_name = 'Garcia'
        email = 'juangarcia@email.com'
        user_name = 'jgarcia'
        password = 'password'

        user = User.create(first_name, last_name, email, user_name, password)

        mocked_hashed_password.assert_called_once()

        self.assertEqual(first_name, user.first_name)
        self.assertEqual(last_name, user.last_name)
        self.assertEqual(email, user.email.value)
        self.assertEqual(user_name, user.user_name)
        self.assertTrue(UserPrivilege.USER in user.user_privilege)
        self.assertTrue(user.is_active)

    def test_archive_user(self):
        user = self.setup_user()
        user.archive_user()

        self.assertTrue(user.user_status == UserStatus.ARCHIVED)

    def test_change_password_of_archive_user(self):
        user = self.setup_user()
        user.user_status = UserStatus.ARCHIVED

        with self.assertRaises(UserError):
            user.change_password(current_password='password', new_password='new_password')

    def test_when_change_password_with_incorrect_current_pw(self):
        user = User.create(
            first_name='Bruno',
            last_name='Diaz',
            email='batman@email.com',
            user_name='batman',
            password='password',
            )
        current_password = 'password1'
        new_password = 'new_password'

        with self.assertRaises(PasswordError):
            user.change_password(current_password=current_password, new_password=new_password)

    def test_when_change_password_success(self):
        user = User.create(
            first_name='Bruno',
            last_name='Diaz',
            email='batman@email.com',
            user_name='batman',
            password='password',
            )
        current_password = 'password'
        new_password = 'new_password'

        user.change_password(current_password=current_password, new_password=new_password)

        self.assertTrue(PasswordEncrypter.is_password_valid(new_password, user.password))
