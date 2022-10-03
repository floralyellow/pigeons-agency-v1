import logging
from copy import deepcopy

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import DEFAULT_DB_ALIAS, ConnectionHandler, connections

LOGGER = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create DB"

    def handle(self, *args, **options):
        selected_database = options.get("database") or "default"
        database_config = settings.DATABASES[selected_database]

        if database_config.get("AUTO_CREATE"):
            self.create_db(selected_database)

    def create_db(self, database):
        database_vendor = connections[database].vendor

        if database_vendor == "postgresql":
            database_config = settings.DATABASES[database]
            postgres_database_config = deepcopy(database_config)
            postgres_database_config["NAME"] = "postgres"
            handler = ConnectionHandler(databases={DEFAULT_DB_ALIAS: postgres_database_config})

            database_name = database_config["NAME"]
            with handler[DEFAULT_DB_ALIAS].cursor() as cursor:
                database_config = settings.DATABASES[database]
                if database_config.get("AUTO_DROP_BEFORE_CREATE"):
                    cursor.execute('DROP DATABASE "{}"'.format(database_name))
                cursor.execute('CREATE DATABASE "{}"'.format(database_name))

            self.stdout.write("Auto-created database '{}'".format(database_name))
            return True

        return False
