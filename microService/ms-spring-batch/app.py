from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
from tasks import process_debts

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Debt

# Configuração do agendador
scheduler = BackgroundScheduler()
scheduler.add_job(func=process_debts, trigger="interval", days=1)  # Executa uma vez por dia
scheduler.start()

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/status', methods=['GET'])
def status():
    return "Microserviço está funcionando e o processamento está agendado.", 200

if __name__ == '__main__':
    app.run(debug=True)
