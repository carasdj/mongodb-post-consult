import database as db

# Evaluate if the old password matches session username
# Check if newpassword1 and newpassword 2 matches
# AND function or, if you already pass the first test,
# just check the second test agad
# For the latter, redirect to the same screen
# Can be 2 different IF functions instead

# use the pymongo reference, there's an equivalent for:
# db.customers.updateOne({"username":"chums@example.com"}, {"$set":{"password":"n3wp@ssw0rd"}})
