#from .models import City
#from .forms import CityForm
import math
from datetime import datetime, time
import calendar
import json
from flask import Flask, json, render_template, request, jsonify

t = time()


class Calculations:
    def calc(param):
        with open('app.json') as f:
            d = json.load(f)
            print(d)
            num_items = int(param['number_of_items'])
            delivery_distance = int(param['delivery_distance'])
            cart_value = int(param['cart_value'])
            time = param['time']
            Friday_rush = calendar.FRIDAY
            start = '15:00:00'
            enda = '19:00:00'
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            # calculations
            surcharge = 10 - cart_value if cart_value < 10 else 0
            base_fee = 2
            delivery_distance_fee = math.ceil(
                delivery_distance / 500) if delivery_distance > 500 else 1
            surcharge = 0.50
            surcharge = 0 if cart_value <= 4 else 0.50 * num_items
            delivery_fee = delivery_distance_fee + surcharge
            if delivery_fee > 15:
                delivery_fee = 15
            elif cart_value >= 100:
                delivery_fee = 0

            while (Friday_rush and current_time >= start):
                delivery_fee = delivery_fee * 1.1
            if current_time <= enda:
                delivery_fee = delivery_fee
            elif delivery_fee > 15:
                delivery_fee = 15
            break

            return delivery_fee


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/cal', methods=['GET', 'POST'])
def calc():
    param = request.json
    result = Calculations.calc(param)

    return {"result": result}


app.run()
