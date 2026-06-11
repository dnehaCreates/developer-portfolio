marked_price = float(input("Enter marked price of the book: "))
discount = float(input("Enter discount percentage: "))

selling_price = marked_price - (marked_price * discount / 100)

print("Selling Price of the book:", selling_price)