from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import UserForm, ProductForm
from .models import db, Users, Products, Orders
from datetime import datetime

user_bp = Blueprint("user_bp", __name__,
                    template_folder="templates")

@user_bp.route("/")
def home():
    users = Users.query.all()
    orders = Orders.query.all()
    products = Products.query.all()
    return render_template("index.html", data={"users":users, "orders":orders, "products":products})

@user_bp.route("/user_register", methods=["GET", "POST"])
def user_register():
    form = UserForm()
    if form.validate_on_submit():
        try:
            user = Users(username=form.username.data, email=form.email.data, phone=form.phone.data)
            db.session.add(user)
            db.session.commit()
            print(user.id)
            order = Orders(user_id=user.id,total_price=form.total_price.data,created_at=datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'))
            db.session.add(order)
            db.session.commit()
            flash("Created Successfully")
            return redirect(url_for("user_bp.home"))
        except Exception as e:
            print(e)
            flash("Something Went wrong!!")
            return redirect(url_for('user_bp.user_register'))
    return render_template("user_register.html", form=form)


@user_bp.route("/product_register", methods=["GET", "POST"])
def product_register():
    form = ProductForm()
    if form.validate_on_submit():
        try:
            product = Products(name=form.product_name.data, price=form.product_price.data)
            db.session.add(product)
            db.session.commit()
            flash("Created Successfully!")
            return redirect(url_for('user_bp.home'))
        except Exception as e:
            print(e)
            flash("Something Went Wrong")
            return redirect(url_for('user_bp.product_register'))
    return render_template("products.html", form=form)