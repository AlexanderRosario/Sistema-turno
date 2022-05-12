import pandas as pd
from  .control import SelectList
import seaborn as sns
import matplotlib.pyplot as plt

def df_frame():
    sql_select = ''' SELECT Users.UserName,Cashiers.Name,COUNT(*) FROM FinishedShift
                        INNER JOIN users on users.UserID = FinishedShift.UserID
                        INNER JOIN CashierUsers on CashierUsers.UserID = Users.UserID
                        INNER JOIN Cashiers on Cashiers.CashierID = CashierUsers.CashierID 
                            WHERE status= 'finished' 
	                            GROUP BY  FinishedShift.UserID
  '''
    data = SelectList(sql_select)
    if not data:
        return "ha ocurrido un error"

    df = pd.DataFrame(data)
    df.columns=['Usuarios','Cajas','Atendidos']
    df = df.pivot(index='Usuarios',columns='Cajas',values='Atendidos')
    
    sns.heatmap(df,center=0,annot=True)

    plt.savefig('static/images/my_plot.png')

    # print(df_seaborn)
    return True
