#  Q1
def add_money(p_money, p_balance):
    a = [5,10,20,50,100]
    if p_money in a:
        p_balance = p_money + p_balance
    else:
        print('invalid input')
    return ('Your balance:',p_balance)

b = add_money(10,2)
print(b)

goods_list = ['apple','orange','cola','juice','banana']
price_list = [3,4,5,6,4]
def show_goods():
    global goods_list
    global price_list
    print('Goods'.ljust(10),'price')
    for i in range(len(goods_list)):
        print(goods_list[i].ljust(10),price_list[i])
    return

def buy_goods(p_balance, p_name, p_number = 1):
    global goods_list
    global price_list
    if p_name not in goods_list:
        print('No this item')
        print('Your balance', p_balance)
        return
    ind = goods_list.index(p_name)
    total_price = price_list[ind] * p_number
    if total_price > p_balance:
        print('unsuccessful')
        print('Your balance', p_balance)
        return
    else:
        print('successful')
        print('Your balance',p_balance - total_price)
        return

