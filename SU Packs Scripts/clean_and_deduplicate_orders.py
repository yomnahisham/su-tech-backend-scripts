import pandas as pd
import mysql.connector

# Step 1: Read the CSV file
csv_file = 'test2.csv' # Specify your actual input file location here
df = pd.read_csv(csv_file)

# Step 2: Clean the data - remove duplicates in the CSV based on email and phone number
df['email'] = df['email'].str.strip()  # Clean up any whitespace in emails
df.drop_duplicates(subset=['email', 'Phone_Number'], keep='first', inplace=True)

# Step 3: Fix the order_num in the CSV to ensure continuity after removing duplicates
df['order_num'] = range(1, len(df) + 1)

# Step 4: Save the cleaned data with fixed order_num to a new CSV file
cleaned_csv = 'cleaned_file.csv'
df.to_csv(cleaned_csv, index=False)

# Step 5: Connect to MySQL Database
db_connection = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_db_name'
)
cursor = db_connection.cursor()

# Step 6: Remove duplicates from the database based on google_id (email)
# Query to identify all duplicates by google_id (excluding the one with the smallest order_num)
find_duplicates_query = """
SELECT google_id, MIN(order_num) AS keep_order_num
FROM orders
GROUP BY google_id
HAVING COUNT(*) > 1;
"""
cursor.execute(find_duplicates_query)
results = cursor.fetchall()

# Step 7: Delete duplicates while keeping the entry with the smallest order_num
for google_id, keep_order_num in results:
    delete_query = """
    DELETE FROM orders 
    WHERE google_id = %s AND order_num != %s;
    """
    cursor.execute(delete_query, (google_id, keep_order_num))
    db_connection.commit()

# Step 8: Fix the order_num sequence after deletion in the database
# We need to reset the order_num so that it is continuous
update_order_num_query = """
SET @order_num := 0;
UPDATE orders
SET order_num = (@order_num := @order_num + 1)
ORDER BY google_id, order_num;
"""
cursor.execute(update_order_num_query)
db_connection.commit()

# Close the database connection
cursor.close()
db_connection.close()

print("Duplicates removed and order_num fixed successfully in both CSV and database.")
