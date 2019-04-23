import time
import os

import redis
from flask import url_for, send_from_directory, render_template, redirect, request, make_response, jsonify
from flask_security import login_required, current_user, roles_required

from CodeRx import app

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect("/homepage", code=302)
    else:
        return render_template('index.html')

@app.route('/editor')
@login_required
def editor():
    return render_template('editor.html', title='Editor')

@app.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html', title='Homepage')

@app.route('/class_management')
# @roles_required('admin')
@login_required
def class_management():
    return render_template('class_management.html', title='Class Management')

@app.route('/admin')
@login_required
@roles_required('admin')
def admin():
    return render_template('admin_page.html', title='Administrator Tools')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Edit Profile')

@app.route('/single_problem')
@login_required
def single_problem():
    return render_template('view_single_problem.html', title='View Problem')

@app.route('/user_submissions')
@login_required
def user_submissions():
    return render_template('view_user_submissions.html', title='All User Submissions')

@app.route('/terminal')
def terminal():
    return render_template('terminal.html')

@app.route('/403')
def error_403():
    return render_template('errors/403.html')

@app.route('/job_complete', methods=['POST'])
def job_complete():
    app.logger.info(request.json)
    return make_response(jsonify({'result': 'job completed successfully'}), 200)