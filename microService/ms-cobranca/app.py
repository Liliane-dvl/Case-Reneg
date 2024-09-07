from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

DATABASE = 'debts.db'  # Nome do banco de dados

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/check_debts', methods=['GET'])
def check_debts():
    conn = get_db()
    cursor = conn.cursor()
    
    # Calcular a data limite
    today = datetime.today()
    cutoff_date = today - timedelta(days=180)
    
    # Consultar dívidas vencidas nos últimos 180 dias
    cursor.execute("SELECT * FROM debts WHERE due_date >= ?", (cutoff_date.strftime('%Y-%m-%d'),))
    debts = cursor.fetchall()
    
    # Categorizar dívidas
    categorized_debts = {'sms': [], 'email': [], 'call': []}
    for debt in debts:
        contact_method = debt['contact_method']
        if contact_method in categorized_debts:
            categorized_debts[contact_method].append({
                'customer_id': debt['customer_id'],
                'amount': debt['amount'],
                'due_date': debt['due_date']
            })
    
    conn.close()
    
    return jsonify(categorized_debts)

if __name__ == '__main__':
    app.run(debug=True)
