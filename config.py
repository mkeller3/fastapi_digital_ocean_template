"""GeoPortal - Configuration File"""

import os

DATABASES = {
    "data": {
        "host": os.environ['db_host'],
        "database": "data",
        "username": os.environ['db_username'],
        "password": os.environ['db_password'],
        "port": 5432,
        "cache_age_in_seconds": 6000,
        "max_features_per_tile": 100000
    }
}
