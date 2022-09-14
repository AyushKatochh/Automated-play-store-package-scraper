import pymongo
from datetime import datetime

def access(col="playstore"):
    client = pymongo.MongoClient(<your database link>)
    mydb = client['scraper']
    mycol = mydb[col]
    return mycol

def add_playstore(name,version,date,package_name):
    mycol=access()
    dic={"package_name":package_name,"App":name,"version":version,"last_update":date,"scrape_time":datetime.now()}
    mycol.insert_one(dic)
def add_all(package_name,version,date):
    mycol=access('All')
    dic={"_id":package_name,"version":version,"last_update":date}
    mycol.insert_one(dic)
def find_all(package_name,version):
    # keys=["package_name","version","last_update"]
    mycol = access('All',)
    query={"_id":package_name}
    x=mycol.find(query)
    x=[i for i in x]
    # dic={ k:v for (k,v) in zip(keys, x)}
    if len(x)==0:
        return 0
    else:
        if version==x[0]['version']:
            return 1
        else:
            return x
def update_all(package_name,version,date):
    mycol = access('All')
    myquery = {"_id": package_name}
    newvalues = {"$set": {"version": version,"date":date}}

    mycol.update_one(myquery, newvalues)
