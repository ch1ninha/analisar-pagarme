# importando as biblio
from datetime import datetime

# declarando as variaveis que podemos usar
data_atual = datetime.now()
ano_atual = data_atual.year
mes_atual = data_atual.month
dia_atual = data_atual.day


# as funcoes

# -> checar se é um dia valido
def check_dia(dia):
    dia = int(dia)   
    if dia >= 1 and dia <= 31:
        return True
    else:
        print("{}, é fora do intervalo do DIA, entre 01 e 31".format(dia))
        return False
    
# -> checar se é um mes valido
def check_mes(mes):
    mes = int(mes)
    if mes >= 1 and mes <= 12:
        return True
    else:
        print("{}, é fora do invervalo de MÊS, entre 01 e 12".format(mes))
        return False
    
# -> checar se é um ano valido
def check_ano(ano):
    ano = int(ano)
    # 1985 <= 2022 E 1985 >= 1990
    # SIM e NAO
    if ano <= ano_atual and ano >= 1990:
        return True
    else:
        print("{}, é fora do intervalo de ANO, entre {} e 1990".format(ano,ano_atual))
        return False
    
# usamos esse método para criar uma string de data
def get_string_data():
    """Retorna uma string de data no formato yyyy-mm-dd"""
    # agora checamos o Dia
    ok_dia = True
    while ok_dia:
        dia = input("Dia?")
        if check_dia(dia):
            ok_dia = False
    dia = int(dia)

    # agora checamos o Mes
    ok_mes = True
    while ok_mes:
        mes = input("Mes?")
        if check_mes(mes):
            ok_mes = False
    mes = int(mes)

    # agora checamos o Ano
    ok_ano = True
    while ok_ano:
        ano = input("Ano?")
        if check_ano(ano):
            ok_ano = False
    ano = int(ano)

    return "{}-{:02d}-{:02d}".format(ano,mes,dia)

# retorna o mesmo método acima, porem agora como tupla
def get_data_separada():
    """
    Retorna uma tupla com os dias passados.
    (ano,mes,dia)
    """
    # agora checamos o Dia
    ok_dia = True
    while ok_dia:
        dia = input("Dia?")
        if check_dia(dia):
            ok_dia = False
    dia = int(dia)

    # agora checamos o Mes
    ok_mes = True
    while ok_mes:
        mes = input("Mes?")
        if check_mes(mes):
            ok_mes = False
    mes = int(mes)

    # agora checamos o Ano
    ok_ano = True
    while ok_ano:
        ano = input("Ano?")
        if check_ano(ano):
            ok_ano = False
    ano = int(ano)

    return ano,mes,dia


# horarios em unixtime
def get_unixtime_data(data):
    """Transforma a string no formato data (yyyy-mm-dd) no formato de string em unix (ms)"""
    _data_datetime = datetime.strptime(data, "%Y-%m-%d")
    _data_unix = datetime.timestamp(_data_datetime)
    return _data_unix * 1000

def get_unixtime_datetime(data):
    """Transforma a string no formato datatime (yyyy-mm-ddThh:mm:ss.Z) no formato de string em unix (ms)"""
    _datetime_datetime = datetime.strptime(data,"%Y-%m-%dT%H:%M:%S.%fZ")
    _datetime_unix = datetime.timestamp(_datetime_datetime)
    return _datetime_unix * 1000


# transformando o tempo de segundos para formato padrao. 
# hh:mm:ss
def get_standard_format(seg):
    """
    Receives a period of time in seconds, and return a string with time standard format.
    HH:MM:SS
    """
    # hours
    h = int(seg // 3600)
    if h > 24:
        dias = seg // 86400
        seg = seg % 86400
        h = int(seg // 3600)
        seg = seg % 3600
        # minutes
        m = int(seg // 60)
        seg = seg % 60
        # seconds
        s = seg
        return "{:02d} Dias {:02d}:{:02d}:{:02d}".format(dias,h,m,s)
    else:
        seg = seg % 3600
        # minutes
        m = int(seg // 60)
        seg = seg % 60
        # seconds
        s = int(seg // 1)

        return "{:02d}:{:02d}:{:02d}".format(h,m,s)