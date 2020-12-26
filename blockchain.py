import hashlib
import json
'''
json 是一个轻量级的数据交换格式，易于阅读和编写
py重的json库是用来编码和解码 JSON 对象的
'''
from time import time
from uuid import uuid4
'''
通用唯一标识符 ( Universally Unique Identifier )，
对于所有的UUID它可以保证在空间和时间上的唯一性，也称为GUID，全称为：
UUID —— Universally Unique IDentifier  Python中称为 UUID
它是通过MAC地址、 时间戳、 命名空间、 随机数、 伪随机数来保证生成ID的唯一性，
有着固定的大小( 128 bit位 )，通常由 32 字节的字符串（十六进制）表示。
它的唯一性和一致性特点，使得可以无需注册过程就能够产生一个新的UUID；UUID可以被用作多种用途, 
既可以用来短时间内标记一个对象，也可以可靠的辨别网络中的持久性对象。
uuid4:基于随机数,由伪随机数得到，有一定的重复概率，该概率可以计算出来。
'''
class Blockchain(object):

    '''Class Blockchain is designed to manage chains, 
    it is uesed to store tx information,
    and helps to add new block to blockchain'''

    def __init__(self): #有了init方法，实例化类的时候就不能用空参数了，必须与__init__方法匹配的承参数
        self.chain=[]#区块列表
        self.current_transaction=[]#交易列表

    def new_block(self):
        #创建一个新的区块，并把它加到区块中
        pass

    def new_transaction(self,sender,recipient,amount):
        '''
        creates a new tx to go into the next block
        :param sender: <str> address of the sender
        :param recipient: <str> address of the recipient
        :param amount: <int> amount of tx
        :renturn:<int> the index of the block that will hold this tx
        '''
        self.current_transaction.append({
                'sender':sender,
                'recipient':recipient,
                'amount':amount, #这里的，可以不要吗？
        })

        return self.last_block['index']+1
        #添加一个新的交易到交易列表
        pass

    @staticmethod #返回函数的静态方法，该方法不强制要求传递参数，可以不实例化就能调用
    def hash(block):
        #对区块取hash值/hash a block
        #:param block:<dict> Block
        #:return:<str>
        '''we must make sure that the Dictionary is ordered 
        or we'll have inconsistent hashes
        '''

        block_string = json.dumps(block,sort_keys=True).encode()
        #这里不明白什么意思，sort_keys是告诉编码器按照字典key排序(a到z)输出，为什呢要重新排布一下呢？
        return hashlib.sha256(block_string).hexdigest()


    @property #将函数变成属性调用的函数，即可以用调用属性的形式来调用方法
    def last_block(self):
        #returns the last block in the chain
        return self.chain[-1]#the last chain

    def proof_of_work(self,last_proof):
        '''
        simple proof of work algorithm
        - p is the previous proof,and p' is the new proof
        - find a number p' such that hash(pp') contains leading 4 zeros,
        - where p is the previous p'
        :param last_proof:<int>
        :return:<int>
        '''

        proof=0
        pass

    @staticmethod
    def valid_proof(last_proof,proof):
        """
        validates the proof: 
        Does hash(last_proof,proof) contains 4 leading zeros
        :param last_proof:<int> Previous Proof
        :param proof:<int>Current Proof
        :return:<bool> Ture if  correct,False if not
        """
        guess =f'{last_proof}{proof}'.encode() 
        #f代表格式化字符串常量
        # encode表示以encoding指定的编码格式编码字符串
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4]=="0000"

