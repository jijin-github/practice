queryset = User.objects.all() # It won't hit the database
print (queryset)  # Now, ORM turns the query into raw sql  and fetches results from the database


queryset = Users.objects.all()
first_five = queryset[:5]    # Hits the database
first_ten = queryset[:10]    # Hits the database

queryset = Users.objects.all()
bool(queryset)  # queryset is evaluated  and results are cached
first_five = queryset[:5]    #  uses the cache
first_ten = queryset[:10]    # uses the cache

from django.db.models import Q
users_list = User.objects.filter(Q(email__startswith="an") | Q(email__startswith="sa"))
# equivalent SQL Qurery is
SELECT * FROM user_table WHERE email LIKE 'an%' OR email LIKE 'sa%'

~Q(email__startswith="an")  # email don't starts with "an" 
# SQL  equivalent
|  = OR
& = AND
~ = NOT

# Create Multiple Objects at once with Bulk Create

Model.objects.filter((Q(key1="value1") & ~Q(key2="value2")) | (~Q(key3="value"))

instance_list = [User(first_name=first_name, email=email) for first_name, email in users_details]
User.objects.bulk_create(instance_list)

# Bulk Update

from django.db.models import F

amount = 5000
developers = Employee.objects.filter(designation="Developer")
developers.update(salary=F("salary")+amount)

# usage of select_related

# without select related
person = Person.objects.get(id=1)
present_address = person.present_address  # Hits the database.
previous_address = person.previous_address  # Hits the database.
# total database hits = 3
# with select related
person = Person.objects.select_related().get(id=1)
present_address = person.present_address # Doesn't hit the database.
previous_address = person.previous_address # Doesn't hit the database.
# total database hits = 1
# you can also select the specific related objects
person = Person.objects.select_related("present_address").get(id=1)
present_address = person.present_address # Doesn't hit the database.
previous_address = person.previous_address # Hits the database.

# Limitaions of select_related

# without prefetch related
book = Book.objects.get(id=1)
author = book.author # Hits the database.
publishers = book # Hits the database.
# total database hits = 3
# with prefetch related
book = Book.objects.prefetch_related().get(id=1)
author = book.author  # Doesn't hit the database.
publishers = book.publishers.all() # Doesn't hit the database.
# total database hits = 1
# you can also select the specific related objects
book = Book.objects.prefetch_related("publishers").get(id=1)
author = book.author  # Doesn't hit the database.
publishers = book.publishers.all() # Hits the database.