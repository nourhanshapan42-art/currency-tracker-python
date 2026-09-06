order =[
    {"item": "laptop","price":1200,"status":"delivered"},
    {"item": "phone","price":800,"status":"cancelled"},
    {"item": "headphone","price":150,"status":"delivered"},
    {"item": "monitor","price":300,"status":"delivered"}
]
successful_order = [item["price"] for item in order if item["status"] == "delivered"]
total = sum(successful_order)
max_price = max(successful_order)
print(successful_order)
print(total)
print(max_price)