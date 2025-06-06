import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, redirect, url_for
from logger_config import ssh_logger, error_logger,http_logger


# logging format
logging_format = logging.Formatter('%(asctime)s %(message)s')

# HTTP Logger
funnel_logger = logging.getLogger('HTTP Logger')
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('http_audits.log',maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)

# Baseline honeypot

def web_honeypot(input_username="admin", input_password="password"):
    
    app = Flask(__name__)

    @app.route('/')
    def index():
        ip = request.remote_addr
        http_logger.info(f"{ip} accessed / with method {request.method}")
        return render_template('wp-admin.html')

    @app.route('/wp-admin-login',methods=['POST'])
    
    def login():
        username = request.form['username']
        password = request.form['password']

        ip_address = request.remote_addr
        http_logger.info(f"{ip_address} attempted login with username: '{username}' and password: '{password}'")

        # funnel_logger.info(f'Client with IP Address: {ip_address} entered\n Username: {username}, Password: {password}')

        if username == input_username and password == input_password:
            return 'RAM RAM BHAIII!'
        else:
            return 'Invalid username or password. Please Try Again.'

    return app

def run_web_honeypot(port=5000,input_username="admin", input_password="password"):
    run_web_honeypot_app = web_honeypot(input_username,input_password)
    run_web_honeypot_app.run(debug=True,port=port,host="0.0.0.0")

    return run_web_honeypot_app


