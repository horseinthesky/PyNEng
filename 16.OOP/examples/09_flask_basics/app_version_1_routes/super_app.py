from flask import Flask

myapp = Flask(__name__)


@myapp.route('/')
@myapp.route('/home')
def index():
    return 'Hello!'


@myapp.route('/users/<username>')
def user_profile(username):
    return 'Hello, {}'.format(username)


@myapp.route('/reports/<int:report_id>')
def report(report_id):
    #print(type(report_id))
    return 'Report {}'.format(report_id)


@myapp.route('/send_command/<device_ip>/<command>')
def send_command(device_ip, command):
    return 'Sending command {} to device {}'.format(command, device_ip)


if __name__ == '__main__':
    myapp.run(debug=True)

