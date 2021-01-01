'''	    	       
@author : uguray

'''
import numpy as np

def sequence_indexer(df, column: str, org_column: str):
    '''
    Sequence indexing of non-sequence ID.

    Parameters
    ----------
    column : Name to be given to sequence ID.
    org_column : Name to be given to original ID.

    Returns
    -------
    df (pd.DataFrame) = Data.
    mapping (dict) = User or item map (column: org_column)

    '''
    df[org_column] = df[column]
    
    df = df.sort_values(column).reset_index(drop=True)

    df_list = df[column].to_list()
    df_list_uq = np.unique(df_list).tolist()
    
    # dict + fill blank
    uq_dict = dict((el, 0) for el in df_list_uq)
    
    # get uq key dict
    for i in range(1, len(df_list_uq)+1):
        uq_dict[df_list_uq[i-1]] = i
    
    # add new column
    for i in range(0, len(df[column])):
        uq_val = uq_dict[df[column][i]]
        df[column][i] = uq_val

    # Data mapping for org_columns in predict
    mapping = dict(df[[column, org_column]].values)

    # Drop org_column
    df = df.loc[:, ~df.columns.isin([org_column])]
    
    return df, mapping

df, mapping = sequence_indexer(df, 'ID', 'original_ID')

    
