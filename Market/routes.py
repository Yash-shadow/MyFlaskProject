from flask import redirect, url_for, flash, session, request

from Market import app, render_template

from Market.models import PetType, Pet, User, Item
from Market.forms  import RegistrationForm, LoginForm, PurchaseForm, SellItemForm

from flask_wtf import csrf

from flask_login import login_user, logout_user, current_user, login_required

from sqlalchemy import or_

from Market import db


@app.route('/')
@app.route('/home')
def homepage():


    return render_template("homepage.html")


@app.route('/<string:pet_type>')
def pets(pet_type):
    pets = Pet.query.all()
    return render_template("pets.html", pets=pets)




# # Route for the form
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = MyForm()
#     if form.validate_on_submit():
#         # Process the form data (e.g., save to database)
#         name = form.name.data
#         # For demonstration, we just print the data
#         print(f"Received name: {name}")
#         return redirect(url_for('success'))
#     return render_template('index.html', form=form)

# # Route for the success page
# @app.route('/success')
# def success():
#     return "Form submitted successfully!"
@app.route('/market',methods=['POST', 'GET'])
@login_required
def market_page():
    purchase_form = PurchaseForm()
    selling_form = SellItemForm()
    if request.method == 'POST'and purchase_form.validate_on_submit():
        purchased_item = request.form.get('I CURSE MYSELF')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            p_item_object.item_buying(current_user)
            flash(f'You have bought a cursed Object {p_item_object.name}', category="danger")
            return redirect(url_for("market_page"))
        
    if request.method == 'POST'and selling_form.validate_on_submit():
        selling_item = request.form.get('Stack Up')
        print(selling_item)
        s_item_object = Item.query.filter_by(name=selling_item).first()
        if s_item_object:
            s_item_object.item_selling()
            flash(f'You got rid of a cursed Object {s_item_object.name} but not the curse JK', category="danger")
            return redirect(url_for("market_page"))


    if request.method == 'GET':
        items = Item.query.filter(or_(Item.owner==None, Item.owner!=current_user.id)).all()
        print(items)
        owned= Item.query.filter(Item.owner==current_user.id).all()
        return render_template('market.html', items=items, owned=owned, purchase_form=purchase_form,selling_form=selling_form)
    
    


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user= User(username= form.username.data, email_address=form.email_address.data,
                    password = form.password.data)
        try:
            db.session.add(user)
        except db.SessionError:
            print(db.sessionErr)
        
        db.session.commit()
        attempted_user =user
        login_user(attempted_user)
        flash(f'Account created successfully and logged in as  {attempted_user.username}', category='success')
        return redirect(url_for('market_page'))

    if form.errors !={}: 
        for err_mssage in form.errors.values():
            # print(f'There was an error with the creating an user : {err_mssage }', category= 'danger')
            flash(f'There was an error with the creating an user : {err_mssage}', category='danger')
    return render_template("register.html", form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
   

    if form.validate_on_submit():
        print(User.query.all())
        attempted_user =  User.query.filter_by(username=form.username.data).first()

        if attempted_user and attempted_user.check_password(
            attempted_password=form.password.data
            ):
            login_user(attempted_user)
            flash(f'Login successful {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash(f'Incorrect details {attempted_user.username}',category='danger')
              
    return render_template("login.html", form=form)




@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user() 
        flash(f'Logout successful', category='info')
    
    return redirect(url_for('homepage'))





# @app.route('/example/<int:pageNo>', methods=['GET'])
# def example_table(pageNo=1):
#    # Fetch users from row 10 to 20 (assuming 1-based index)

#     per_page = 10
#     start_index = 1 + per_page*(pageNo-1)
#     end_index = (pageNo) *per_page

#     tems = example.query.filter(example.id >= start_index, example.id <= end_index).all()
#     print(start_index,end_index,tems)
#     # result = [{'id': example.id, 'value': example.number} for item in tems]
    
    
#     return render_template("example.html", result=tems)