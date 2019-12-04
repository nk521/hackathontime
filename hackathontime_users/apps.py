from django.apps import AppConfig


class HackathontimeUsersConfig(AppConfig):
    name = 'hackathontime_users'

    def ready(self):
    	import hackathontime_users.signals