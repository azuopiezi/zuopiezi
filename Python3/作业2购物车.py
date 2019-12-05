'''
购物车程序

salary =5000
1. iphone6s 5800
2. macbook 9000
3. coffee 32
4. pythonbook 80
5. bicycle 1500
选择购物商品数字，如果余额不足，显示余额多少
把放到购物车中的商品并显示当前余额：333
如果选择退出
打印出已经购买的商品
付款后，显示余额多少，欢迎下次光临

'''
#salary = 50000

# salary = int(input("Salary:"))

goods = [[1,'Iphone6',5800],
         [2,'Macbook',9000],
         [3,'Coffee',32],
         [4,'Pythonbook',80],
         [5,'Bicycle',1500]
         ]
# print(goods)
# prices = [5800,9000,32,80,1500]
# print(prices)
# flag = [1,2,3,4,5]
# print(flag)
shoppingCar=0

msg='''
-----------------------商品信息-------------
%s

-----------------------END-------------
'''  %(goods)
print(msg)
#
# shoppingCar=goods[0]
# print("放到购物车中的商品为:%s" %shoppingCar)
# sum = salary-prices[0]
# if sum < 0:
#     print("余额为:%d ,请放回此物品%s" %(sum,shoppingCar))
# else:
#     print("余额为:%d" %sum)
#     ###打印出购买的商品和花费
#     print("购买的商品为:%s,共花费:%d" %(shoppingCar,prices[0]))







