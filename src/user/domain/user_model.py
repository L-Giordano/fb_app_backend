from src.user.domain.email_address import EmailAddress
from src.user.domain.errors import (
    PasswordError,
    UserError,
    )
from src.user.domain.password_encrypter import PasswordEncrypter
from src.user.domain.user_enums import (
    UserPrivilege,
    UserStatus,
    )


class User:
    def __init__(
            self,
            id: str,
            first_name: str,
            last_name: str,
            email: EmailAddress,
            user_name: str,
            password: str,
            user_status: UserStatus,
            user_privilege: list[UserPrivilege]
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.password = password
        self.user_status = user_status
        self.user_privilege = user_privilege

    @classmethod
    def create(
        cls,
        first_name: str,
        last_name: str,
        email: str,
        user_name: str,
        password: str,
    ) -> "User":
        email = EmailAddress(email)
        password = PasswordEncrypter.new_ecrypted_password(password)
        user_status = UserStatus.ACTIVE
        user_privilege = [UserPrivilege.USER]
        return cls(
            id=None,
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_name=user_name,
            password=password,
            user_status=user_status,
            user_privilege=user_privilege,
            )

    @property
    def is_active(self) -> bool:
        return self.user_status == UserStatus.ACTIVE

    def archive_user(self) -> None:
        self.user_status = UserStatus.ARCHIVED

    def change_password(self, current_password, new_password) -> None:
        if self.user_status == UserStatus.ARCHIVED:
            raise UserError("Can not modify archived user!")
        if not (PasswordEncrypter
                .is_password_valid(current_password, self.password)):
            raise PasswordError('You provided a wrong current password')
        self.password = PasswordEncrypter.new_ecrypted_password(new_password)
