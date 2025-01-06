#Adapter — это структурный паттерн проектирования, который позволяет объектам с несовместимыми интерфейсами работать вместе.


class LegacyUser:
    def __init__(self, data: str):
        parts = data.split("|")
        self.username = parts[0]
        self.email = parts[1]
        self.phone_number = parts[2]


class UserAdapter:
    def __init__(self, legacy_user: LegacyUser):
        self.username = legacy_user.username
        self.email = legacy_user.email
        self.phone = legacy_user.phone_number


def process_user_data(data: str):
    legacy_user = LegacyUser(data)
    user_adapter = UserAdapter(legacy_user)
    print(user_adapter.__dict__)


if __name__ == "__main__":
    data = "john_doe|john@example.com|1234567890"
    process_user_data(data)
