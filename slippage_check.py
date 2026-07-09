# Check if price slippage is within acceptable limits for a swap
def check_slippage(expected_price, execution_price, max_allowed_percent=1.0):
    price_difference = abs(expected_price - execution_price)
    slippage_percent = (price_difference / expected_price) * 100
    
    is_safe = slippage_percent <= max_allowed_percent
    return is_safe, slippage_percent

safe, percent = check_slippage(100.0, 99.2, max_allowed_percent=1.0)
print(f"Slippage: {percent:.2f}% | Transaction Safe to Execute? {safe}")
