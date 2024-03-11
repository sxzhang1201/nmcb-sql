
sql_create_table = '''
CREATE TABLE participant
(sex_at_birth			  INTEGER			  NOT NULL ,
participant_id			INTEGER	      NOT NULL ,
date_of_birth				DATE		NOT NULL ,
birth_place			  VARCHAR(20)		 NULL
)'''

sql_insert_fake_data = '''
INSERT INTO participant VALUES
('0', 'castor_1', '2011', 'NL'),
('1', 'castor_2', '2002', 'ES'),
('2', 'castor_3', '1992', 'NL'),
('1', 'castor_5', '1892', 'UK')
'''

sql_query_data = '''
SELECT * FROM participant
'''