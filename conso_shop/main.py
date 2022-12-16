import product
import shopclient    
import order

product_1 = product.Product('Cherry Candy', 'candies')
product_2 = product.Product('Apple candy', 'candies')
product_3 = product.Product('Chocolate', 'candies')
product_4 = product.Product('AmericanaCookie', 'cookies')


product_1.procurement(21, 12).procurement(21, 12).procurement(37, 10).set_selling_price(15)
product_2.procurement(64, 4).procurement(21, 8).procurement(37, 3).set_selling_price(8)
product_3.procurement(1, 55).procurement(34, 50).procurement(37, 65).set_selling_price(85)
    
consumer_1 = shopclient.Shopclient('William', 'Sheakespeare')
consumer_2 = shopclient.Shopclient('Sherlock', 'Holmes')
consumer_3 = shopclient.Shopclient('Emmet', 'Brown')
    
consumer_3.get_loyalty_card(58, 'B213412')

order_1 = order.Order(consumer_3)
order_1.add_to_basket(product_1, 1).add_to_basket(product_3, 2).add_to_basket(product_2, 15)
print(order_1)