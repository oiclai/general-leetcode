import pandas as pd
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]

'''
metodo .loc do Pandas -> permite acesso a linhas e colunas
'''    