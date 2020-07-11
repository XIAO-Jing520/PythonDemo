import pythoncom
import PyHook3 as pyHook


class KeyBoardManager(object):
    keyIsPressed = False

    def onKeyDown(self, event):
        print('envent is ', event)
        if self.keyIsPressed:
            return True
        print(str(event.Key) + ' is pressed')
        print('Ascii:', event.Ascii)
        print('MessageName:', event.MessageName)  # 同上，共同属性不再赘述
        print('Message:', event.Message)
        print('Time:', event.Time)
        print('Window:', event.Window)
        print('WindowName:', event.WindowName)
        print('Ascii:', event.Ascii, chr(event.Ascii))  # 按键的ASCII码
        print('Key:', event.Key)  # 按键的名称
        print('KeyID:', event.KeyID)  # 按键的虚拟键值
        print('ScanCode:', event.ScanCode)  # 按键扫描码
        print('Extended:', event.Extended)  # 判断是否为增强键盘的扩展键
        print('Injected:', event.Injected)
        print('Alt', event.Alt)  # 是某同时按下Alt
        print('Transition', event.Transition)  # 判断转换状态
        print('---')

        self.keyIsPressed = True
        return True

    def onKeyUp(self, event):
        self.keyIsPressed = False
        print(str(event.Key) + ' is released')
        print('Ascii:', event.Ascii)
        print('MessageName:', event.MessageName)  # 同上，共同属性不再赘述
        print('Message:', event.Message)
        print('Time:', event.Time)
        print('Window:', event.Window)
        print('WindowName:', event.WindowName)
        print('Ascii:', event.Ascii, chr(event.Ascii))  # 按键的ASCII码
        print('Key:', event.Key)  # 按键的名称
        print('KeyID:', event.KeyID)  # 按键的虚拟键值
        print('ScanCode:', event.ScanCode)  # 按键扫描码
        print('Extended:', event.Extended)  # 判断是否为增强键盘的扩展键
        print('Injected:', event.Injected)
        print('Alt', event.Alt)  # 是某同时按下Alt
        print('Transition', event.Transition)  # 判断转换状态
        print('---')

        return True


def onMouseEvent(event):
    print("MessageName:", event.MessageName)
    print("Message:", event.Message)
    print("Time:", event.Time)
    # print ("Window:", event.Widow)
    print("WindowName:", event.WindowName)
    print("Position:", event.Position)
    print("Wheel:", event.Wheel)
    print("Injected:", event.Injected)
    print("---")

    return True


if __name__ == "__main__":
    mykbmanager = KeyBoardManager()
    # 创建一个“钩子”管理对象
    hookmanager = pyHook.HookManager()
    # 监控键盘操作
    hookmanager.KeyDown = mykbmanager.onKeyDown
    hookmanager.KeyUp = mykbmanager.onKeyUp
    # 设置键盘“钩子”
    hookmanager.HookKeyboard()

    # 监控鼠标操作
    hookmanager.MouseAll = onMouseEvent
    # 设置鼠标“钩子”
    hookmanager.HookMouse()

    # 循环获取信息
    pythoncom.PumpMessages()
