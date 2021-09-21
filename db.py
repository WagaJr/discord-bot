import psycopg2 # Use NoSQL

conn = psycopg2.connect("dbname=test user=postgres")

cur = conn.cursor()

cur.execute