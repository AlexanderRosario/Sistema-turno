from  helpers.control import InsertAndUpdate

def insertTurn(ident,description):
    sql = '''INSERT INTO Turns (IdentificationClient,description) VALUES ('{}','{}')'''.format(ident,description)
    return  InsertAndUpdate(sql)