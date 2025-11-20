from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# --------------------------------------
#  MYSQL CONNECTION FUNCTION
# --------------------------------------
def get_db_connection():
    return mysql.connector.connect(
        host="portfolio_mysql",
        user="root",
        password="root",
        database="portfolio"
    )

# --------------------------------------
#  FETCH PROFILE DATA (linkedin, github, about)
# --------------------------------------
def get_profile_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT linkedin, github, about_text, email FROM profile LIMIT 1")
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        # If no record exists, return placeholder
        return row if row else {
            "linkedin": "#",
            "github": "#",
            "about_text": "Your about section is not set yet."
        }

    except Exception as e:
        print("Database error:", e)
        return {
            "linkedin": "#",
            "github": "#",
            "about_text": "Error loading profile info."
        }

# --------------------------------------
#  ROUTES
# --------------------------------------

@app.route("/")
def home():
    data = get_profile_data()
    return render_template("index.html", data=data)

@app.route("/about")
def about():
    data = get_profile_data()
    return render_template("about.html", data=data)

@app.route("/contact")
def contact():
    data = get_profile_data()
    return render_template("contact.html", data=data)

# --------------------------------------
#  RUN APP
# --------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
