# Write a solution to calculate and display the number of rows and columns of players.
import pandas as pd
from typing import List
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

'''
função pronta do Pandas, saber o nº de linhas (rows) e colunas (columns) so dataframe -> shape
df_size[0]: num linhas no df
df_size[1]: num colunas no df
'''
