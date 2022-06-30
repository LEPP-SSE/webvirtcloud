from flask import Flask, request
from vrtManager.hostdetails import wvmHostDetails

from vrtManager.connection import wvmConnection

app = Flask(__name__)

@app.route('/')
def index():
    return "welcome to webvirtcloud api"

@app.route('/list')
def listVms():
    connection = wvmConnection('10.10.120.75', 'root', '', 'CONN_TCP')
    hostDetails = wvmHostDetails(connection)
    return str(hostDetails)