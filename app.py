import streamlit as st
import mysql.connector

st.title("Student Registration App")

# -----------------------------
# MySQL Connection (XAMPP)
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",          # XAMPP default
    database="streamlit_db"
)

c = conn.cursor()

# -----------------------------
# Registration Form
# -----------------------------
st.subheader("Student Registration")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")

if st.button("Register"):
    if name == "" or email == "":
        st.error("Fill all fields")
    else:
        c.execute(
            "INSERT INTO students (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        st.success("Registered successfully 🎉")

# -----------------------------
# Admin Section
# -----------------------------
st.markdown("---")
st.subheader("Admin Login")

admin_password = st.text_input("Enter admin password", type="password")

if admin_password == "admin123":
    st.success("Admin access granted")

    c.execute("SELECT * FROM students")
    rows = c.fetchall()

    if rows:
        st.table(rows)
    else:
        st.info("No data yet")

elif admin_password != "":
    st.error("Wrong password")
