from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from forms import ExpenseForm
from models import Expense
from extensions import db

expenses = Blueprint('expenses', __name__)

@expenses.route('/add_expense', methods=['GET', 'POST'])
@login_required
def add_expense():

    form = ExpenseForm()

    if form.validate_on_submit():

        expense = Expense(
            user_id=current_user.id,
            category=form.category.data,
            amount=form.amount.data,
            description=form.description.data,
            payment_method=form.payment_method.data
        )

        db.session.add(expense)
        db.session.commit()

        return redirect(url_for('dashboard.home'))

    return render_template(
        'add_expense.html',
        form=form
    )