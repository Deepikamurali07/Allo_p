import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'ProductDetails',
    'user': 'PUser12',
    'password': 'PSQL@123',
    'host': 'localhost',
    'port': '5432'
}

# Establish the connection
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Create the table with columns in the specified order
create_table_query = '''
CREATE TABLE IF NOT EXISTS prodet (
    UniqueID SERIAL PRIMARY KEY,
    Sr_No INTEGER,
    Product_Name VARCHAR(255),
    Order_Processing_Date DATE,
    Promised_Delivery_Date DATE,
    Quantity_Required INTEGER,
    Components TEXT,
    Operation TEXT,
    Process_Type VARCHAR(50),
    Machine_Number VARCHAR(50),
    Run_Time_min_per_1000 INTEGER,
    Cycle_Time_seconds INTEGER,
    Setup_time_seconds INTEGER,
    Ready_Time TIMESTAMP,
    Start_Time TIMESTAMP,
    End_Time TIMESTAMP,
    Wait_Time INTERVAL,
    Status VARCHAR(50),
    Time_Difference INTERVAL
);
'''
cursor.execute(create_table_query)
conn.commit()

# Insert sample data
insert_query = '''
INSERT INTO prodet (
    Sr_No,
    Product_Name,
    Order_Processing_Date,
    Promised_Delivery_Date,
    Quantity_Required,
    Components,
    Operation,
    Process_Type,
    Machine_Number,
    Run_Time_min_per_1000,
    Cycle_Time_seconds,
    Setup_time_seconds,
    Ready_Time,
    Start_Time,
    End_Time,
    Wait_Time,
    Status,
    Time_Difference
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
);
'''
sample_data = (
    1, 'ProductA', '2024-06-28', '2024-07-01', 1000, 'Component1, Component2', 'OperationA', 'TypeA', 'Machine1', 
    10, 5, 300, '2024-06-30 08:00:00', '2024-06-30 09:00:00', '2024-06-30 11:00:00', '30 minutes', 'In Progress', '15 minutes'
)
cursor.execute(insert_query, sample_data)
conn.commit()

# Select data
select_query = '''
SELECT * FROM prodet;
'''
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
cursor.close()
conn.close()
