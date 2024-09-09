from flask import Flask, jsonify, request
import os

PORT = int(os.environ.get('PORT', '5000'))
VERSION = "1.0"
DEBUG = True if str(os.environ.get('DEBUG')).lower() == 'true' else False

app = Flask(__name__)

response = {
    "version": VERSION
}

@app.route('/api/version')
def get_incomes():
    if DEBUG:
        print(request.headers)
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)