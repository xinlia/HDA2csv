# pip install -i https://pypi.doubanio.com/simple/  pywinauto

from pywinauto import Application, keyboard, mouse
import time
import os


def click(x,y):
    mouse.click("LEFT", (x, y))
    time.sleep(0.1)

list=os.listdir('.\\HISTORY')

app_path = "D:\\DataManagerToolV3.09.5\\DataManager.exe"
app = Application().start(app_path)
time.sleep(0.5)


for file_name in list:
    if not file_name.endswith('.HDA'):
        continue
    dlg_spec = app.window(title='DataManager Tool 2019【V3.09.5】')
    dlg_spec.menu_select(r"文件->打开文件")
    time.sleep(0.05)
    dlg_spec1 = app.window(title='打开')
    time.sleep(0.01)
    #click(225, 518)
    #keyboard.send_keys(file_name)
    dlg_spec1.Edit.type_keys(file_name)
    time.sleep(0.01)
    dlg_spec1.type_keys('%O')
    time.sleep(0.1)
    click(76,135)
    click(90, 200)
    dlg_spec2 = app.window(title='另存为')
    dlg_spec2.Edit.type_keys(file_name.replace('.HDA', '.csv'))
    dlg_spec2.type_keys('%S')
    time.sleep(0.1)
    keyboard.send_keys('{ENTER}')
    time.sleep(0.1)
    click(135, 1001)
    keyboard.send_keys('{TAB}')
    time.sleep(0.01)
    keyboard.send_keys('{ENTER}')
    time.sleep(0.1)

