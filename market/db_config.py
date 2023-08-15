import yaml
from urllib.parse import quote_plus


def get_db_config():
    db_config = yaml.full_load(open('market/db.yaml'))

    db_details = {
        'user': db_config['user'],
        'password': quote_plus(db_config['password']),
        'host': db_config['host'],
        'port': db_config['port'],
        'database': db_config['database']
    }

    return db_details
