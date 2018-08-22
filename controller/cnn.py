from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import numpy as np
import keras

classes = ["monkey", "boar", "crow"]
classes_len = len(classes)
image_size = 50


def main():
    X_train, X_test, y_train, y_test = np.load(".././photos.npy")
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


def model_train(X, y):
    model = Sequential()
    # Conv2D(pictures, filter)
    # X_train.shape -> (450, 50, 50, 3) 50*50*3のサイズの画像が450個
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=X.shape[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # 25% を消去
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    # Flatten...データを一列に並べる
    model.add(Flatten())
    # 全結合
    model.add(Dense(512))
    # 負の値を消去
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    # 最後の出力層のnode... monkey, boar, crow
    model.add(Dense(3))
    model.add(Activation('softmax'))

    # 最適化(誤差関数を各重みで微分した値を元に、更新すべき方向とどの程度更新するか)
    # 微分によって求めた値を、 学習率、エポック数、過去の重みの更新量など を踏まえてどのように重みの更新に反映するかを定めるのが 最適化関数
    # lr=leaning_rate, decay=学習率を下げていく(10の-6乗)
    opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

    # loss...損失関数
    model.compile(
        loss='categorical_crossentropy',
        optimizer=opt,
        metrics=['accuracy']
    )

    # 32枚ずつ, 100回繰り返す
    model.fit(X, y, batch_size=32, nb_epoch=100)

    model.save('.././photos_css.h5')

    return model


def model_eval(model, X, y):
    scores = model.evaluate(X, y, verbose=1)
    print('Test Loss: ', scores[0])
    print('Test Accuracy: ', scores[1])


if __name__ == "__main__":
    main()