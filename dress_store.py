# My Dress Store - Black Saree Premium
def calculate_price(dress_type, color):
  base_price = 1000
  if color == "black":
    print("black is premium color!")
    return base_price + 800
    return base_price
    # Test
    price = calculate_price("saree", "black")
    print(f"Tumhari black saree ka price hai: Rs. {price}")
