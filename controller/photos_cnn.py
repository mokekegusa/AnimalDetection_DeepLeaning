from keras.utils import np_utils
import numpy as np

from models.cnn import model_train, model_eval

classes = ["monkey", "boar", "crow"]
classes_len = len(classes)
image_size = 50


def main():
    X_train, X_test, y_train, y_test = np.load("./photos.npy")
    # 正規化... 現在は256階調(整数)だが、0~1の方が良い
    X_train = X_train.astype("float") / 256
    X_test = X_test.astype("float") / 256
    # one-hot-vector... 正解値は1。他は0 # [0,1,2]=>[1,0,0],[0,1,0],[0,0,1]に変換
    y_train = np_utils.to_categorical(y_train, classes_len)
    y_test = np_utils.to_categorical(y_test, classes_len)

    # モデルの作成
    model = model_train(X_train, y_train)
    # テスト用データをモデルに渡し、評価。
    model_eval(model, X_test, y_test)


if __name__ == "__main__":
    main()