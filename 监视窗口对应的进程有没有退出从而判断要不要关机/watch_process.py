import psutil


def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        print(psutil.Process(pid).name())
        if psutil.Process(pid).name() == processname:
            break
    else:
        print("not found")


if judgeprocess('notepad++.exe') == 0:
    print('success')
else:
    pass
