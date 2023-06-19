import tkinter as tk
import random

def dispLabel():
    kuji = ['大吉','中吉','小吉','凶']
    lbl.configure(text=random.choice(kuji)) #

root = tk.Tk() #Tk()はTkinterのウィンドウオブジェクトを生成するためのコンストラクタです。rootはウィンドウオブジェクトへの参照です。
root.geometry('200x100') #geometry()メソッドを使用して、ウィンドウの幅と高さをピクセル単位で指定

lbl = tk.Label(text='LABEL') #Label()はテキストやイメージなどの表示用のウィジェットを生成するためのコンストラクタです。
btn = tk.Button(text='PUSH',command=dispLabel) #Button()はクリック可能なボタンを生成するためのコンストラクタです。

lbl.pack() #pack()メソッドを使用して、ウィジェットを親ウィンドウに配置します。ここでは、ラベルをウィンドウに追加しています。
btn.pack() #ボタンウィジェットをウィンドウに配置します。
tk.mainloop() #mainloop()関数は、ウィンドウが表示され、イベントの処理が開始される無限ループを作成します。