#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Emman
#
# Created:     21/09/2018
# Copyright:   (c) Emman 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pymongo import MongoClient
from random import randint
from pprint import pprint


client = MongoClient('localhost',27017)
db=client.business
#Step 2: Creating sample data
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 11):
    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
    }
    """#Step 3: Inserting business object directly into MongoDB via insert_one
    result=db.reviews.insert_one(business)
    #Step 4: Printing to the console the ObjectID of the new document
    print('Created {0} of 10 as {1}'.format(x,result.inserted_id))"""

#Count all the documents in the collection
print('**********************************************')
entry_count = db.reviews.count_documents({})
print("The number of documents in my collection: %d" %entry_count)

#Count all the documents that have their 'category' as 'Business'
print('**********************************************')
business_count = db.reviews.count_documents({'rating' : randint(1, 5)})
print("All entries in the Business Rating Category: %d" %business_count)

#Print all docments in Json format
print('**********************************************')
cursor = db.reviews.find({})
for document in cursor:
    pprint(document)

#db.business.drop()
