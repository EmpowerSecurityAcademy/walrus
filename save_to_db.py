#Server Connection to MySQL:

import MySQLdb
from import_config import load_config

config = load_config()

conn = MySQLdb.connect(host= config["database"]["connection_url"],
                  user=config["database"]["user_name"],
                  passwd=config["database"]["password"],
                  db=config["database"]["db_instance"])
x = conn.cursor()

text_file = open("./tmp/pdf_text.txt", "r")
lines = text_file.readlines()
all_text = ""
for line in lines:
	all_text += line

print(all_text)

try:
   x.execute("INSERT INTO pdfs (text_value, url) VALUES(" + all_text + ", 'sample_url')");
   conn.commit()
except:
   conn.rollback()

conn.close()



