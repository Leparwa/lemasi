from flask import  render_template,  request
from werkzeug.utils import redirect
from . import main
from .forms import ProductForm
from .requests import new_book, get_books
from app import  photos



# Views
@main.route('/')
def index():
   return redirect('home')

@main.route('/admin')
def admin():
   return render_template('admin.html')

@main.route('/add-book', methods = ['POST', 'GET'])
def add_book():
    form = ProductForm()
    if form.validate_on_submit():  
       title = request.form.get('title')
       price = request.form.get('price')  
       author = 'lemasi'
       description = request.form.get('description')
       image = request.form.get('image')
       json_data = { "title":title, "price": price, "description": description,  "author": author, "image": image}
       new_book('/pitch', json_data)
    return render_template('create_product.html', productform=form )

@main.route('/home')
def home():
   books = get_books('/pitch')
   return render_template('home.html', books = books)

@main.route('/view-request')
def view_requests():
   return render_template('view_request.html')