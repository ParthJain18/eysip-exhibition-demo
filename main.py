from flask import Flask
from routes import routes
# from apis import apis

app = Flask(__name__)
app.register_blueprint(routes)
# app.register_blueprint(apis)

if __name__ == '__main__':
    app.run(port=5000, debug=True)