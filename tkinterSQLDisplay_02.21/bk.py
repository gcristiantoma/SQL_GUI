import sqlite3
my_conn = sqlite3.connect('my_db.db')
print("Created database successfully");

my_conn.execute('''
CREATE TABLE IF NOT EXISTS customers(id integer primary key,
                      first_name text,
                      last_name text,
                      age integer,
                      sex text
                      );''')
my_conn.commit()
print("Student Table created successfully");
#
# r_set=my_conn.execute('''INSERT INTO `customers`
# (`id`, `first_name`, `last_name`, `age`,`sex`) VALUES
# (1, 'John Deo', 'Stevenson', 75, 'female'),
# (2, 'Max Ruin', 'Jhonson', 85, 'male'),
# (3, 'Arnold', 'Jhonson', 55, 'male'),
# (4, 'Krish Star', 'Stevenson', 60, 'female'),
# (5, 'John Mike', 'Stevenson', 60, 'female'),
# (6, 'Alex John', 'Stevenson', 55, 'male'),
# (7, 'My John Rob', 'Woszniak', 78, 'male'),
# (8, 'Asruid', 'Woszniak', 85, 'male'),
# (9, 'Tes Qry', 'Muntean', 78, 'male'),
# (10, 'Big John', 'Stevenson', 55, 'female'),
# (11, 'Ronald', 'Muntean', 89, 'female'),
# (12, 'Recky', 'Muntean', 94, 'female'),
# (13, 'Kty', 'Wizer', 88, 'female'),
# (14, 'Bigy', 'Wizer', 88, 'female'),
# (15, 'Tade Row', 'Stevenson', 88, 'male'),
# (16, 'Gimmy', 'Stevenson', 88, 'male'),
# (17, 'Tumyu', 'Muntean', 54, 'male'),
# (18, 'Honny', 'Woszniak', 75, 'male'),
# (19, 'Tinny', 'Witsze', 18, 'male'),
# (20, 'Jackly', 'Witsze', 65, 'female'),
# (21, 'Babby John', 'Stevenson', 69, 'female'),
# (22, 'Reggid', 'Wizer', 55, 'female'),
# (23, 'Herod', 'Eight', 79, 'male'),
# (24, 'Tiddy Now', 'Wizer', 78, 'male'),
# (25, 'Giff Tow', 'Wizer', 88, 'male'),
# (26, 'Crelea', 'Wizer', 79, 'male'),
# (27, 'Big Nose', 'Jhonson', 81, 'female'),
# (28, 'Rojj Base', 'Wizer', 86, 'female'),
# (29, 'Tess Played', 'Wizer', 55, 'male'),
# (30, 'Reppy Red', 'Muntean', 79, 'female'),
# (31, 'Marry Toeey', 'Stevenson', 88, 'male'),
# (32, 'Binn Rott', 'Wizer', 90, 'female'),
# (33, 'Kenn Rein', 'Muntean', 96, 'female'),
# (34, 'Gain Toe', 'Wizer', 69, 'male'),
# (35, 'Rows Noump', 'Muntean', 88, 'female');''')
# my_conn.commit()
# my_conn.close()
db_name='my_db.db'
def connection_db(db_name):
    my_conn = sqlite3.connect(db_name)
    return my_conn

def results_query(db_connection,query):
    r_set=db_connection.execute(query)
    rows = r_set.fetchall()
    return rows

conn=connection_db(db_name)

list_results=results_query(conn,"select * from customers")

def return_column_names(db_name,table_name):
    con=connection_db(db_name)
    columns_names=results_query(con,"PRAGMA table_info({});".format(table_name))
    lista=[]
    for c in columns_names:
        lista.append(c[1])
        print(c[1])
    return lista
# return_column_names('my_db.db',"student")

def return_set_results(db_name,table_name):
    results= results_query(connection_db(db_name),"select * from {}".format(table_name))
    return results

print(len(return_set_results(db_name,"student")))
for row in list_results:
    print(row)
