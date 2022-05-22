from  helpers.control import InsertAndUpdate

def insertTurn(ident,servicesID):
    sql = '''INSERT INTO Turns (IdentificationClient,ServiceID) VALUES ('{}',{})'''.format(ident,servicesID)

    return  InsertAndUpdate(sql)