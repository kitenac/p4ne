from matplotlib import pyplot
from openpyxl import load_workbook

# wb - специальный удобный объект для хранения таблицы - можно к списку приввести
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data'] # Загрузить лист с именем "Data" в переменную sheet

sheet['A'][1:] # Получить содержимое колонки A в виде списка
wb['Data']['A'][5].value # значение получить уже

# 0-th element of column is it`s name - so take [1:]
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


pyplot.plot()
pyplot.plot(extract_col(Table['Y']), extract_col(Table['a-t']))
pyplot.plot(extract_col(Table['Y']), extract_col(Table['Activeness']))

# plot description:
pyplot.xlabel("Годы")
pyplot.ylabel("Отн. темп-ра и солн. акт-ть")
pyplot.title('Годы - по григорианскому,\nтемпература - по Цельсию,\nсолн. активность - Вт/м²')
pyplot.show()
