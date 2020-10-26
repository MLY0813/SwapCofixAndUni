# SwapCofixAndUni

## Contract part

The contract currently realizes arbitrage between COFIX and UNISWAP. ETH exchange USDT and USDT exchange ETH. After the operation, the contract balance will be checked. If there is a loss of funds, the transaction will fail. In addition, the contract also implements an exchange interface with cofi value, and the cofi mined is also taken into account in the income.

## python

Python simply implements the function of initiating transactions in a loop, querying every 12 seconds. The criterion for initiating a transaction is detecting that the transaction may be successfully executed (there is room for arbitrage). The detailed configuration parameters of the program are in the config file.
