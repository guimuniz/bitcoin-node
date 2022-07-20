# mudar nome do arquivo

from client import BitcoinNodeClient

# passar url pra env var -> prettyconf
bitcoin_node = BitcoinNodeClient("http://foo:bar@0:18332/")


def node_is_sync():
    try:
        response = bitcoin_node.get_chain_status()
    except Exception as e:
        return {"error": str(e)}

    status = response["result"][0]["status"]

    is_sync = True if status == "active" else False

    return is_sync
