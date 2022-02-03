import math
from datetime import datetime, time
import calendar
import json
from flask import Flask, json, render_template, jsonify, request
from numpy import integer

#from flask_restful import Resource

t = time()


class Calculations():
    with open('app.json') as f:
            d = json.load(f)
            print(d)
            num_items = ['number_of_items']
            delivery_distance = ['delivery_distance']
            cart_value = ['cart_value']
            t = ['time']

    def __init__(self, cart_value,delivery_distance, num_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.num_items = num_items
        self.time = time
        
    #Dan = Calculations(790, 2235, 4, "2021-10-12T13:00:00Z", {delivery_fee})
    def surcharge(self):
        b = (10 - self.cart_value if self.cart_value < 10 else 0)
        return(b)
    
    def delivery_distance_fee(self):
        a = self.delivery_distance_fee = math.ceil(
            self.delivery_distance / 500) if self.delivery_distance > 500 else 1
        self.surcharge = int( 0 if self.cart_value <= 4 else 0.50 * self.num_items)
        return(a)
        
    def friday_rush(self):
        # calculations
        #surcharge = 10 - self.cart_value if self.cart_value < 10 else 0
        Friday_rush = calendar.FRIDAY
        start = '15:00:00'
        end = '19:00:00'
        now = datetime.now()
        #current_time = now.strftime("%H:%M:%S")
        #c = if calendar.FRIDAY + start > end
            #delivery_fee = self.delivery_distance_fee + self.surcharge 
            #elif delivery_fee > 15:
                #delivery_fee = 15
            #else self.cart_value >= 100:
                #delivery_fee = 0
        #return Friday_rush
        #return(self.surcharge + self.delivery_distance_fee)
            
        #while (Friday_rush and current_time >= start):
            #delivery_fee * 1.1
        #if current_time <= enda:
            #delivery_fee = delivery_fee
        #elif delivery_fee > 15:
            #delivery_fee = 15 
        #return(delivery_fee)

demo1 = Calculations(790, 2235, 4, "2021-10-12T13:00:00Z")
print(demo1.surcharge())
print(demo1.delivery_distance_fee())
#print(demo1.happyhour())

#app = Flask(__name__)
#app.config["DEBUG"] = True

#@app.route('/', methods = ['GET', 'POST'])
#def home():
    #if(request.method == 'GET'):
        #with open('app.json') as f:
            #d = json.load(f)
        #data = request.json()
        #result = obj.delivery_fee
        #return jsonify(
            #{'data': d},
            #{'delivery fee': "closer to victory"},
            #{'result': Calculations.cart_value}
        #)
        

#@app.route('/<int:num>', methods = ['GET'])
#def disp(num):
    
    #return jsonify({'data': num**2})

#if __name__ == '__main__':
    
    #app.run(debug = True)