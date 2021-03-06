from keras.models import Sequential
from keras.layers import Lambda, Conv2D, Dropout, Dense, Flatten
from keras.optimizers import Adam


class DqnModel:
    @staticmethod
    def build_model(input_shape, output_shape, learning_rate=1.0e-4, keep_prob=0.5):
        model = Sequential()
        model.add(Lambda(lambda x: x/127.5-1.0, input_shape=input_shape))
        model.add(Conv2D(24, 5, 5, activation='elu', subsample=(2, 2)))
        model.add(Conv2D(36, 5, 5, activation='elu', subsample=(2, 2)))
        model.add(Conv2D(48, 5, 5, activation='elu', subsample=(2, 2)))
        model.add(Conv2D(64, 3, 3, activation='elu'))
        model.add(Conv2D(64, 3, 3, activation='elu'))
        model.add(Dropout(keep_prob))
        model.add(Flatten())
        model.add(Dense(200, activation='elu'))
        model.add(Dense(100, activation='elu'))
        model.add(Dense(30, activation='elu'))
        model.add(Dense(output_shape))
        model.summary()

        model.compile(loss='mean_squared_error', optimizer=Adam(lr=learning_rate))

        return model