from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/mes', methods=['POST'])
def handle_post_request():
    values = request.get_json()
    tag = values['tag']
    data = values['data']
    
    print(f"[{datetime.datetime.now().time()}]tag: {tag}, data: {data}")
    
    return 'Success'

@app.route('/synced/mes', methods=['POST'])
def handle_post_request2():
    values = request.get_json()
    temperature = values['temperature'] or None
    rpm = values['RPM'] or None
    
    print(f"[{datetime.datetime.now().time()}]temp: {temperature}, rpm: {rpm}")
    
    return 'Success'

if __name__ == '__main__':
    app.run()
