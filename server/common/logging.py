import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import jsonify
from datetime import datetime

log_format = '%(asctime)s [%(levelname)s] - %(name)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)

# Configuring the rotating file handler
log_file_path = './logs/sastaticket.log'
file_handler = RotatingFileHandler(log_file_path, maxBytes=10 * 1024 * 1024, backupCount=2, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(log_format))
