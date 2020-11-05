import hashlib
import json
from flask import Flask


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash=0)

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain)+1,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_previous_block(self):
        return self.chain[-1]


app = Flask(__name__)
blk = Blockchain()


@app.route('/mine_block')
def mine_block():
    previous_block = blk.get_previous_block()

    previous_hash = blk.hash(previous_block)

    block = blk.create_block(previous_hash)

    response = {
        'Message': 'Your block is mined',
        'index': block['index'],
        'previous_hash': block['previous_hash']
    }
    return response


@app.route('/get_chain')
def get_chain():
    response = {
        'chain': blk.chain,
        'length': len(blk.chain)
    }
    return response


app.run()
