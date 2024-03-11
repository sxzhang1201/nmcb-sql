import sqlite3
import sql_statements
import pandas as pd


def test_castor():
	database_path = 'test_castor.db'
	castor_file_path = 'transform_castor.csv'
	
	conn = None
	
	try:
		conn = sqlite3.connect(database_path)
	except Exception as e:
		print(e)
	
	# Create a Cursor object for data manipulation
	cursor = conn.cursor()
	
	# Create a table
	# if not os.path.exists(database_path):
	try:
		cursor.execute(sql_statements.sql_create_table)
	except Exception as e:
		print(e)
	
	# Insert data
	print('Inserting data')
	cursor.execute(sql_statements.sql_insert_fake_data)
	
	# Read database
	print('\nRead data after inserting data')
	cursor.execute(sql_statements.sql_query_data)
	rows = cursor.fetchall()
	for row in rows:
		print(row)
	
	# Load Castor CSV file
	data = pd.read_csv(castor_file_path)
	
	# A dictionary for representing mappings (Castor variable : SQL data model variable)
	variable_mapping = {
		'Castor Participant ID': 'participant_id',
		'sex': 'sex_at_birth',
		'birthplace': 'birth_place',
		'dob': 'date_of_birth'
	}
	
	# Get the list of CSV variables
	mapped_variables = list(variable_mapping.keys())
	# Get the list of SQL variables with the order correctly corresponding to `mapping_variables`
	sql_variables = [variable_mapping[key] for key in mapped_variables]
	
	# Subset dataset
	subset_df = data[mapped_variables]
	
	# Connect to SQLite database (or create if it doesn't exist)
	conn = sqlite3.connect('test_castor.db')
	cursor = conn.cursor()
	
	for index, row in subset_df.iterrows():
		columns = ', '.join(sql_variables)
		# print(columns)
		
		placeholders = ', '.join('"' + str(item) + '"' for item in row)
		# print(placeholders)
		
		sql = "INSERT INTO participant ({}) VALUES ({})".format(columns, placeholders)
		# print(sql)
		
		cursor.execute(sql)
	
	# Read database
	print('\nRead data after inserting transformed Castor data:')
	cursor.execute(sql_statements.sql_query_data)
	rows = cursor.fetchall()
	for row in rows:
		print(row)
	
	# Commit the changes and close the connection
	conn.commit()
	conn.close()


if __name__ == '__main__':
	test_castor()
