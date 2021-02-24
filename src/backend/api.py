import flask
import json
from flask import request
from flask_cors import CORS
from CourseInfo import Course

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<p> Taxi-Js-Learner home dir </p>"


@app.route('/api/v1/instructions', methods=['GET'])
def api_get_instructions():
    start = request.args.get('start')
    end = request.args.get('end')
    response = app.response_class(json.dumps(
        Course.get_instructions(start, end), sort_keys=False, indent=4), mimetype=app.config['JSONIFY_MIMETYPE'])
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

app.run()
