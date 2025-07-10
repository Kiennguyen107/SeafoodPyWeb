
from flask import Flask, request, render_template
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:kiennguyen1106@localhost:5432/Main"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/user/home")
def go_user_home():
    products_from_db = Product.query.all()
    return render_template("/user/home.html", products=products_from_db)


# admin_web
@app.route("/admin/home")
def go_admin_home():
    products_from_db = Product.query.all()
    return render_template("/admin/home.html", products=products_from_db)


# Tìm kiếm
@app.route("/admin/Search/Success")
def search_product_success():
    id = request.args.get("id")
    products = Product.query.filter(Product.id == id)
    bills = Bill.query.filter(Bill.order_id == id)
    return render_template("/admin/Search_Product_Success.html", products=products, bills=bills)


# Tìm kiếm
@app.route("/admin/Search")
def search_product():
    products_from_db = Product.query.all()
    return render_template("/admin/Search_Product.html", products=products_from_db)


# Lấy dữ liệu
@app.route("/admin/product/<product_id>")
def go_admin_product_details(product_id):
    product = Product.query.get(product_id)
    return render_template("/admin/ProductDetails.html", product=product)


# Xóa dữ liệu thành công
@app.route("/admin/product/<product_id>/delete")
def go_admin_delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return render_template("/admin/DeleteProductSuccess.html")


# Cập nhật dữ liệu
@app.route("/admin/product/<product_id>/update")
def go_admin_update_product(product_id):
    product = Product.query.get(product_id)
    return render_template("/admin/UpdateProduct.html", product=product)


# Cập nhật dữ liệu thành công
@app.route("/admin/product/<product_id>/update-product-success")
def go_admin_update_product_success(product_id):

    product = Product.query.get(product_id)
    name = request.args.get("product_name")
    product.name = name
    price = request.args.get("product_price")
    product.price = price
    quantity = request.args.get("product_quantity")
    product.quantity = quantity
    product.last_modified_date = datetime.now()

    db.session.commit()

    return render_template("/admin/UpdateProductSuccess.html")


# Thêm dữ liệu
@app.route("/admin/product/add-new-product")
def go_admin_add_new_product():
    return render_template("/admin/AddNewProduct.html")


# Thêm dữ liệu thành công
@app.route("/admin/product/add")
def go_admin_add_new_product_success():
    name = request.args.get("product_name")
    price = request.args.get("product_price")
    quantity = request.args.get("product_quantity")
    status = "ACTIVE"

    new_product = Product(name=name, price=price, quantity=quantity, status=status, created_date=datetime.now())

    db.session.add(new_product)
    db.session.commit()
    return render_template("/admin/AddNewProductSuccess.html")


# Customer web
@app.route("/customer/SignInfor")
def SignInfor():
    return render_template("/customer/SignInfor.html")


@app.route("/customer/AddNewCusSuccess")
def AddNewCusSuccess():
    name = request.args.get("name")
    phone_number = request.args.get("phone_number")
    address = request.args.get("address")
    created_date = request.args.get("created_date")
    customers = Customer.query.filter(Customer.name == name)

    customer = Customer(name=name, phone_number=phone_number, address=address, created_date=created_date)
    db.session.add(customer)
    db.session.commit()
    return render_template("/customer/AddNewCusSuccess.html", customers=customers)


@app.route("/customer/Inforcus")
def Inforcus():
    customer_new = Customer.query.all()
    return render_template("/customer/Inforcus.html", customers=customer_new)


@app.route("/customer/Search/Success")
def search_customer_success():
    id = request.args.get("id")
    customers = Customer.query.filter(Customer.id == id)
    orders = Order.query.filter(Order.id_cus == id)
    return render_template("/customer/Search_Customer_Success.html", customers=customers, orders=orders)


@app.route("/customer/cus/<customer_id>")
def go_customer_details(customer_id):
    customer = Customer.query.get(customer_id)
    return render_template("/customer/CusDetail.html", customer=customer)


@app.route("/customer/cus/<customer_id>/delete")
def go_cus_delete_Infor(customer_id):
    customer = Customer.query.get(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return render_template("/customer/DeleteInforSuccess.html")


@app.route("/customer/cus/<customer_id>/update")
def go_cus_update_Infor(customer_id):
    customer = Customer.query.get(customer_id)
    return render_template("/customer/UpdateCusInfor.html", customer=customer)


@app.route("/customer/cus/<customer_id>/update-Infor-success")
def go_cus_update_Infor_success(customer_id):

    customer = Customer.query.get(customer_id)
    name = request.args.get("customer_name")
    customer.name = name
    phone_number = request.args.get("customer_phone_number")
    customer.phone_number = phone_number
    address = request.args.get("customer_address")
    customer.address = address
    customer.created_date = datetime.now()

    db.session.commit()

    return render_template("/customer/UpdateCusInforSuccess.html")


@app.route("/user/productoder/<product_id>")
def ProductInfor(product_id):
    product = Product.query.get(product_id)
    return render_template("/user/ProductInfor.html", product=product)


# Order web
@app.route("/user/ClientOrder")
def go_add_order_home():
    products_from_db = Product.query.all()
    return render_template("/user/AddOrder.html", products=products_from_db)


@app.route("/user/order/add")
def go_user_add_order():
    id_cus = request.args.get("id_cus")
    name_PD = request.args.get("name_PD")
    status = "ACTIVE"

    order = Order(name_PD=name_PD, id_cus=id_cus, status=status)

    db.session.add(order)
    db.session.commit()
    return render_template("/user/AddOrderSuccess.html", orders=Order.query.all())


@app.route("/user/Error")
def error():
    return render_template("/user/Error.html")


@app.route("/user/order/<order_id>")
def go_order_details(order_id):
    order = Order.query.get(order_id)
    return render_template("/user/OrderDetail.html", order=order)


@app.route("/user/order/<order_id>/delete")
def go_user_delete_order(order_id):
    order = Order.query.get(order_id)
    db.session.delete(order)
    db.session.commit()
    return render_template("/user/Error.html")


@app.route("/user/order/<order_id>/update")
def go_user_update_order(order_id):
    order = Order.query.get(order_id)
    return render_template("/user/UpdateOrderInfor.html", order=order)


@app.route("/user/order/<order_id>/update-OrderIF-success")
def go_user_update_OrderIF_success(order_id):
    order = Order.query.get(order_id)
    id = request.args.get("id")
    order.id = id
    name_PD = request.args.get("name_PD")
    order.name_PD = name_PD

    db.session.commit()

    return render_template("/user/UpdateOrderIFSuccess.html")


# Bill web
@app.route("/admin/home/bill")
def go_user_bill():
        id = request.args.get("id")
        order_id = request.args.get("order_id")
        quantity = request.args.get("quantity")
        total_money = request.args.get("total_money")

        bill = Bill(order_id=order_id, id=id, quantity=quantity, total_money=total_money)

        db.session.add(bill)
        db.session.commit()
        return render_template("/admin/Check_Bill.html", bills=Bill.query.all())


@app.route("/admin/Search_bill/Success")
def search_bill_success():
    order_id = request.args.get("order_id")
    products = Product.query.filter(Product.id == order_id)
    bills = Bill.query.filter(Bill.order_id == order_id)
    return render_template("/admin/Search_Bill_Success.html", products=products, bills=bills)


# Tìm kiếm
@app.route("/admin/Search_bill")
def search_bill():
    bill = Bill.query.all()
    return render_template("/admin/Search_Bill.html", bills=bill)


@app.route("/admin/billfill/")
def go_fill_out_bill():  # Tham số
    product = Product.query.all()
    order = Order.query.all()
    return render_template("/admin/Fill_out_bill.html", products=product, orders=order)


@app.route("/admin/billdetail/")
def go_admin_bill_details():
    bill = Bill.query.all()
    return render_template("/admin/Detail_Bill.html", bills=bill)


@app.route("/admin/bill/<bill_id>/delete")
def go_admin_delete_bill(bill_id):
    bill = Bill.query.get(bill_id)
    db.session.delete(bill)
    db.session.commit()
    return render_template("/user/Error.html")


@app.route("/admin/bill/<bill_id>/update")
def go_admin_update_bill(bill_id):
    bill = Bill.query.get(bill_id)
    return render_template("/admin/UpdateBillInfor.html", bill=bill)


@app.route("/admin/bill/<bill_id>/update-bill-success")
def go_admin_update_bill_success(bill_id):
    bill = Bill.query.get(bill_id)
    id = request.args.get("id")
    bill.id = id
    order_id = request.args.get("order_id")
    bill.order_id = order_id
    quantity = request.args.get("quantity")
    bill.quantity = quantity
    total_money = request.args.get("total_money")
    bill.total_money = total_money

    db.session.commit()

    return render_template("/admin/UpdateBillSuccess.html")


@app.route("/admin/bill/print-bill-success")
def go_admin_print_bill():
    bill = Bill.query.all()
    return render_template("/admin/Print_bill_success.html", bills=bill)
