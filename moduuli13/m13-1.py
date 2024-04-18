from flask import Flask, request
app = Flask(__name__)

def is_prime(luku):
    if luku > 1:
        for i in range(2, int(luku)):
            if (luku % i) == 0:
                return False
        return True
    else:
        return False

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = float(luku)  # Convert luku to float
    if is_prime(luku):
        return f"{luku} is a prime number."
    else:
        return f"{luku} is not a prime number."

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
