import tkinter as tk
import tkinter.filedialog as fd #ファイルダイアログを使用するためのfiledialogモジュールをインポート
import PIL.Image #画像の処理に使用するPIL（Pillow）ライブラリからImageモジュールをインポート
import PIL.ImageTk #TkinterでPIL画像を表示するためのモジュール

def dispPhoto(path): #指定されたパスの画像を読み込んでリサイズし、画像ラベルに表示する処理を行います。
    newImage = PIL.Image.open(path).resize((300,300)) #指定されたパスの画像をPIL.Image.open()メソッドで読み込み、resize()メソッドでリサイズ
    imageData = PIL.ImageTk.PhotoImage(newImage) #Tkinterの画像データに変換
    imageLabel.configure(image = imageData) #画像ラベルに画像を表示
    imageLabel.image = imageData #imageLabelのimageプロパティがimageDataで更新され、新しい画像がラベルに表示されるようになります。

def openFile(): #ファイルダイアログを開き、選択された画像ファイルのパスを取得します。取得したパスを引数としてdispPhoto関数を呼び出し、画像を表示します。
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)
    
root = tk.Tk() #Tkinterのウィンドウを作成
root.geometry('400x350') #ウィンドウのサイズを設定

btn = tk.Button(text='ファイルを開く',command=openFile) #ファイルを開くためのボタンウィジェットを作成
imageLabel = tk.Label() #画像を表示するためのラベルウィジェットを作成
btn.pack() #ボタンウィジェットをウィンドウに配置
imageLabel.pack() #画像ラベルウィジェットをウィンドウに配置
tk.mainloop()