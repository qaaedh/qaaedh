from flask import Flask, jsonify, request
import math

app = Flask(__name__)

@app.route('/alkuluku/<int:number>', methods=['GET'])
def is_prime(number):
    if number < 2:
        return jsonify({"Number": number, "isPrime": False})
    if number == 2:
        return jsonify({"Number": number, "isPrime": True})
    if number % 2 == 0:
        return jsonify({"Number": number, "isPrime": False})
    for i in range(3, math.isqrt(number) + 1, 2):
        if number % i == 0:
            return jsonify({"Number": number, "isPrime": False})
    return jsonify({"Number": number, "isPrime": True})

if __name__ == '__main__':
    app.run(debug=True)