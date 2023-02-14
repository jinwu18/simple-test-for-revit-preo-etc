import pywinauto
from pprint import *
from pywinauto.keyboard import send_keys
import time


def pywinauto_creatfile():
    app = pywinauto.Application(backend='uia').connect(process=8836)
    pprint(app.windows())
    dlg = app.window(title='*新文件 1 - Notepad++')
    dlg.print_control_identifiers()
    menu = dlg.child_window(title="应用程序", auto_id="MenuBar", control_type="MenuBar")
    menu.print_control_identifiers()
    menu.child_window(title="文件(F)", control_type="MenuItem").click_input()
    menu.item_by_path('文件(F)->新建(N)').click_input()


def pywinauto_connectapp(pid, addr, handleid):
    """
    与app建立连接的三种方式：
    通过进程id连接
    通过句柄连接
    通过安装路径连接
    :return: none
    """
    if pid:
        app = pywinauto.Application(backend='uia').connect(process=pid)
    elif addr:
        app = pywinauto.Application(backend='uia').start(addr)
    elif handleid:
        app = pywinauto.Application(backend='uia').connect(handle=handleid)
    else:
        app = None
        print("[ERROR]: The key_words of connection is wrong!")
    return app


def pywinauto_wfile(addr):
    """
    操作文件：在notepad++中键入文字并保存
    bug：多次打开未关闭会引发异常
    :return:
    """
    app = pywinauto.Application(backend='uia').start(addr)
    pprint(app)
    dlg = app['新文件 1 - Notepad++']
    # dlg.print_control_identifiers()
    menu = dlg.child_window(title="应用程序", auto_id="MenuBar", control_type="MenuBar")
    # menu.print_control_identifiers()
    file = menu.child_window(title="文件(F)", control_type="MenuItem")
    # file.print_control_identifiers()
    file.click_input()
    menu.item_by_path('文件(F)->另存为(A)...').click_input()
    save_as = dlg['另存为']
    # save_as.print_control_identifiers()
    # 文件命名为pywinauto_test保存
    save_name = "pywinauto_test"
    save_as.child_window(title="文件名:", auto_id="1001", control_type="Edit").type_keys(save_name)
    save_as.child_window(title="保存(S)", auto_id="1", control_type="Button").click_input()
    check_save_as = dlg['确认另存为']
    check_save_as.child_window(title="是(Y)", auto_id="CommandButton_6", control_type="Button").click_input()
    time.sleep(5)
    new_win = app[r'C:\Users\ruanjin\PycharmProjects\pythonProject\pywinauto_test.txt - Notepad++']
    # new_win.child_window(title="pywinauto_test.txt", control_type="TabItem").type_keys("hello world!!")
    new_win.child_window(title="pywinauto_test.txt", control_type="TabItem")
    new_win.print_control_identifiers()
    send_keys("hello world!!")
    new_menu = new_win.child_window(title="应用程序", auto_id="MenuBar", control_type="MenuBar")
    new_menu.child_window(title="文件(F)", control_type="MenuItem").click_input()
    new_menu.item_by_path('文件(F)->保存(S)').click_input()
    time.sleep(4)
    new_win.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pid = 30064
    addr = r"C:\Program Files (x86)\Notepad++\notepad++.exe"
    handleid = None
    #pywinauto_creatfile()
    #app = pywinauto_connectapp(pid, addr, handleid)
    #pprint(app)
    pywinauto_wfile(addr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

