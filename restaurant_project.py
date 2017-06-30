from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    return "Restaurants"

@app.route('/restaurants/new')
def newRestaurant():
    return "New restaurant"

@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant():
    return "Edit restaurant"

@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant():
    return "Delete restaurant"

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu():
    return "Menu items"

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem():
    return "New menu item"

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem():
    return "Edit menu item"

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem():
    return "Delete menu item"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)