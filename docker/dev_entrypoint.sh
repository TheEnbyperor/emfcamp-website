#!/usr/bin/env bash
#
# Entrypoint script used by development app docker image
#
set -e

export PGPASSWORD=postgres
PSQL="/usr/bin/psql -h postgres -U postgres"

until $PSQL -c '\q'; do
  >&2 echo "Waiting for Postgres to be available"
  sleep 1
done

echo "Creating databases (errors about database existing are normal)..."

$PSQL -c 'CREATE DATABASE emf_site' || true
$PSQL emf_site -c 'CREATE EXTENSION postgis' || true
$PSQL -c 'CREATE DATABASE emf_site_test' || true
$PSQL emf_site_test -c 'CREATE EXTENSION postgis' || true

# Create dev config from example file if it doesn't exist
if [ ! -e /app/config/development.cfg ];
then
	cp /app/config/development-example.cfg /app/config/development.cfg
fi;

echo "Initialising database..."
poetry run flask db upgrade

if [ $# -gt 0 ]; then
  exec "$@"
fi

echo "Creating base data..."
poetry run flask create_perms
poetry run flask dev createbankaccounts
poetry run flask cfp create_venues
poetry run flask cfp create_tags
poetry run flask tickets create
echo "Starting dev server..."
exec poetry run flask run --extra-files ./config/development.cfg:./logging.yaml -h 0.0.0.0 -p 2342 --debug
