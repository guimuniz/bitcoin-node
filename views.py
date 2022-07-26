from flask import Flask, jsonify, request

from service import node_is_sync, get_fee_until_two_blocks
from client import BitcoinNodeClient

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

bitcoin_client = BitcoinNodeClient("http://foo:bar@0:18332/")

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


@app.route("/create-wallet", methods=['POST'])
def generate_wallet():
    json = request.get_json()
    wallet_name = json.get('wallet_name')
    if wallet_name is None:
        return "Missing wallet name", 400

    try:
        response = bitcoin_client.create_wallet(wallet_name)
    except Exception as error:
        return jsonify({"error": str(error)}), 500

    wallet_name = response['result']['name']

    return jsonify({
        'wallet_name': wallet_name
    }), 200

# passar lógica pras views e testar
