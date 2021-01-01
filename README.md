# Utility Functions for Python

- **sequence_indexer:** For instance, if ID is exist and not sequence in dataframe, this function generates the sequence ID without breaking the observation numbers, again. Then, original and new ID are mapping.

        | ID  | original_ID |
        |-----| ------------|
        |  1  |      1      |
        |  2  |      3      |
        |  2  |      3      |
        |  3  |      9      |
        |  3  |      9      |
        |  3  |      9      |

- **data_generate:** For instance, let's think we have two userID, three itemID in total. We want to generate the items based on userID. Optionally you may want to drop the indexes in the train or validation data from the generated data.

        | userID | itemID |      | userID | itemID |
        |------- |--------|      |--------|--------|
        |    1   |    1   |      |    1   |    1   |
        |    1   |    3   |  ->  |    1   |    3   |
        |    2   |    2   |      |    1   |    2   |
                                 |    2   |    1   |
                                 |    2   |    3   |
                                 |    2   |    2   |

- **pickle_serialize_deserialize:** Save and read the object or anything else as pickle.