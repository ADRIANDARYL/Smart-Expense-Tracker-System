from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Expense

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/dashboard')
@login_required
def home():

    expenses = Expense.query.filter_by(
        user_id=current_user.id
    ).all()

    total_expenses = sum(exp.amount for exp in expenses)

    recent_transactions = expenses[-5:]

    return render_template(
        'dashboard.html',
        total_expenses=total_expenses,
        recent_transactions=recent_transactions
    )