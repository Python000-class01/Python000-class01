import pandas as pd
import os
import locale
from configure import getConfig


class Utils:

    @staticmethod
    def get_data(source):
        return pd.read_csv(os.path.join("data", source)).to_dict('records')

    @staticmethod
    def printed_currency(val):
        locale.setlocale(locale.LC_ALL, getConfig().get('locale', 'en_US'))
        return locale.currency(val, grouping=True)

