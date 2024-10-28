
'''
outra alternativa -> usando typing (organizacao) => EXECUÇÃO EM MENOR TEMPO (362 ms):

import pandas as pd
from typing import List # biblioteca que fornece anotações de tipos p/variaveis 
# (DEFINE DADOS (tipagem) ESPERADOS - PARAMETRO, RETORNO)

student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ['student_id', 'age'])
print(createDataframe(student_data))
'''
import pandas as pd # runtime (557 ms)

student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]
def createDataframe(student_data):
    return pd.DataFrame(student_data, columns = ['student_id', 'age'])
print(createDataframe(student_data))
