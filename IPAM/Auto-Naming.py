from openpyxl import load_workbook

# wb - специальный удобный объект для хранения таблицы - можно к списку приввести
wb = load_workbook('Network parameters_DMC-SC_v1.5.xlsx')
sheet = wb['Data'] # Загрузить лист с именем "Data" в переменную sheet

sheet['A'][1:] # Получить содержимое колонки A в виде списка
wb['Data']['A'][5].value # значение получить уже

# !!! 0-th element of column is it`s name - so take [1:]
Table = {
 'Y': wb['Data']['A'][1:],
 'a-t': wb['Data']['C'][1:],
 'Activeness': wb['Data']['D'][1:]
}

# get value of wb_cell
def extract_value(cell):
    return cell.value

# wb_col ---> list of values
def extract_col(wb_col):
    return list(map(extract_value, wb_col))


a = extract_col(Table['Y'])