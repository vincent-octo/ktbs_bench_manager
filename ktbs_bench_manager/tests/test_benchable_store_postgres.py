from ktbs_bench_manager import BenchableGraph
from os import getenv
import rdflib


# Get PostgreSQL connection info from environment.
# This must be set by: export KTBS_PG_USER="user_of_postgres" && export KTBS_PG_PASSWORD="my_password"
PG_USER = getenv('KTBS_PG_USER')
PG_PASSWORD = getenv('KTBS_PG_PASSWORD')

PG_STORE_ID = 'http://localhost/pg/persistent_store'

assert PG_USER is not None and PG_PASSWORD is not None, 'Environment variables must be set in order to connect '\
    + 'to PostgreSQL.\nYou need to: export KTBS_PG_USER="user_of_postgres" && export KTBS_PG_PASSWORD="my_password".'

CREATED_STORE = {'store_id': PG_STORE_ID,
                 'config': 'postgresql+psycopg2://{user}:{password}@localhost/test_ktbs_bench_manager'.format(
                     user=PG_USER, password=PG_PASSWORD
                 )}


def test_connect_existing_pg():
    """Test a successful connection to an already created PostgreSQL store."""
    postgres = BenchableGraph("SQLAlchemy",
                              CREATED_STORE['store_id'],
                              CREATED_STORE['config'],
                              graph_create=False)
    assert postgres.connect() == rdflib.store.VALID_STORE
    postgres.close()
