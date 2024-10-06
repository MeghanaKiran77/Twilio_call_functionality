from flask import Flask, request

app = Flask(__name__)

@app.route('/incoming-call', methods=['POST'])
def incoming_call():
    # Handle the incoming call request here
    return 'OK', 200

@app.route('/status-callback', methods=['POST'])
def status_callback():
    call_status = request.form.get('CallStatus')
    print(f"Call Status: {call_status}")
    return '', 200

if __name__ == '__main__':
    app.run(port=3000)
