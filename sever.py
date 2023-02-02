import json
import use_model
from flask import *

app = Flask(__name__)

@app.route("/post", methods=["POST"])
def post_souse_code():
    problem_id=request.json['problemId']
    language=request.json["language"]
    source_code = request.json['sourceCode']

    # ここで機械学習用のコードを関数に入れて結果を受け取る
    use_model.probability_error_source_code(source_code)

    result = {
      "problemId": problem_id,
      "language" : language,
      "result": [{ #TODO 現在サンプルを入れているため結果を入れるようにする
          "lineNumber": 1,
          "estimatedCorrectSentence": "#include<stdio.h>",
          "probability": 0.98,
        }
      ]
    }
    return jsonify({"result": result})



if __name__ == "__main__":
    app.run()


