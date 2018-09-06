import hashlib
import json
from time import time

class Blockchain:

    def __int__(self):

        self.chain = []
        self.transactions = []

        self.new_block(100,1)

    def new_block(self,proof,previousHash = None):

        block = {
            "index" : len(self.chain) + 1,
            "timestamp" : time(),
            "transactions" : self.transactions,
            "proof" : proof,
            "previousHash" : previousHash or hash(self.chain[-1])
        }

        self.chain.append(block)
        self.transactions = []

        return block

    def new_transaction(self,sender,recipient,amount):

        self.transactions.append({
            "sender": sender,
            "recipient" : recipient,
            "amount" : amount
        })

        return self.last_block["index"] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):

        proof = 0

        while self.valid_proof(last_proof,proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):

        str = f'{last_proof}*{proof}'.encode()
        str = hashlib.sha256(str).hexdigest()
        return str[:4] == "0000"
