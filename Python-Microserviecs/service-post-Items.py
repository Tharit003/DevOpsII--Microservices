from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_Items01 as us

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def register():
    # Get the user's login information from the request
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    cafe = us.cafe_Items_name()
    data = [x for x in cafe if x["name"]==name]
    # return jsonify(_user)
    #Get Data
    if (data):
        return jsonify({'message': 'Cannot create user.'}), 401
    else:
        us.cafe_name_add(name,category,price,instock)
        return jsonify({'message': 'Created successfully.'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True) #127.0.0.1