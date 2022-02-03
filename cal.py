import math
from datetime import datetime, time
import calendar
import json
from flask import Flask, json, render_template, jsonify, request
from numpy import integer

#from flask_restful import Resource

t = time()


class Calculations:
    with open('app.json') as f:
            d = json.load(f)
            print(d)
            num_items = ['number_of_items']
            delivery_distance = ['delivery_distance']
            cart_value = ['cart_value']
            t = ['time']

    def __init__(self, cart_value=None,delivery_distance=None, num_items=None, time=None ,delivery_fee=None):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.num_items = num_items
        self.time = time
        self.delivery_fee = delivery_fee
        
    #Dan = Calculations(790, 2235, 4, "2021-10-12T13:00:00Z", {self.delivery_fee})
    def calc(self):
            # calculations
            surcharge = 10 - self.cart_value if self.cart_value < 10 else 0
            delivery_distance_fee = math.ceil(
                self.delivery_distance / 500) if self.delivery_distance > 500 else 1
            surcharge = int( 0 if self.cart_value <= 4 else 0.50 * self.num_items)
            self.delivery_fee = delivery_distance_fee + surcharge
            if self.delivery_fee > 15:
                self.delivery_fee = 15
            elif self.cart_value >= 100:
                self.delivery_fee = 0

            Friday_rush = calendar.FRIDAY
            start = '15:00:00'
            enda = '19:00:00'
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            while (Friday_rush and current_time >= start):
                self.delivery_fee = self.delivery_fee * 1.1
            if current_time <= enda:
                self.delivery_fee = self.delivery_fee
            elif self.delivery_fee > 15:
                self.delivery_fee = 15
            return self.delivery_fee
            
#print(Calculations.calc(cart_value, delivery_distance, num_items, t))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        with open('app.json') as f:
            d = json.load(f)
        #data = request.json()
        #result = obj.self.delivery_fee
        return jsonify(
            {'data': d},
            {'delivery fee': "closer to victory"},
            {'result': Calculations.delivery_fee}
        )

@app.route('/<int:num>', methods = ['GET'])
def disp(num):
    
    return jsonify({'data': num**2})

if __name__ == '__main__':
    
    app.run(debug = True)