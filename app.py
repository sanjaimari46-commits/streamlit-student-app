import streamlit as st
import sqlite3

st.title("Student Registration App")

# DB connect
conn = sqlite3.connect("students.db")
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")
conn.commit()

# Inputs
name = st.text_input("Enter Name")
email = st.text_input("Enter Email")

# Insert data
if st.button("Register"):
    c.execute(
        "INSERT INTO students (name, email) VALUES (?, ?)",
        (name, email)
    )
    conn.commit()
    st.success("Data saved successfully")

# SHOW DATA
st.subheader("Registered Students")

c.execute("SELECT * FROM students")
rows = c.fetchall()

st.table(rows)
