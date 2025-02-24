import os
import qrcode
import sqlite3
from flask import Flask, request, jsonify
import pyotp

app = Flask(__name__)

#Função para carregar o banco de dados
def load_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        secret TEXT NOT NULL
    )
    ''')
    conn.commit()
    return conn, cursor

#Função para salvar um usuário no banco de dados
def save_user(username, password, secret):
    conn, cursor = load_db()
    cursor.execute('''
    INSERT INTO users(username, password, secret) VALUES (?,?,?)
    ''', (username, password, secret))
    conn.commit()
    conn.close()

#Endpoint simples para garantir que o Flask esta funcionando    
@app.route('/')
def home():
    return "Flask is working!"

#Endpoint para registrar um usuário
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error":"Username and password are required"}), 400
    
    #Gerar chave 2FA
    totp = pyotp.TOTP(pyotp.random_base32())
    secret = totp.secret
    save_user(username, password, secret)

    #Gerar o QR code para o 2FA
    uri = totp.provisioning_uri(username, issuer_name='MyApp')
    qr = qrcode.make(uri)
    qr.save(f'{username}_qrcode.png')

    return jsonify({"message": "User registered successfully", "qrcode": f'{username}_qrcode.png'}), 201

    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


