import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]
# How to access two collections under the same database
order_management_db = myclient["order_management"]

def get_branch(code):
    branches_coll = products_db["branches"]
    branch = branches_coll.find_one({"code":code})

    return branch

def get_branches():
    branch_list = []
    branches_coll = products_db["branches"]

    for p in branches_coll.find({}):
        branch_list.append(p)

    return branch_list

def get_orders():
    order_list = []
    orders_coll = order_management_db["orders"]

    for p in orders_coll.find({"username":insert the username of whoever is logged in}):
        order_list.append(p)

    return order_list

    # db.orders.find({"username":"chums@example.com"})

def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)

def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user

def get_product(code):
    products_coll = products_db["products"]
    product = products_coll.find_one({"code":code})

    return product

def get_products():
    product_list = []
    products_coll = products_db["products"]

    for p in products_coll.find({}):
        product_list.append(p)

    return product_list

def get_order(code):
    orders_coll = order_management_db["orders"]
    order = orders_coll.find_one({"code":code})

    return order
