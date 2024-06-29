import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'ProductDetails',
    'user': 'PUser12',
    'password': 'PSQL@123',
    'host': 'localhost',
    'port': '5432'
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Create the RunTime table
create_table_query = '''
CREATE TABLE IF NOT EXISTS RunTime (
    Run_time INTEGER
);
'''
cursor.execute(create_table_query)
conn.commit()

# Insert a row into the RunTime table
insert_query = '''
INSERT INTO RunTime (Run_time) VALUES (%s);
'''
run_time_value = 27  # Example integer value
cursor.execute(insert_query, (run_time_value,))
conn.commit()

# Select and fetch data from the RunTime table
select_query = 'SELECT * FROM RunTime;'
cursor.execute(select_query)
rows = cursor.fetchall()

# Print the selected rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
