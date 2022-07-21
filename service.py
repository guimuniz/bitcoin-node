# mudar nome do arquivo

from decimal import Decimal
from client import BitcoinNodeClient

# passar url pra env var -> prettyconf
bitcoin_node = BitcoinNodeClient("http://foo:bar@0:18332/")


def node_is_sync():
    try:
        response = bitcoin_node.get_chain_status()
    except Exception as error:
        raise Exception(error)

    status = response["result"][0]["status"]

    is_sync = True if status == "active" else False

    return is_sync


def get_fee_until_two_blocks():
    try:
        response = bitcoin_node.get_estimate_fee(2)
    except Exception as error:
        raise Exception(error)

    fee = response["result"]["feerate"]
    fee_in_byte = fee / 1000
    final_fee = f"{fee_in_byte:.8f}"

    return final_fee
