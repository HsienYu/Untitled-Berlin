from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
messages = dict()


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/message', methods=['POST'])
def update_message():
    content = request.get_json()
    print(content)
    messages[content['void_id']] = content['msg']
    return jsonify(content)


@app.route('/message', methods=['GET'])
def get_all_message():
    print(messages)
    return jsonify(messages)


@app.route('/message', methods=['DELETE'])
def delete_all_message():
    messages.clear()
    print(messages)
    return jsonify(messages)


@app.route('/message/<void_id>', methods=['GET'])
def get_message(void_id):
    msg = messages.get(void_id)
    return jsonify(msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
