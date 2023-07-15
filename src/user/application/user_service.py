from src.user.application.user_DTOs import (
    CreateUserDTO,
    UserDto,
    )
from src.user.domain.user_model import User
from src.user.domain.user_repository import IUserRepository


class UserService:
    def __init__(
        self,
        user_repo: IUserRepository,
    ) -> None:
        self.user_repo = user_repo

    def create(self, user_dto: CreateUserDTO) -> UserDto:
        new_user = User.create(
            first_name=user_dto.first_name,
            last_name=user_dto.last_name,
            email=user_dto.email,
            user_name=user_dto.user_name,
            password=user_dto.password,
        )

        saved_user = self.user_repo.save(user=new_user)

        return self._parse_user_dto(saved_user)

    def get_user_by_id(self, user_id: int) -> UserDto:
        retrive_user = self.user_repo.get(user_id=user_id)
        return self._parse_user_dto(retrive_user)

    def get_all_user(self) -> list[UserDto]:
        all_users = self.user_repo.get_all

        response = []

        for user in all_users:
            response.append(self._parse_user_dto(user))

        return response

    def archive(self, user_id: int) -> None:
        user = self.user_repo.get(user_id=user_id)
        user.archive_user()
        self.user_repo.save(user=user)

    def change_user_password(self, user_id: int, current_password: str, new_password: str,) -> None:
        user = self.user_repo.get(user_id=user_id)
        user.change_password(current_password=current_password, new_password=new_password)
        self.user_repo.save(user=user)

    def _parse_user_dto(self, user: User) -> UserDto:
        return UserDto(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            user_name=user.user_name,
            )
