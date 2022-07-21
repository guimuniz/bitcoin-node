from flask import Flask, jsonify

from service import node_is_sync, get_fee_until_two_blocks

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# resolver o export FLASK_APP=service + export FLASK_ENV=development que é necessário pra rodar


@app.route("/is-sync", methods=['GET'])
def is_sync():
    try:
        is_sync = node_is_sync()
    except Exception as error:
        return jsonify({"error": str(error)}), 500

    return jsonify({
        'is_sync': is_sync
    }), 200


@app.route("/network-fee", methods=['GET'])
def network_fee():
    try:
        fee = get_fee_until_two_blocks()
    except Exception as error:
        return jsonify({"error": str(error)}), 500

    return jsonify({
        'fee': fee
    }), 200
