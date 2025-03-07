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

@app.route('/hospital_facility')
@login_required
def hospital_facility():
    return render_template('hospital_facility.html')

@app.route('/public_complex_facility')
@login_required
def public_complex_facility():
    return render_template('public_complex_facility.html')

@app.route('/private_complex_facility')
@login_required
def private_complex_facility():
    return render_template('private_complex_facility.html')

@app.route('/optic_facility')
@login_required
def optic_facility():
    return render_template('optic_facility.html')

@app.route('/pharmacy_facility')
@login_required
def pharmacy_facility():
    return render_template('pharmacy_facility.html')

@app.route('/dental_facility')
@login_required
def dental_facility():
    return render_template('dental_facility.html')

@app.route('/laboratories_facility')
@login_required
def laboratories_facility():
    return render_template('laboratories_facility.html')

@app.route('/support_services_facility')
@login_required
def support_services_facility():
    return render_template('support_services_facility.html')

@app.route('/eg')
@login_required
def eg():
    return render_template('eg.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))