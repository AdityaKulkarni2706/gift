from flask import Flask, render_template, request, jsonify
import functions
import sqlite3

app = Flask(__name__)

@app.route("/")

def route_default():
    return render_template("index.html")

@app.route("/bday")

def render_bday():
    return render_template("flipbook.html")

@app.route("/submit", methods = ["POST"])
def submit():
    data = request.json
    username = data['username']
    pwd = data['password']
    query = f"SELECT * FROM Credentials WHERE username = '{username}' AND password = '{pwd}'"
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f"Rows : {rows}")

    if rows:
        return jsonify({"status": "1", "data": rows})
    else:
        return jsonify({"status": "0"})




if __name__ == '__main__':
    app.run(debug=True)
