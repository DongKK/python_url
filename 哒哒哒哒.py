from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
def closewindow():
    messagebox.showinfo(title='嘿嘿嘿',message='别害羞，叫一个听听')
    # windows.destroy()   #关闭窗口
    return
def say():
    # say=Toplevel()              #创建一个顶级窗口，依赖于原始窗口存在
    messagebox.showinfo(title='呦西', message='儿子真乖！')
    windows.destroy()
def nosay():
    # nosay=Toplevel()
    messagebox.showinfo(title='不叫？', message='不叫？')
    # nosay.mainloop()
    return
windows=Tk()    #创建一个窗口
windows.title('薄墨夙风')  #更改窗口的标题
windows.geometry('260x350+600+150')#设置窗口的大小
windows.geometry('+600+150')        #设置窗口的位置
windows.protocol('WM_DELETE_WINDOW',closewindow)  #当用户关闭窗口时触发
label=Label(windows,text='快,叫爸爸！',font=("微软雅黑",20))                  #添加一个文本标签
# label.grid()                #显示标签
# imag=PhotoImage(file='lala.jpg')                     #添加图片的控件
# image=Label(windows,image=imag)
# image.grid(row=2,columnspan=2)
label.grid(row=0,column=0,sticky=W)            #调整方位
photo=Image.open('lll.jpg')
phot=ImageTk.PhotoImage(photo)
pho=Label(windows,image=phot)
pho.grid(row=2,columnspan=2)
botten=Button(windows,text='爸爸',width=8,height=2,command=say)                                #添加一个按钮控键
botten.grid(row=9,column=0,sticky=W)
botten2=Button(windows,text='不叫',width=8,height=2,command=nosay)
botten2.grid(row=9,column=1,sticky=S)



windows.mainloop()    #显示窗口












