from  helpers.control import InsertAndUpdate

def insertTurn(ident,servicesID):
    # list_service = servicesID.split(",")[0]
    # print(list_service)
    sql = '''INSERT INTO Turns (IdentificationClient,ServiceID) VALUES ('{}',{})'''.format(ident,servicesID.split(",")[0])

    return  InsertAndUpdate(sql)