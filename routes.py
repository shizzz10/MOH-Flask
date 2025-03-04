from app import app
from flask import render_template, session, redirect, url_for, flash
from functools import wraps
from forms import sign_in

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('You need to log in first!', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Main index route
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = sign_in()
    if 'logged_in' in session:
        flash('You need to logout first!', 'warning')
        return redirect(url_for('index'))

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

# Facility management routes
@app.route('/add-facility')
@login_required
def add_facility():
    return render_template('add-facility.html')

@app.route('/update-facility')
@login_required
def update_facility():
    return render_template('update-facility.html')

@app.route('/view_facility')
@login_required
def view_facility():
    return render_template('view-facility.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))