import sklearn.datasets

digits = sklearn.datasets.load_digits() #手書き数字のデータセットを読み込みます。このデータセットには、0から9までの数字の手書き画像とその対応するラベルが含まれています。

print('データの個数＝', len(digits.images)) #読み込んだデータセット内の画像の数を表示しています。digits.imagesは画像データを含むNumPy配列です。各画像は8x8ピクセルのグレースケール画像であり、
print('画像データ＝', digits.images[0]) #digits.images[0]は最初の画像を表します。
print('何の数字か＝', digits.target[0]) #digits.targetは、各画像の対応する数字のラベルを含むNumPy配列です。digits.target[0]は最初の画像の対応する数字を表します。
