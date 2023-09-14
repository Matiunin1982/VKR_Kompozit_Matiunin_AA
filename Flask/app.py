from flask import Flask, request, render_template
import tensorflow as tf

app = Flask(__name__)


@app.route('/')
def choose_prediction_method():
    return render_template('main.html')


def matrica_prediction(params):
    model = tf.keras.models.load_model('Flask/saved_model/model_minmax.h5')
    pred = model.predict([params])
    return pred


@app.route('/matrica/', methods=['POST', 'GET'])
def matrica_predict():
    message = ''
    if request.method == 'POST':
        param_list = ('plot', 'mup', 'ko', 'seg', 'tv', 'pp', 'mup', 'pr', 'ps', 'yn', 'shn', 'pln')
        params = []
        for i in param_list:
            param = request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        message = f'Спрогнозированное Соотношение матрица-наполнитель для введенных параметров: {matrica_prediction(params)}'
    return render_template('matrica.html', message=message)


if __name__ == '__main__':
    app.run()
