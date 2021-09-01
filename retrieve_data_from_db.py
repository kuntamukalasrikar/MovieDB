import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="srikar",
  password="srikar@1234",
  database="cinema"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT movies.name, cast.actor, cast.actress, cast.director, movies.year_of_release FROM movies INNER JOIN cast ON movies.movie_id=cast.movie_id")

myresult = mycursor.fetchall()

print("output")
for x in myresult:
  print(x)

