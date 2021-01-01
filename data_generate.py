"""	    	       
@author : uguray

"""
import pandas as pd


def data_generate(data, user_col: str, item_col: str, *args):
    """
    Add all items to each user.

    Parameters
    ----------
    data (pd.DataFrame): Data to be generated.
    train (pd.DataFrame): Drop user and item id from generate_data. (optional)
    val (pd.DataFrame): Drop user and item id from generate_data. (optional)

    Returns
    -------
    all_data (pd.DataFrame): Generated data.

    """
    users = list(set(data[user_col]))
    items = list(set(data[item_col]))

    result = []
    for user in users:
        for item in items:
            result.append([user, item])

    # Generalized data
    generate_data = pd.DataFrame(result, columns=[user_col, item_col])

    [df.set_index([user_col, item_col], inplace=True) for df in [generate_data, *args]]

    [generate_data.drop(df.index, inplace=True) for df in [*args]]

    [df.reset_index(inplace=True) for df in [generate_data, *args]]

    return all_data

generate_data = data_generate(
     df, 'userID', 'itemID', train_data, val_data
)
