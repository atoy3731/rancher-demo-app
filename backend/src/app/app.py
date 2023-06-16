from flask import Flask, jsonify
import os

PORT = int(os.environ.get('PORT', '5000'))
VERSION = "2.0"

app = Flask(__name__)

response = {
    "version": VERSION
}


@app.route('/api/version')
def get_incomes():
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)