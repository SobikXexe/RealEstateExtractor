export PGPASSWORD=$POSTGRES_PASSWORD;
psql -U $POSTGRES_USER -d $POSTGRES_DB \
    -c "CREATE TABLE flat (
            id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
            title TEXT,
            photo TEXT
        );";
