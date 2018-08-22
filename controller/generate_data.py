from PIL import Image
import glob
import numpy as np
from sklearn import model_selection


classes = ["monkey", "boar", "crow"]
classes_len = len(classes)
image_size = 50

# 画像の読み込み
X = []
# ラベルデータ
Y = []

for index, cls in enumerate(classes):
    photos_dir = '.././' + cls
    # pettern一致でファイル一覧を取得
    files = glob.glob(photos_dir + '/*.jpg')
    for i, file in enumerate(files):
        if i > 200:
            break
        image = Image.open(file)
        image = Image.convert("RGB")
        image = image.resize(image_size, image_size)
        data = np.asarray(image)
        X.append(data)
        # 0=monkey, 1=boar, 2=row
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)

# 4つの変数のデータをファイルに(npの配列をtxtファイルとして)保存
xy = (X_train, X_test, y_train, y_test)
np.save(".././photos.npy", xy)