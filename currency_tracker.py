import requests
import pandas as pd
from datetime import datetime

def fetch_and_save_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    try:

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rates = data["rates"]

        usd_amount = float(input("أدخل المبلغ بالدولار ($):"))
        print(f"\n--- قيمة {usd_amount}$ بالعملات الاخرى ---")
        target_currencies = ["EGP", "EUR", "SAR"]
        converted_values = []

        for currency in target_currencies:
            converted_val = usd_amount * rates[currency]
            converted_values.append(converted_val)
            print(f"{currency}: {converted_val:.2f}")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = {
            "Timestamp": [current_time] * len(target_currencies),
            "Currency": target_currencies,
            "Rate_vs_USD": [rates[c] for c in target_currencies],
            "Entered_USD":[usd_amount] * len(target_currencies),
            "Converted_amount": converted_values
        }

        df = pd.DataFrame(log_data)
        file_path = "exchange_rates_log.csv"
        df.to_csv(file_path, mode='a', header=not pd.io.common.file_exists(file_path), index=False)
        print("تم حساب التحويلات وتسجيل التقرير بنجاح في الشيت exchange_rates_log.csv!")
        
    except requests.exceptions.RequestException as e:
        print(f"خطأ في الاتصال بالشبكة :{e}") 

    except ValueError:
        print("خطأ يرجى ادخال رقم صحيح للمبلغ")

if __name__ == "__main__":
    fetch_and_save_rates()