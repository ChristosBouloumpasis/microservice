import pymysql

def connectToDatabase():
    try:

        db = pymysql.connect(environ.get('DB_Host'), environ.get('DB_User'), environ.get('DB_Password'),environ.get('DB_Name'))

        return db
    except Exception as e:
        print(e)
        db.close()

def get_random(type):
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"""select Attribute_Name
                    from randomiser.drink_attributes
                    where Attribute_Type = %s
                    order by rand()
                    limit 1"""
        parameters = (type)
        cursor.execute(query, type)
        db.close()
        result = cursor.fetchone()
        return result["Attribute_Name"]
    except Exception as e:
        print(e)
        db.close()
        return False
