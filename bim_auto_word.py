from win32com.client import Dispatch
import random, os


def word_operate():
    app = Dispatch('Word.Application')
    # 新建word文档
    doc = app.Documents.Add()
    app.Visible = 1
    s = app.Selection
    for i in range(20):
        s.Text = 'Windows 10’s Task Manager has detailed GPU-monitoring tools hidden in it. You can view per-application and system-wide GPU usage, and Microsoft promises the Task Manager’s numbers will be more accurate than the ones in third-party utilities.' \
                 'How This Works' \
                 'These GPU features were added in Windows 10’s Fall Creators Update, also known as Windows 10 version 1709. If you’re using Windows 7, 8, or an older version of Windows 10, you won’t see these tools in your Task Manager. Here’s how to check which version of Windows 10 you have.' \
                 'Windows uses newer features in the Windows Display Driver Model to pull this information directly from the GPU scheduler (VidSCH) and video memory manager (VidMm) in the WDDM’s graphics kernel, which are responsible for actually allocating the resources. It shows very accurate data no matter which API applications use to access the GPU—Microsoft DirectX, OpenGL, Vulkan, OpenCL, NVIDIA CUDA, AMD Mantle, or anything else.' \
                 'y only systems with WDDM 2.0-compatible GPUs show this information in the Task Manager. If you don’t see it, your system’s GPU probably uses an older type of driver.' \
                 'You can check which version of WDDM your GPU driver is using by pressing Windows+R, typing “dxdiag” into the box, and then pressing Enter to open the DirectX Diagnostic tool. Click the “Display” tab and look to the right of “Driver Model” under Drivers. If you see a “WDDM 2.x” driver here, your system is compatible. If you see a “WDDM 1.x” driver here, your GPU isn’t compatible.' \
                 '' \
                 'How to View an Application’s GPU Usage' \
                 'This information is available in the Task Manager, although it’s hidden by default. To access it, open the Task Manager by right-clicking any empty space on your taskbar and selecting “Task Manager” or by pressing Ctrl+Shift+Esc on your keyboard.' \
                 'Click the “More details” option at the bottom of the Task Manager window if you see the standard, simple view.' \
                 'In the full view of Task Manager, on the “Processes” tab, right-click any column header, and then enable the “GPU” option. This adds a GPU column that lets you see the percentage of GPU resources each application is using.' \
                 'You can also enable the “GPU Engine” option to see which GPU engine an application is using.'
    doc.SaveAs('C:\\Users\\' + os.getlogin() + '\\Desktop\\工作文档\\python_word_demo' + str(random.randint(1000000, 9999999)) + '.docx')
    doc.Close()
    app.Quit()


def test_run():
    word_operate()


if __name__ == '__main__':
    for i in range(2):
        test_run()
