__author__ = 'Q'


from Database import DataBase



db = DataBase("summer2014courses.db")

print("-------------Assignments---------------------")
db.display_table_by_date("Assignments")

print("-------------Readings------------------------")
db.display_table_by_date("Readings")

print("-------------Tests------------------------")
db.display_table_by_date("Tests")

db.close()