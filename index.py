from datetime import datetime
import pandas as pd
from pprint import pprint
# separar los datos de prueba
from data import data_customer_order_status, data_seasons_problem, data_detecting_change


def customer_order_status(data):
    groupby_order_number = pd.DataFrame(data).groupby(['order_number'])
    status_level = ["CANCELLED", "SHIPPED", "PENDING"]
    result = []
    for order_number, json_data in groupby_order_number:
        status_final = status_level[0]
        for row in json_data['status']:
            if status_level.index(row) > status_level.index(status_final):
                status_final = row
        result.append({
            'order_number': order_number,
            'status': status_final
        })
    return result


def seasons_problem(data):
    def season(date):
        date = datetime.strptime(date.strftime("%m-%d"), "%m-%d")
        if date >= datetime.strptime("03-19", "%m-%d") and date <= datetime.strptime("06-19", "%m-%d"):
            return "Spring"
        elif date >= datetime.strptime("06-20", "%m-%d") and date <= datetime.strptime("09-21", "%m-%d"):
            return "Summer"
        elif date >= datetime.strptime("09-22", "%m-%d") and date <= datetime.strptime("12-20", "%m-%d"):
            return "Fall"
        else:
            return "Winter"
    return list(map(
        lambda order: {
            'ORD_ID': order['ORD_ID'],
            'SEASON': season(order['ORD_DT'])
        },
        data
    ))


def detecting_change(data):
    return [r for p, r in enumerate(data) if p > 0 and r["was_rainy"] and not(data[p - 1]["was_rainy"])]


def run():
    print("->Customer Order Status")
    print(pd.DataFrame(customer_order_status(data_customer_order_status)))
    print("->Seasons Problem")
    print(pd.DataFrame(seasons_problem(data_seasons_problem)))
    print("->Detecting Change")
    print(pd.DataFrame(detecting_change(data_detecting_change)))


if __name__ == '__main__':
    run()
