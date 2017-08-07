from indexd.index.drivers.alchemy import SQLAlchemyIndexDriver
from indexd.alias.drivers.alchemy import SQLAlchemyAliasDriver
from indexd.auth.drivers.alchemy import SQLAlchemyAuthDriver

usr = '{{db_username}}'
db = '{{db_database}}'
psw = '{{db_password}}'
pghost = '{{db_host}}'
pgport = 5432
CONFIG = {}

CONFIG['JSONIFY_PRETTYPRINT_REGULAR'] = False
CONFIG['INDEX'] = {
'driver': SQLAlchemyIndexDriver('postgresql+psycopg2://{usr}:{psw}@{pghost}:{pgport}/{db}'.format(
    usr=usr,
    psw=psw,
    pghost=pghost,
    pgport=pgport,
    db=db,
)),
}

CONFIG['ALIAS'] = {
'driver': SQLAlchemyAliasDriver('postgresql+psycopg2://{usr}:{psw}@{pghost}:{pgport}/{db}'.format(
    usr=usr,
    psw=psw,
    pghost=pghost,
    pgport=pgport,
    db=db,
)),
}

AUTH = SQLAlchemyAuthDriver('postgresql+psycopg2://{usr}:{psw}@{pghost}:{pgport}/{db}'.format(
    usr=usr,
    psw=psw,
    pghost=pghost,
    pgport=pgport,
    db=db,
))

settings = {'config': CONFIG, 'auth': AUTH}