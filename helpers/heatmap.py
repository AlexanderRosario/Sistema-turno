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
    try:
        df = pd.DataFrame(data)
        df.columns=['Usuarios','Cajas','Atendidos']
        sns.heatmap(df,center=0,annot=True,linewidths=0.7,linecolor='black',cmap="YlOrRd")
        
        plt.savefig('static/images/my_plot.png')
        

    except Exception as e:
        
        print(str(e))
        return {'is_success': None,
                'error':str(e)}
                
    return {'is_success': True,
                'error':None}
