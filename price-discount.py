price_product = float(input("How much is the product? $"))
discount = float(input("Select the % of discount: "))
value = (100-discount)/100
newvalue = price_product * value
print(f'Your product cust is ${price_product:.2f} but with discount will be costs ${newvalue:.2f}')