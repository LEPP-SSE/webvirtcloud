from crypt import methods
import sys
import os
import libvirt
from flask import Flask, request
from vrtManager.connection import CONN_TCP
from vrtManager.instance import wvmInstance

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appsettings.settings")

app = Flask(__name__)


#index route
@app.route('/')
def index():
    return "welcome to webvirtcloud api"


#get uuid via libvirt api
@app.route('/uuid-libvirt', methods=['GET'])
def listVmsLibvirt():
    domain = request.args.get('domain')
    try:
        conn = libvirt.open("qemu+tcp://192.168.0.2/system")
    except libvirt.libvirtError:
        print('failed to open connection to the hypervisor')
        sys.exit(1)

    try:
        domain = conn.lookupByName(domain)
    except libvirt.libvirtError:
        print('failed to find the main domain')
        sys.exit(1)

    return str(domain.UUIDString())


#get uuid via webvirtcloud functionality
@app.route('/uuid-webvirtcloud', methods=['GET'])
def listVmsWebvirtcloud():
    domain = request.args.get('domain')
    inst = wvmInstance('192.168.0.2', 'root', 'INSTALLMANAGER', CONN_TCP, domain)
    return str(inst.get_uuid())


#send request to the endpoints via:
# curl "http://localhost:5000/uuid-webvirtcloud?domain=docker-host-linux-2020"
