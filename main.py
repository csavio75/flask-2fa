import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from .storage import connect_db, create_tables
from .otp import generate_otp, verify_otp

app = Flask(__name__)
CORS(app)


@app.get("/")
def init_db():
    create_tables()
    return jsonify({'success': True})


@app.post("/login")
def login():
    records = json.loads(request.data)
    username = records['username']
    password = records['password']
    try:
        query = f"SELECT id, username FROM users WHERE username='{username}' AND password='{password}'"
        cnx = connect_db()
        cursor = cnx.cursor()
        cursor.execute(query)
        data = cursor.fetchone()
        cnx.close()

        if data:
            response = {
                'success': True,
                'data': {
                    'id': data[0],
                    'username': data[1],
                }
            }
        else:
            response = {'success': False}
        return jsonify(response)
    except Exception as e:
        print(e)
        return jsonify({
            'error': 'an error occurred while'
        })


@app.get('/otp/<username>')
def get_otp(username):
    uri = generate_otp(username)
    return jsonify({'uri': uri})


@app.post('/verify_otp')
def check_otp():
    records = json.loads(request.data)
    code = records['code']
    valid = verify_otp(code)
    return jsonify({'success': valid})


@app.get("/logout")
def logout():
    return jsonify({'status': 'logged out'})
