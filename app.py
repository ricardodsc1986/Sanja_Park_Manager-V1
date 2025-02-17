from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

# Conexão com o banco de dados
def get_db_connection():
    conn = mysql.connector.connect(
        host='http://localhost:5000',
        user='root',
        password='password',
        database='estacionamento'
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM registros_veiculos')
    veiculos = cursor.fetchall()
    conn.close()
    return render_template('index.html', veiculos=veiculos)

@app.route('/registrar_entrada', methods=['POST'])
def registrar_entrada():
    placa = request.form['placa']
    entrada = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO registros_veiculos (placa, entrada) VALUES (%s, %s)', (placa, entrada))
        conn.commit()
        flash('Entrada registrada com sucesso!', 'success')
    except mysql.connector.Error as err:
        flash(f'Erro ao registrar entrada: {err}', 'error')
    finally:
        conn.close()
    return redirect(url_for('index'))

@app.route('/registrar_saida/<placa>')
def registrar_saida(placa):
    saida = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE registros_veiculos SET saida = %s WHERE placa = %s', (saida, placa))
        conn.commit()
        flash('Saída registrada com sucesso!', 'success')
    except mysql.connector.Error as err:
        flash(f'Erro ao registrar saída: {err}', 'error')
    finally:
        conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)