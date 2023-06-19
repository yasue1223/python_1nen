from turtle import * #turtleモジュールから全ての関数やクラスをインポート
shape('turtle') #亀の形状を設定します。ここでは、亀の形状を実際の亀の形に設定
for i in range(4): #ループを使用して四角形を描画します。range(4)は0から3までの値を順番に取ります。
    forward(100) #亀を画面上で100ピクセル前進
    left(90) #亀を画面上で左に90度回転
done()