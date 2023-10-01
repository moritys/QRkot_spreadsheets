from datetime import datetime


FORMAT = "%Y/%m/%d %H:%M:%S"
NOW_DATE_TIME = datetime.now().strftime(FORMAT)

SHEETS_TYPE = 'sheets'
DRIVE_TYPE = 'drive'
SERVICE_VER_4 = 'v4'
SERVICE_VER_3 = 'v3'

SPREADSHEET_BODY = {
    'properties': {'title': f'Отчет на {NOW_DATE_TIME}',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 100,
                                                  'columnCount': 11}}}]
}

TABLE_VALUES = [
    ['Отчет от', NOW_DATE_TIME],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]
