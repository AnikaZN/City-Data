from flask import Flask, jsonify, request

df = pd.read_csv('./anika_cities.csv')

app = Flask(__name__)

# @app.route('/')
# def root():
#     return 'Hello world!'

@app.route('/')
def root():

    data = request.get_json(force = True)
    output = df[df['city'] == str(data)]

    return jsonify(output = output)

if __name__ == '__main__':
    app.run()
