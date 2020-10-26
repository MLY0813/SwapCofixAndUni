from config import *
from swapContract import *
import time

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    while 1:
        now = int(time.time())
        timeArray = time.localtime(now)

        tx_dic_one = doitForUni(w3.toWei('40', 'ether'))
        try:
            tx_dic_one_gas = w3.eth.estimateGas(tx_dic_one)
        except ValueError:
            print("doitForUni", time.strftime("%Y--%m--%d %H:%M:%S", timeArray))
        else:
            print('success')
            sendTransationWithMoreGas(tx_dic_one, "2")


        tx_dic_two = doitForCofix(w3.toWei('40', 'ether'))
        try:
            tx_dic_two_gas = w3.eth.estimateGas(tx_dic_two)
        except ValueError:
            print("doitForCofix", time.strftime("%Y--%m--%d %H:%M:%S", timeArray))
        else:
            print('success')
            sendTransationWithMoreGas(tx_dic_two, "2")
        time.sleep(SETTING["TIME_SPAN"])


