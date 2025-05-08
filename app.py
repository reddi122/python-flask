from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Docker Calculator!"

@app.route('/calculate')
def calculate():
    operation = request.args.get('operation')
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except (TypeError, ValueError):
        return "Please provide valid numbers for num1 and num2."

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero."
        result = num1 / num2
    else:
        return "Unsupported operation. Use add, subtract, multiply, or divide."

    return f"The result of {operation}ing {num1} and {num2} is: {result}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

