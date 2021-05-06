import datetime
import hashlib as h


class Block:
    def __init__(self, index, timestamp, data, prevhash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prevhash = prevhash
        self.hash = self.hash_block()

    def hash_block(self):
        block_encryption = h.sha256()
        ingest = "{}{}{}{}".format(self.index, self.timestamp, self.data, self.prevhash)
        block_encryption.update(ingest.encode('utf-8'))
        return block_encryption.hexdigest()

    @staticmethod
    def genesis_block():
        return Block(0, datetime.datetime.now(), "First block transaction", " ")

    @staticmethod
    def new_block(last_block):
        index = last_block.index + 1
        timestamp = datetime.datetime.now()
        prev_hash = last_block.hash
        data = 'Transaction {}'.format(index)
        return Block(index, timestamp, data, prev_hash)



