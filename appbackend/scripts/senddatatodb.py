import psycopg2
import numpy as np


# Queries to create table and insert query

# CREATE TABLE maintableaudioandtext (
# id SERIAL PRIMARY KEY,
# audio_data BYTEA,
# text_data TEXT
# );

# INSERT INTO public.maintableaudioandtext(
# id, audio_data, text_data)
# VALUES (?, ?, ?);


def senddatato_db(audiodata, textdata ):

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="http://172.19.80.1:5432",
        database="postgres",
        user="postgres",
        password="."
    )

    # Convert float32 data to bytes
    audio_bytes = audiodata.tobytes()

    # Insert data into the database
    cur = conn.cursor()
    
    query =  """INSERT INTO public.maintableaudioandtext(id, audiodata, textdata)VALUES (%s, %s, %s);"""
    

    cur.execute(query, (audiodata, textdata))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

    print('db write sucess')

    return 


# senddatato_db(audiodata, textdata )

