import time
from web3 import Web3
from config import SETTING
from config import w3


abi = """[{"inputs":[{"internalType":"address","name":"_cofixRouter","type":"address"},{"internalType":"address",
"name":"_uniRouter","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{
"internalType":"uint256","name":"ethAmount","type":"uint256"},{"internalType":"uint256","name":"deadline",
"type":"uint256"}],"name":"doitForCofix","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{
"internalType":"uint256","name":"ethAmount","type":"uint256"},{"internalType":"uint256","name":"deadline",
"type":"uint256"},{"internalType":"uint256","name":"cofiPrice","type":"uint256"}],"name":"doitForCofixGetCofi",
"outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"ethAmount",
"type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"doitForUni","outputs":[],
"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"ethAmount",
"type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256",
"name":"cofiPrice","type":"uint256"}],"name":"doitForUniGetCofi","outputs":[],"stateMutability":"payable",
"type":"function"},{"inputs":[],"name":"getCofixRouter","outputs":[{"internalType":"address","name":"",
"type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getETHBalance","outputs":[{
"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{
"internalType":"uint256","name":"gasLimit","type":"uint256"}],"name":"getGasFee","outputs":[{
"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],
"name":"getNestPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view",
"type":"function"},{"inputs":[],"name":"getSuperMan","outputs":[{"internalType":"address","name":"",
"type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token",
"type":"address"}],"name":"getTokenBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],
"stateMutability":"view","type":"function"},{"inputs":[],"name":"getUniRouter","outputs":[{"internalType":"address",
"name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"moreETH","outputs":[],
"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_cofixRouter",
"type":"address"}],"name":"setCofixRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[
{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"setNestPrice","outputs":[],
"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newMan",
"type":"address"}],"name":"setSuperMan","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{
"internalType":"address","name":"_uniRouter","type":"address"}],"name":"setUniRouter","outputs":[],
"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount",
"type":"uint256"}],"name":"turnOutETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{
"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount",
"type":"uint256"}],"name":"turnOutToken","outputs":[],"stateMutability":"nonpayable","type":"function"},
{"stateMutability":"payable","type":"receive"}] """

contractObj = w3.eth.contract(address=Web3.toChecksumAddress(SETTING["CONTRACT_ADDRESS"]), abi=abi)


def doitForUni(ethAmount):
    tx_dic = contractObj.functions.doitForUni(ethAmount, int(time.time())).buildTransaction({
        'from': SETTING["WALLET_ADDRESS"],
        'gas': 800000,
        'value': ethAmount + w3.toWei('0.01', 'ether')
    })
    return tx_dic


def doitForCofix(ethAmount):
    tx_dic = contractObj.functions.doitForCofix(ethAmount, int(time.time())).buildTransaction({
        'from': SETTING["WALLET_ADDRESS"],
        'gas': 800000,
        'value': ethAmount + w3.toWei('0.01', 'ether')
    })
    return tx_dic


