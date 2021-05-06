from model.ledger import Block


def main():
    blockchain = [Block.genesis_block()]
    prev_block = blockchain[0]

    for i in range(0, 5):
        addblock = Block.new_block(prev_block)
        blockchain.append(addblock)
        prev_block = addblock

        print("block id: {}".format(addblock.index))
        print("Timestamp: {}".format(addblock.timestamp))
        print("Hash: {}".format(addblock.hash))
        print("Previous Hash: {}".format(addblock.prevhash))
        print("data: {}\n".format(addblock.data))


if __name__ == "__main__":
    main()