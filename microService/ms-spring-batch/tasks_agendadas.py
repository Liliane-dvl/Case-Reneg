from models import db, Debt
from datetime import datetime, timedelta

def send_to_bureau(bureau_name, debts):
    # Implementar lógica para enviar dívidas para o bureau de crédito
    print(f"Enviando {len(debts)} dívidas para {bureau_name}")

def process_debts():
    today = datetime.now().date()
    cutoff_date = today - timedelta(days=180)

    debts = Debt.query.filter(Debt.due_date < cutoff_date).all()

    serasa_debts = [debt for debt in debts if debt.contact_method == 'serasa']
    bvs_debts = [debt for debt in debts if debt.contact_method == 'bvs']
    quod_debts = [debt for debt in debts if debt.contact_method == 'quod']

    send_to_bureau('Serasa', serasa_debts)
    send_to_bureau('BVS', bvs_debts)
    send_to_bureau('Quod', quod_debts)
