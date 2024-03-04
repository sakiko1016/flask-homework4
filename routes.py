from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User

@app.route('/register', methods=['POST'])
def register():
  # Register user logic
  ...

@app.route('/login')  
def login():
  # Login user logic
  ...
  
@app.route('/cars', methods=['GET', 'POST'])
@token_required
def cars(current_user):

  if request.method == 'GET':
    cars = Car.query.all()
    return jsonify([car.to_dict() for car in cars])

  if request.method == 'POST': 
    # Create car logic
    ...

  return jsonify(car.to_dict()), 201

@app.route('/cars/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def car(current_user, id):

  car = Car.query.get(id)
  if not car:
    return jsonify({'message': 'Car not found'}), 404
  
  if request.method == 'GET':
    return jsonify(car.to_dict())
  
  if request.method == 'PUT':
    # Update car logic
    ...

  if request.method == 'DELETE':
    # Delete car logic
    ...

  return jsonify(car.to_dict())

if __name__ == '__main__':
    app.run()