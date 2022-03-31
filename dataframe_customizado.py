import pandas as pd
import datetime

def get_lista_email(dataframe):
    """
    Transformando o dataframe em uma lista com os emails, sem duplicados
    """
    _res = list(dict.fromkeys(dataframe['email']))
    return _res


def get_date_filter(df,date_start,
                    date_end = None):
    """
    Returning a DataFrame filtered with the date (update), can use the start and end date.
    Date format = "yyyy-mm-dd" as string
    """
    print(date_start)
    
    if date_start.count("-") != 2:
        return print("Please, pass the date as a string with this format 'yyyy-mm-dd'")

    
    _date_start_tuple = tuple([int(_) for _ in date_start.split("-")])
    _date_start = datetime.datetime(*_date_start_tuple)
    
    _year_min = _date_start.year
    _month_min = _date_start.month
    _day_min = _date_start.day

    # only use the start date to filter
    _filter = 0

    if date_end != None:
        _date_end_tuple = tuple([int(_) for _ in date_end.split("-")])
        _date_end = datetime.datetime(*_date_end_tuple)

        _year_max = _date_end.year
        _month_max = _date_end.month
        _day_max = _date_end.day

        _filter = 1
    
    # adding a switch to do
    match _filter:
        case 0:
            df = df[(df['data_atualizacao'] > (pd.Timestamp(year=_year_min,
                                                            month=_month_min,
                                                            day=_day_min,
                                                            hour=0).to_datetime64()))]
            return df

        case 1:
            df = df[(df['data_atualizacao'] > (pd.Timestamp(year=_year_min,
                                                            month=_month_min,
                                                            day=_day_min,
                                                            hour=0).to_datetime64()))
                    &
                    (df['data_atualizacao'] < (pd.Timestamp(year=_year_max,
                                                            month=_month_max,
                                                            day=_day_max,
                                                            hour=0).to_datetime64()))]
            return df