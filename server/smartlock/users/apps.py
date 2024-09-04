from django.apps import AppConfig


class UsersConfig(AppConfig):
    from django.apps import AppConfig
    name = 'users'

    def ready(self):
        import users.signals
