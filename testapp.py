from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'DELETE', 'GET'])
def my_app():
    print (request)
    print(request.environ)
    response = jsonify({'Hello': 'World!!!', 'app': {'name': 'MY 1st app'}})
    print (response)
    print (response.data)
    return response

if __name__ == '__main__':
        app.run()
        print(app.url_map)




