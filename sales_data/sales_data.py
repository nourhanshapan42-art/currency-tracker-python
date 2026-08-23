try:
    with open("sales_data.csv","r") as file:
        header = next(file)
        total_revenue = 0
        max_quantity = 0
        most_sold_product = ""
        max_revenue = 0
        highest_revenue = ""
        category_totals = {}
        for line in file:
            data = line.strip().split(',')
            product = data[0]
            category = data[1]
            try:
                quantity = int(data[2])
                price = float(data[3])
            except ValueError:
                 print(f"تنبيه: تم تخطي سطر يحتوي على بيانات غير رقمية: {data}")
                 continue  # الانتقال للسطر التالي فوراً
            product_revenue = quantity * price
            total_revenue += product_revenue
            category_totals[category]=category_totals.get(category, 0) + product_revenue
            if quantity > max_quantity:
                max_quantity = quantity
                most_sold_product = product
            if product_revenue > max_revenue:
                max_revenue = product_revenue
                highest_revenue = product
        # print(data) 
        # print(product_revenue)
# print(f"Total Revenue: {total_revenue}")  
# print(most_sold_product)
# print(highest_revenue) 
# print(category_totals)    

    with open ("sales_summary.txt","w") as summary_file:

        summary_file.write("=== SALES SUMMARY REPORT ===\n")
        summary_file.write(f"Total Revenue: ${total_revenue}\n")
        summary_file.write(f"Most Sold Product: {most_sold_product} ({max_quantity} units)\n")
        summary_file.write(f"Highst Revenue Product: {highest_revenue} (${max_revenue})\n\n")
        summary_file.write("Revenue by Category:\n")
        for category_name, category_rev in category_totals.items():
                summary_file.write(f"- {category_name}: ${category_rev}\n")
    print("Report generated successfully!")
except FileNotFoundError:
     print("خطأ لم يتم العثور على الملف:sales_data.csv!")