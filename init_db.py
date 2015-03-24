#!/usr/bin/env python3

# initialize Django
import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django
django.setup()
from django.contrib.auth.models import Group, Permission
from django.db import connection
import subprocess

# regular imports
import homepage.models as hmod


##### DROP DATABASE, RECREATE IT, THEN MIGRATE IT #################

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

####################################    DUMMY DATA    ################################################
##########################       PHOTOS
for data in [
   ["2000-12-25", "Sydney", "Cool yeah!", "/static/homepage/media/magicbeans.jpg"],
   ["2000-12-25", "Herriman", "Oaky", "/static/homepage/media/pipe.jpg"],
   ["2000-12-25", "Salt Lake", "dsfsdsd", "/static/homepage/media/tatteredflag.jpg"],
    ["2000-12-25", "hahaha", "feefef best this", "/static/homepage/media/George-Washington.jpg"],
    ["2000-12-25", "Provo", "BEEFY", "/static/homepage/media/George-Washington.jpg"],
]:
    p = hmod.Photograph()
    p.date_taken = data[0]
    p.place_taken = data[1]
    p.description = data[2]
    p.image = data[3]
    p.save()

##########################       ADDRESSES
for data in [
   ["1432 Wallaby Way", "Sydney", "SydneyState", "49830", "Australia"],
   ["1782 S. Ashland Ridge dr.", "Herriman", "UT", "47483", "USA"],
   ["4484 W. 344 S.", "Salt Lake", "UT", "84848", "USA"],
    ["4555 W. 566 S.", "hahaha", "NY", "44555", "USA"],
    ["34343 W. 884444 S.", "Provo", "UT", "84333", "USA"],
]:
    a = hmod.Address()
    a.street1 = data[0]
    a.city = data[1]
    a.state = data[2]
    a.zip_code = data[3]
    a.country = data[4]
    a.save()


###################################      CREATE PERMISSIONS/GROUPS
g1 = Group()
g1.name = "Admin"
g1.save()

g2 = Group()
g2.name = 'Manager'
g2.save()

g3 = Group()
g3.name = 'Agent'
g3.save()

g4 = Group()
g4.name = 'Customer'
g4.save()

############################       ADD Permissions to Groups

admin = Group.objects.get(name="Admin")
admin.permissions = Permission.objects.all()
admin.save()

manager = Group.objects.get(name="Manager")
manager.permissions = Permission.objects.all().exclude(id=24) #Just can't delete Users
manager.save()

agent = Group.objects.get(name="Agent")
agent.permissions = Permission.objects.all().exclude(id=3) ##I want this to exclude all id's of the multiple 3 so the Agent can't delete anything.
agent.save()

###################################    USERS

id_counter = 0

for data in [
   ["Jayson", "jensen", "jayson", "jayson", "jays_son@gmail.com", False, "Am I cool?", "yes", "801-324-4233", 1],
   ["Macie", "Vogt", "macie", "macie", "macie_waffle_love@gmail.com", False, "Whos my daddy?", "Gerald", "801-624-4433", 4],
   ["David", "Vogtes", "david", "david", "dave_the_man@gmail.com", False, "How old am I?", "43", "801-324-4433", 3],
    ["Steven", "Dewey", "steven", "steven", "dewey_CEO@gmail.com", False, "Whats my favorite color?", "pink", "801-384-4433", 2],
    ["Kevin", "LeStarge", "kevin", "lestarge", "kblestarge@gmail.com", True, "Am I cool?", "Heck yes", "801-324-4733", 4],
]:
    id_counter += 1

    u = hmod.User()
    u.first_name = data[0]
    u.last_name = data[1]
    u.set_password(data[2])
    u.username = data[3]
    u.email = data[4]
    u.is_superuser = data[5]
    u.security_question = data[6]
    u.security_answer = data[7]
    u.phone = data[8]
    u.address_id = id_counter
    u.photo_id = id_counter
    u.save()

    u.groups.add(data[9])
    u.save()

##########################       EVENTS
for data in [
   ["Bobsledding", "This is the coolest description ever!", "2000-12-25", "2012-12-25", "File name", "cool venue", 1],
   ["Axe Throwing Competition", "blahahahbl shshh kdkdkkdkdkdk", "2000-12-25", "2012-12-25", "File name", "cool venue", 1],
   ["Bobbing for Apples", "oooooOOOOooooo, This is a good one", "2000-12-25", "2012-12-25", "File name", "cool venue", 2],
    ["Beer Drinking Competition", "Drink a lot of beer, but be careful, it's so bad for you", "2000-12-25", "2012-12-25", "File name", "cool venue", 4],
    ["Mayflower Replica", "yeah, it's a good one", "2000-12-25", "2012-12-25", "File name", "cool venue", 1],
]:
    e = hmod.Event()
    e.name = data[0]
    e.description= data[1]
    e.start_date = data[2]
    e.end_date = data[3]
    e.map_file_name = data[4]
    e.venue_name = data[5]
    e.address_id = data[6]
    e.save()

##########################       CATEGORY
e1 = hmod.Category()
e1.description = "Cool Category"
e1.save()

e2 = hmod.Category()
e2.description = "Rad Category"
e2.save()

e3 = hmod.Category()
e3.description = "Too-cool-for-school Category"
e3.save()

##########################       PRODUCT SPECIFICATION
for data in [
   ["Magic Beans", "39.95", "These beans make you smarter and taller", "Jack", "0.01", "hhhhh", "sdf", "five", 1, 5, 1],
    ["George Washington's Pipe", "1300", "Seriously, he smoked this", "His Mom", "1000", "hhhhh", "sdf", "five", 2, 5, 2],
    ["Tattered 19th Century Flag", "369.95", "If you're into that", "China", "4.50", "hhhhh", "sdf", "five", 3, 5, 3],
]:

    e = hmod.ProductSpecification()
    e.name = data[0]
    e.price = data[1]
    e.description = data[2]
    e.manufacturer = data[3]
    e.average_cost = data[4]
    e.sku = data[5]
    e.order_form_name = data[6]
    e.production_time = data[7]
    e.category_id = data[8]
    e.vendor_id = data[9]
    e.photo_id = data[10]
    e.save()

#########################       STOCKED PRODUCT
for data in [
   ["5", "Behind the fridge", "I don't know", 1, 3],
   ["445", "Shed", "I don't know", 2, 1],
   ["100", "sdfs", "I don't know", 2, 3],
    ["42", "house", "I don't know", 1, 2],
    ["7", "Under the bed", "I don't know", 2, 3],
]:
    s = hmod.StockedProduct()
    s.quantity_on_hand = data[0]
    s.shelf_location= data[1]
    s.order_file= data[2]
    s.photo_id= data[3]
    s.product_specification_id= data[4]
    s.save()

##########################       SERIALIZED PRODUCT
for data in [
   ["1", "sdfs", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Green", "stripes", "1776", "1889", "1", "Barn", "I don't know", 2, 2],
   ["2", "sdf", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Green", "stripes", "1776", "1889", "45", "Barn", "I don't know", 3, 3],
   ["3", "fsf", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Green", "stripes", "1776", "1889", "43", "Barn", "I don't know", 1, 3],
    ["4", "wer", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Green", "stripes", "1776", "1889", "345", "Barn", "I don't know", 4, 3],
    ["5", "werff", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Green", "stripes", "1776", "1889", "5", "Barn", "I don't know", 1, 1],
]:

    sp = hmod.SerializedProduct()
    sp.serial_number = data[0]
    sp.type = data[1]
    sp.date_acquired = data[2]
    sp.cost = data[3]
    sp.for_sale = data[4]
    sp.condition_new = data[5]
    sp.notes = data[6]
    sp.owner_id = data[7]
    sp.size = data[8]
    sp.size_modifier = data[9]
    sp.gender = data[10]
    sp.color = data[11]
    sp.pattern = data[12]
    sp.start_year = data[13]
    sp.end_year = data[14]

    sp.quantity_on_hand = data[15]
    sp.shelf_location= data[16]
    sp.order_file= data[17]
    sp.photo_id= data[18]
    sp.product_specification_id= data[19]

    sp.save()

#########################       RENTAL PRODUCT
for data in [
   ["45", "55.43", "99.99", "34", "THIS IS THE BETTER WAY", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Yellow", "lad", "1999", "1733", "400", "behind fridge", "dsfd", 1, 2],
   ["234", "55.43", "99.99", "66", "blahaha", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Yellow", "lad", "1999", "1733", "400", "behind fridge", "dsfd", 2, 3],
   ["2", "55.43", "99.99", "90", "ooooOOOOoo", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Yellow", "lad", "1999", "1733", "400", "behind fridge", "dsfd", 3, 2],
    ["77", "55.43", "99.99", "94", "Ride on", "2012-12-12", "50.55", True, False, "this is a good product", 1, "Huge", "well, kinda huge", "Male", "Yellow", "lad", "1999", "1733", "400", "behind fridge", "dsfd", 4, 1],
]:

    r = hmod.RentalProduct()
    r.times_rented = data[0]
    r.price_per_day= data[1]
    r.replacement_price= data[2]

    r.serial_number = data[3]
    r.type = data[4]
    r.date_acquired = data[5]
    r.cost = data[6]
    r.for_sale = data[7]
    r.condition_new = data[8]
    r.notes = data[9]
    r.owner_id = data[10]
    r.size = data[11]
    r.size_modifier = data[12]
    r.gender = data[13]
    r.color = data[14]
    r.pattern = data[15]
    r.start_year = data[16]
    r.end_year = data[17]

    r.quantity_on_hand = data[18]
    r.shelf_location= data[19]
    r.order_file= data[20]
    r.photo_id= data[21]
    r.product_specification_id= data[22]

    r.save()
#################################      ORDER

for data in [
   ["1990-08-15", "801-898-6764", "2000-12-12", "2000-11-11", "2000-11-11", "453", 2, 1, 3, 2, 3, 4],
   ["1990-08-15", "801-898-6764", "2000-12-12", "2000-11-11", "2000-11-11", "453", 2, 5, 3, 2, 4, 2],
    ["1990-08-15", "801-898-6764", "2000-12-12", "2000-11-11", "2000-11-11", "453", 1, 1, 1, 2, 1, 4],
    ["1990-08-15", "801-898-6764", "2000-12-12", "2000-11-11", "2000-11-11", "453", 2, 3, 2, 2, 3, 4],
]:

    sp = hmod.Order()
    sp.order_date = data[0]
    sp.phone = data[1]
    sp.date_packed = data[2]
    sp.date_paid = data[3]
    sp.date_shipped = data[4]
    sp.tracking_number = data[5]
    sp.ships_to_id = data[6]
    sp.packed_by_id = data[7]
    sp.payment_processed_by_id = data[8]
    sp.shipped_by_id = data[9]
    sp.handled_by_id = data[10]
    sp.customer_id = data[11]
    sp.save()

#################################      CART LINE ITEM

for data in [
   ["51", 2, 3],
    ["83", 1, 1],
    ["74", 3, 2],
]:

    cli = hmod.CartLineItem()
    cli.quantity = data[0]
    cli.stocked_product_id = data[1]
    cli.user_id = data[2]
    cli.save()

#################################      SALE ITEM

for data in [
   ["989", 5, "499.99", 2],
   ["912", 3, "499.99", 1],
    ["89", 9, "499.99", 3],
    ["20", 1, "499.99", 4],
]:

    si = hmod.SaleItem()
    si.quantity = data[0]
    si.product_id = data[1]

    si.amount = data[2]
    si.order_id = data[3]

    si.save()

#################################      Rental Item

for data in [
   ["1998-12-12", "1990-08-15", "1989-01-01", ".50", 11, "99.99", 1],
    ["1988-12-12", "1990-08-15", "1989-01-01", ".50", 12, "99.99", 2],
    ["1978-12-12", "1990-08-15", "1989-01-01", ".50", 13, "99.99", 3],
    ["2015-12-12", "2015-08-15", "2016-01-01", ".50", 13, "99.99", 3],
]:

    ri = hmod.RentalItem()
    ri.date_out = data[0]
    ri.date_in = data[1]
    ri.date_due = data[2]
    ri.discount_percent = data[3]
    ri.rental_product_id = data[4]

    ri.amount = data[5]
    ri.order_id = data[6]
    ri.save()

#################################      Damage Fee

for data in [
   ["dents and scrapes", False, 3, "50.43", 1],
   ["paint spilled", True, 1, "43", 2],
    ["grass stains", False, 2, "10.00", 3],
]:

    df = hmod.DamageFee()
    df.description = data[0]

    df.waived = data[1]
    df.rental_item_id = data[2]

    df.amount = data[3]
    df.order_id = data[4]

    df.save()

#################################      Late Fee

for data in [
   ["5", False, 1, "10.43", 3],
   ["3", True, 2, "4.50", 2],
    ["25", False, 3, "50.00", 1],
]:

    lf = hmod.LateFee()
    lf.days_late = data[0]

    lf.waived = data[1]
    lf.rental_item_id = data[2]

    lf.amount = data[3]
    lf.order_id = data[4]

    lf.save()

################################      Configuration Parameters

for data in [
   [".23"],
   [".20"],
    [".13"],
]:

    cp = hmod.ConfigurationParameters()
    cp.sales_tax_rate = data[0]
    cp.save()

#################################      AREA

for data in [
   ["Pioneer Park", "Cool park with lots of trees", "22", 1, 2, 4, None, 4],
    ["Provo Jamboree", "Lots of scouts", "21", 1, 2, 4, None, 4],
    ["Orem Skate Park", "Nice skating", "1", 1, 2, 4, None, 4],
    ["Utah Valley Convention Center", "sdfsdfsdfsdfsdf", "100", 1, 2, 4, None, 4],
]:

    a = hmod.Area()
    a.name = data[0]
    a.description = data[1]
    a.place_number = data[2]
    a.coordinator_id = data[3]
    a.supervisor_id = data[4]
    a.event_id = data[5]
    #a.participants = data[6]
    a.photo_id = data[7]
    a.save()

#################################       Participant Role

for data in [
   [1, 1, "Colonial Tea Party Guy", "Cool"],
   [3, 2, "Bootlegger", "kinda lame"],
    [2, 3, "Cook in the kitchen", "funny"],
]:

    pr = hmod.ParticipantRole()
    pr.participant_id = data[0]
    pr.area_id = data[1]
    pr.name = data[2]
    pr.type = data[3]

    pr.save()




print("Script ran successfully!          Group Lucky #7 is in the house!")