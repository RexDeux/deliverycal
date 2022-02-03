import math
from datetime import datetime, time
import datetime as DT
import dateutil.relativedelta as REL
import json
from flask import Flask, json, render_template, jsonify, request
from numpy import integer

#from flask_restful import Resource
class Calculations():
    with open('app.json') as f:
            d = json.load(f)
            print(d)
            num_items = ['number_of_items']
            delivery_distance = ['delivery_distance']
            cart_value = ['cart_value']
            time = ['time']

    def __init__(self, cart_value,delivery_distance, num_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.num_items = num_items
        self.time = datetime.strptime(time, '%b %d %Y %I:%M%p')
        
    def surcharge(self):
        b = (10 - self.cart_value if self.cart_value < 10 else 0)
        return(b)
    
    def delivery_distance_fee(self):
        a = self.delivery_distance_fee = math.ceil(
            self.delivery_distance / 500) if self.delivery_distance > 500 else 1
        self.surcharge = int( 0 if self.cart_value <= 4 else 0.50 * self.num_items)
        return(a)
        
    def friday_rush(self):
        #today = DT.date.today()
        #now = DT.datetime.now()
        today = DT.date.today()
        now = DT.datetime.now()
        rd = REL.relativedelta(days=1, weekday=REL.FR)
        next_friday = today + rd
        start = DT.datetime.combine(DT.date.today(), DT.time(hour=15))
        end = DT.datetime.combine(DT.date.today(), DT.time(hour=19))
        delivery_fee = (Calculations.delivery_distance_fee(self) + Calculations.surcharge(self))
        while next_friday:
            if self.time < "T15:00:00Z":
                delivery_fee * 1.1
            elif self.time > "T19:00:00Z":
                delivery_fee * 1
        return(delivery_fee)

demo1 = Calculations(790, 2235, 4, "2022-02-04T16:00:00Z")
print('Your surcharge is:',demo1.surcharge(),'euros')
print('Your delivery distance fee is:',demo1.delivery_distance_fee(),'euros')
#print('Your total fee is:',demo1.surcharge() + demo1.delivery_distance_fee())
print('Your delivery fee is', demo1.friday_rush())

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