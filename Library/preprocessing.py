import logging
import numpy as np
import pandas as pd
from copy import deepcopy
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder


class DataFramePreprocessor(object):
    """This class helps perform preprocessing on data frames.
     Through this class, you can perform scaling or encoding operations on data frames.

     The currently verified transformers are as follows. 
     MinMaxScaler, StandardScaler, LabelEncoder, OneHotEncoder
    """
    def __init__(self) -> None:
        self._logger = logging.getLogger(self.__class__.__name__)

    def fit_transform_multiple_transformer(
        self, dataframe, transformers, columns_matrix, fit=True
    ):
        """Transforms each column of the DataFrame using copied transformers
        and returns the transformed DataFrame along with the fitted transformers.

        Args:
           df: The DataFrame to perform the transformation on.
           transformers: The source transformers on which to perform the transformation operation.
           The transformer in question must have a 'fit_transform' function.
           columns: This is a matrix of columns to be applied to each transformer.
           fit: Whether to perform fit before transform.

        Return:
            result_df: It is a DataFrame containing only the transformed data.
            transformers_dict: This is a dict with each column name as the key and the transformer as the value.
        """
        result_dfs = []
        result_tfs = []
        try:
            for transformer, columns in zip(transformers, columns_matrix):
                df, tfs = self.fit_transform_single_transformer(
                    dataframe, transformer, columns, fit
                )
                result_dfs.append(df)
                result_tfs.append(tfs)

            result_df = pd.concat(result_dfs, axis=1)
            transformers_dict = {k: v for dic in result_tfs for k, v in dic.items()}
            return (result_df, transformers_dict)
        except Exception as e:
            self._logger.exception(e)
            return None

    def fit_transform_single_transformer(
        self, dataframe, transformer, columns, fit=True
    ):
        """Transforms each column of the DataFrame using copied transformers
        and returns the transformed DataFrame along with the fitted transformers.

        Args:
           dataframe: The DataFrame to perform the transformation on.
           transformer: The source transformer on which to perform the transformation operation.
           The transformer in question must have a 'fit_transform' function.
           columns: List of columns on which transformations will be applied in the DataFrame.
           fit: Whether to perform fit before transform.

        Return:
            result_df: It is a DataFrame containing only the transformed data.
            transformers_dict: This is a dict with each column name as the key and the transformer as the value.
        """
        if len(columns) < 1:
            return None
        # The transformer corresponding to each column is stored.
        transformers = {}
        # Variable to store the transformed data
        data = []

        try:
            # Perform transformations on each column.
            for col in columns:
                tf = deepcopy(transformer)
                df_col = dataframe[col].to_numpy()

                if isinstance(tf, LabelEncoder) == False:
                    df_col = df_col.reshape(-1, 1)

                if fit == True:
                    result = tf.fit_transform(df_col)
                else:
                    result = tf.transform(df_col)

                if len(result.shape) == 1:
                    result = result.reshape(-1, 1)
                data.append(result)
                transformers[col] = tf

            if isinstance(tf, OneHotEncoder):
                dfs = []
                cols = [
                    [f"{col}_{cat}" for cat in tf.categories_[0]]
                    for col, tf in transformers.items()
                ]
                for i, d in enumerate(data):
                    df = pd.DataFrame(d.toarray(), columns=cols[i])
                    dfs.append(df)
                result_df = pd.concat(dfs, axis=1)
            else:
                result_df = pd.DataFrame(np.hstack(data), columns=columns)

            return (result_df, transformers)
        except Exception as e:
            self._logger.exception(e)
            return None

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return super.__repr__()


if __name__ == "__main__":
    titanic = pd.read_csv(r"D:\Python\AI_Example\data\titanic.csv")
    lbl = LabelEncoder()
    mms = MinMaxScaler()
    ohe = OneHotEncoder()
    numeric_cols = ["Parch", "Age", "Fare"]
    onehot_col = ["SibSp", "Sex"]
    label_col = ["Pclass"]
    dfp = DataFramePreprocessor()
    df, tfs = dfp.fit_transform_single_transformer(titanic, lbl, onehot_col)
    df, tfs = dfp.fit_transform_multiple_transformer(
        titanic, [mms, ohe, lbl], [numeric_cols, onehot_col, label_col]
    )

    df, tfs = dfp.fit_transform_multiple_transformer(
        titanic[:5], [mms, ohe, lbl], [numeric_cols, onehot_col, label_col]
    )
    col = [[k] for k in tfs]
    transforms = [tf for tf in tfs.values()]
    df, tfs = dfp.fit_transform_multiple_transformer(
        titanic[5:10], transforms, col, fit=False
    )
