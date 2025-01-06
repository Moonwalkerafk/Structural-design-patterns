#Proxy — это структурный паттерн проектирования, который предоставляет суррогатный объект вместо реального.


class Subject:
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("RealSubject: Performing a sensitive operation.")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject, user_role: str):
        self._real_subject = real_subject
        self._user_role = user_role

    def request(self):
        if self._user_role == "admin":
            self._real_subject.request()
        else:
            print("Proxy: Access denied. You don't have the necessary privileges.")


# Пример использования
real_subject = RealSubject()
proxy_admin = Proxy(real_subject, "admin")
proxy_admin.request()
proxy_user = Proxy(real_subject, "user")
proxy_user.request()
