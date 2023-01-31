import json
from flask import *

app = Flask(__name__)

@app.route("/post", methods=["POST"])
def post_souse_code():
    code = request.json['sourceCode']

    # ここで機械学習用のコードを関数に入れて結果を受け取る

    result = {
      "sourceCode": code
    }
    return jsonify({"result": result})



if __name__ == "__main__":
    app.run()


