from flask import Flask, jsonify, request

from client import BitcoinNodeClient

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# passar url pra env var -> prettyconf
bitcoin_node_client = BitcoinNodeClient("http://foo:bar@0:18332/")

# resolver o export FLASK_APP=service + export FLASK_ENV=development que é necessário pra rodar


@app.route("/is-sync", methods=['GET'])
def is_sync():
    try:
        response = bitcoin_node_client.get_chain_status()
    except Exception as error:
        return jsonify({"error": str(error)}), 500

    status = response["result"][0]["status"]
    is_sync = True if status == "active" else False

    return jsonify({
        'is_sync': is_sync
    }), 200


@app.route("/network-fee", methods=['GET'])
def network_fee():
    try:
        response = bitcoin_node_client.get_estimate_fee(2)
    except Exception as error:
        return jsonify({"error": str(error)}), 500

    fee = response["result"]["feerate"]
    fee_in_btc_byte = fee / 1000
    fee_in_satoshi_byte = fee_in_btc_byte * 100000000

    return jsonify({
        'fee': fee_in_satoshi_byte
    }), 200


@app.route("/create-wallet", methods=['POST'])
def generate_wallet():
    json = request.get_json()
    wallet_name = json.get('wallet_name')
    if wallet_name is None:
        return "Missing wallet name", 400

    try:
        response = bitcoin_node_client.create_wallet(wallet_name)
    except Exception as error:
        return jsonify({"error": str(error)}), 500

    wallet_name = response['result']['name']

    return jsonify({
        'wallet_name': wallet_name
    }), 200


@app.route("/balance", methods=['GET'])
def get_balance():
    try:
        response = bitcoin_node_client.get_balance()
    except Exception as error:
        return jsonify({"error": str(error)}), 500

    balance = response['result']['balance']

    return jsonify({
        'balance': balance
    }), 200
