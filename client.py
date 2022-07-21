import requests


class BitcoinNodeClient:
    def __init__(self, url):
        self.url = url

    def get_chain_status(self):
        response = requests.post(
            url=self.url,
            json={"method": "getchaintips", "params": []},
        )
        if response.status_code != 200:
            raise Exception("Error connecting to node")

        return response.json()

    def get_estimate_fee(self, conf_target):
        response = requests.post(
            url=self.url,
            json={"method": "estimatesmartfee", "params": [conf_target]},
        )
        if response.status_code != 200:
            raise Exception("Error connecting to node")

        return response.json()
