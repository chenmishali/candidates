from flask import Flask, jsonify
from flask_cors import CORS
import requests
import json


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# [{name: , job: , start: ,end: }]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    req = requests.get('https://hs-resume-data.herokuapp.com/v3/candidates/all_data_b1f6-acde48001122')
    data = json.loads(req.text)
    print(json.dumps(data, indent=4, sort_keys=True))
    index = 0
    candidates_dict = []
    while True:
        try:
            candidate_dict = {}
            candidate_dict["CANDIDATE_NAME"] = data[index]["contact_info"]["name"]["formatted_name"]
            jobs_count = 0
            candidate_dict["JOBS"] = []
            candidates_dict.append(candidate_dict)
            while True:
                experience = []
                try:
                    job = {}
                    job["JOB_TITLE"] = data[index]["experience"][jobs_count]["title"]
                    experience.append(job)
                except:
                    break

            index += 1
        except:
            break

    return json.dumps(req.text)


if __name__ == '__main__':
    app.run()