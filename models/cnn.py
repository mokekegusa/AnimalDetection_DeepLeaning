from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import keras


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
    model.save('./photos_css.h5')
    return model


def model_eval(model, X, y):
    scores = model.evaluate(X, y, verbose=1)
    print('Test Loss: ', scores[0])
    print('Test Accuracy: ', scores[1])
