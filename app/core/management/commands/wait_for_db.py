""" 
django command to wait for the database to be available.

"""

import time
from psycopg2 import OperationalError as PsycopgOp2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    """ Django command to wait for database"""

    def handle(self, *args, **options):
        
        self.stdout.write('waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True

            except(PsycopgOp2Error, OperationalError):
                self.stdout.write('databse unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))


         
        