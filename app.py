import streamlit as st
import sqlite3

st.title("Student Registration App with DB")

# Connect to database (create if not exists)
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
''')
conn.commit()

# Input boxes
name = st.text_input("Enter your Name")
email = st.text_input("Enter your Email")

# Button
if st.button("Register"):
    c.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    st.success(f"Hello {name}, you are registered with email {email} 🎉")
