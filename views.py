from flask import Flask, jsonify

from service import node_is_sync

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# resolver o export FLASK_APP=service + export FLASK_ENV=development que é necessário pra rodar


@app.route("/is-sync", methods=['GET'])
def is_sync():
    try:
        is_sync = node_is_sync()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({
        'is_sync': is_sync
    }), 200
