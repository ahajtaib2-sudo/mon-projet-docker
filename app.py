from flask import Flask, render_template, request
from password_utils import check_password_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        password = request.form.get("password", "")
        level, score, reasons = check_password_strength(password)
        result = {
            "password": password,
            "level": level,
            "score": score,
            "reasons": reasons,
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
