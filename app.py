from flask import Flask, render_template, request
from passwordgen import generate_password, rate_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    strength = None
    css_class = None

    if request.method == "POST":
        length = int(request.form.get("length", 12))
        use_lower = "lowercase" in request.form
        use_upper = "uppercase" in request.form
        use_nums = "numbers" in request.form
        use_syms = "symbols" in request.form

        password = generate_password(length, use_lower, use_upper, use_nums, use_syms)

        if "Please select" not in password:
            strength, css_class = rate_password(password)

    return render_template("index.html", password=password, strength=strength, css_class=css_class)

if __name__ == "__main__":
    app.run(debug=True)


