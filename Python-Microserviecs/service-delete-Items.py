from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_Items01 as us

app = Flask(__name__)

@app.route('/delete', methods=['DELETE'])
def delete():
    # Get the user's login information from the request
    name = request.form.get('name')
    cafe = us.find_cafe_name(name)

    if cafe:
        us.cafe_remove(name)
        return jsonify({'message': 'delete successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot delete user.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1