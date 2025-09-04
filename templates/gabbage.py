from flask import Flask, render_template, request
from calculator import calculator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            a = request.form["num1"]
            b = request.form["num2"]
            op = request.form["operation"]
            result = calculator(a, b, op)
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)



def calculator(a, b, op):
    a = float(a)
    b = float(b)

    if op == 'add' or op == '+':
        return a + b
    elif op == 'subtract' or op == '-':
        return a - b
    elif op == 'multiply' or op == '*':
        return a * b
    elif op == 'divide' or op == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Unsupported operation"

def get_min(numbers:int):
    min_num = numbers[-1]
    for number in numbers:
        if number < min_num:
            min_num = number
    return min_num


def get_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num


def factorial(n):
   result = 1
   for i in range(1, n+1):
       result = result * i
   return result


def  get_average(numbers):
    total = sum(numbers)
    length = len(numbers)
    return total / length if length > 0 else 0

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python Calculator</title>
    <style>
        body {
            font-family: sans-serif;
            background: #f9f9f9;
            padding: 40px 20px;
            text-align: center;
            color: #333;
        }

        h1 {
            color: #0077b6;
            margin-bottom: 10px;
        }

        .description {
            max-width: 500px;
            margin: 0 auto 30px;
            font-size: 16px;
            line-height: 1.5;
        }

        form {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            display: inline-block;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        input, select, button {
            padding: 10px;
            margin: 8px 5px;
            font-size: 16px;
            width: 180px;
            max-width: 100%;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            background: #0077b6;
            color: #fff;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        button:hover {
            background: #023e8a;
        }

        h2 {
            margin-top: 30px;
            color: #2a9d8f;
        }

        @media (max-width: 500px) {
            input, select, button {
                width: 100%;
                margin: 10px 0;
            }

            form {
                width: 90%;
            }
        }
    </style>
</head>
<body>
    <h1>Python Calculator 🧮</h1>

    <div class="description">
        <p><strong>By Qowiyat</strong> - Intern at Veegil Technologies</p>
        <p>Enter two numbers, choose an operation, and hit <strong>Calculate</strong> to get your result.</p>
    </div>

    <form method="post">
        <input type="text" name="num1" placeholder="First number" required>
        <input type="text" name="num2" placeholder="Second number" required><br>
        <select name="operation" required>
            <option value="+">Add (+)</option>
            <option value="-">Subtract (-)</option>
            <option value="*">Multiply (*)</option>
            <option value="/">Divide (/)</option>
            <option value = "!">Factorial(!)</option>
        </select><br>
        <button type="submit">Calculate</button>
    </form>

    <h2>Result: {{ result }}</h2>
</body>
</html>
