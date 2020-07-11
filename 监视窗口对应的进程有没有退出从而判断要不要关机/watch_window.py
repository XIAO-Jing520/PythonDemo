from ctypes import *
import PyHook3 as pyHook
import pythoncom
import win32api
import time
import psutil
import os

hm = pyHook.HookManager()


def onKeyboardEvent(event):
    print("onKeyboardEvent")
    hm.UnhookKeyboard()  # 停止监听
    pid = c_ulong(0)
    hwnd = event.Window
    windowTitle = create_string_buffer(512)
    windll.user32.GetWindowTextA(hwnd, byref(windowTitle), 512)
    windll.user32.GetWindowThreadProcessId(hwnd, byref(pid))
    windowName = windowTitle.value.decode('gbk')
    print("当前您处于%s窗口" % windowName)
    print("进程名", psutil.Process(pid.value).name())
    print("当前窗口所属进程id %d" % pid.value)
    print("当前刚刚按下了%s键" % chr(event.Ascii))

    while True:
        pl = psutil.pids()
        for each_pid in pl:
            # print(each_pid, psutil.Process(each_pid).name())
            if pid.value == each_pid:
                print(windowName, "正在运行")
                time.sleep(5)
                break
        else:
            print("程序结束，关机")
            win32api.PostQuitMessage(1)  # 结束程序
            os.system("shutdown -s -t  60 ")
            return False  # True 会把输入复制一份给原窗口，False不会复制一份给原窗口
    return True


hm.KeyDown = onKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
