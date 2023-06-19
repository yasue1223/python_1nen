from turtle import * #turtleモジュールから全ての関数やクラスをインポート
shape('turtle') #亀の形状を設定します。ここでは、亀の形状を実際の亀の形に設定
col = ['orange','limegreen','gold','plum','tomato'] #色のリストを定義
for i in range(5): #ループを使用して五芒星を描画します。range(5)は0から4までの値を順番に取ります。
    color(col[i]) #亀のペンの色を設定します。col[i]は色のリストから順番に色を取得します。
    forward(200) #亀を画面上で200ピクセル前進
    left(144) #亀を画面上で左に144度回転
done()