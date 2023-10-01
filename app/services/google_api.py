import copy
from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings
from .constants import (
    DRIVE_TYPE, FORMAT, SHEETS_TYPE, SERVICE_VER_3, SERVICE_VER_4,
    SPREADSHEET_BODY, TABLE_VALUES
)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover(
        SHEETS_TYPE, SERVICE_VER_4
    )

    spreadsheet_body = copy.deepcopy(SPREADSHEET_BODY)
    spreadsheet_body['properties']['title'] = f'Отчет на {now_date_time}'

    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover(DRIVE_TYPE, SERVICE_VER_3)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheetid: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover(SHEETS_TYPE, SERVICE_VER_4)

    table_values = copy.deepcopy(TABLE_VALUES)
    table_values[0] = ['Отчет от', now_date_time]

    for project in projects:
        new_row = [
            str(project['name']),
            str(project['close_date'] - project['create_date']),
            str(project['description'])
        ]
        table_values.append(new_row)
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    response = await wrapper_services.as_service_account(  # noqa
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            # количество столбцов для диапазона понятно, но
            # не совсем поняла, как взять реальное значение строк,
            # которое зависит от количества проектов
            range='R1C1:R30C3',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
