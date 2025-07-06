from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from models import events
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    event_type = request.headers.get("X-GitHub-Event")

    if event_type == "push":
        data = {
            "type": "push",
            "author": payload['pusher']['name'],
            "to_branch": payload['ref'].split("/")[-1],
            "timestamp": datetime.utcnow()
        }
    elif event_type == "pull_request":
        pr = payload['pull_request']
        data = {
            "type": "pull_request",
            "author": pr['user']['login'],
            "from_branch": pr['head']['ref'],
            "to_branch": pr['base']['ref'],
            "timestamp": datetime.utcnow()
        }
        if payload.get('action') == 'closed' and pr.get('merged'):
            data['type'] = 'merge'
    else:
        return "Event not handled", 200

    events.insert_one(data)
    return "Webhook received", 200

@app.route('/latest')
def latest():
    recent = list(events.find().sort("timestamp", -1).limit(10))
    result = []
    for e in recent:
        ts = e['timestamp'].strftime("%d %B %Y - %I:%M %p UTC")
        if e["type"] == "push":
            msg = f"{e['author']} pushed to {e['to_branch']} on {ts}"
        elif e["type"] == "pull_request":
            msg = f"{e['author']} submitted a pull request from {e['from_branch']} to {e['to_branch']} on {ts}"
        elif e["type"] == "merge":
            msg = f"{e['author']} merged branch {e['from_branch']} to {e['to_branch']} on {ts}"
        else:
            continue
        result.append(msg)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
