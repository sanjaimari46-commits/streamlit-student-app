import streamlit as st
import sqlite3

st.title("Student Registration App")

# -----------------------------
# Database connection
# -----------------------------
conn = sqlite3.connect("students.db")
c = conn.cursor()

# Create table if not exists
c.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")
conn.commit()

# -----------------------------
# Registration form (FOR ALL)
# -----------------------------
st.subheader("Student Registration")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")

if st.button("Register"):
    if name.strip() == "" or email.strip() == "":
        st.error("Please enter both name and email")
    else:
        c.execute(
            "INSERT INTO students (name, email) VALUES (?, ?)",
            (name, email)
        )
        conn.commit()
        st.success("Registered successfully 🎉")

# -----------------------------
# Admin section (ONLY FOR YOU)
# -----------------------------
st.markdown("---")
st.subheader("Admin Login")

admin_password = st.text_input("Enter admin password", type="password")

if admin_password == "admin123":   # 🔐 change this password if you want
    st.success("Admin access granted")

    c.execute("SELECT * FROM students")
    rows = c.fetchall()

    if len(rows) == 0:
        st.info("No registrations yet")
    else:
        st.table(rows)

elif admin_password != "":
    st.error("Wrong password")
