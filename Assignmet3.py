product_price = float(input("Enter the product price: "))
# Assuming 18% GST
product_gst = (product_price * 18) / 100  
MRP = product_price + product_gst
print("Product Price:", product_price)
print("Product GST:", product_gst)
print("MRP of Product:", MRP)
