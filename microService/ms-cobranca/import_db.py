import sqlite3

conn = sqlite3.connect('debts.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE debts (
        id INTEGER PRIMARY KEY,
        customer_id TEXT,
        amount REAL,
        due_date DATE,
        contact_method TEXT
    )
''')

# Inserir alguns dados de exemplo
c.execute('''
    INSERT INTO debts (customer_id, amount, due_date, contact_method)
    VALUES ('customer1', 100.0, '2024-01-01', 'sms'),
           ('customer2', 200.0, '2024-05-01', 'email'),
           ('customer3', 300.0, '2024-07-01', 'call')
''')

conn.commit()
conn.close()
