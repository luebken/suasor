import numpy
import pandas as pd
import sklearn
import scipy
import json
import os



# query = """
# WITH stars AS (
#      SELECT actor.login AS user, repo.name AS repo
#      FROM githubarchive.month.201706
#      WHERE type="WatchEvent"
# ),
# repositories_stars AS (
#      SELECT repo, COUNT(*) as c FROM stars GROUP BY repo
#      ORDER BY c DESC
#      LIMIT 1000
# ),
# users_stars AS (
#     SELECT user, COUNT(*) as c FROM  stars
#     WHERE repo IN (SELECT repo FROM repositories_stars)
#     GROUP BY user HAVING c > 10 AND C < 100
#     LIMIT 10000
# )
# SELECT user, repo FROM stars
# WHERE repo IN (SELECT repo FROM repositories_stars)
# AND user IN (SELECT user FROM users_stars)
# """

query = """
SELECT
    weight_pounds, state, year, gestation_weeks
FROM
    `bigquery-public-data.samples.natality`
ORDER BY weight_pounds DESC LIMIT 10;
"""

gc_svc_account = {
  "type": "service_account",
  "project_id": "suasor-184008",
  "private_key_id": "<TBD>",
  "private_key": "<TBD>",
  "client_email": "webquery@suasor-184008.iam.gserviceaccount.com",
  "client_id": "103981968423963988522",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/webquery%40suasor-184008.iam.gserviceaccount.com"
}

def main(params):
    gc_svc_account['private_key_id'] = params['GC_SVC_PRIVATE_KEY_ID']
    gc_svc_account['private_key'] = params['GC_SVC_PRIVATE_KEY']

    data = pd.io.gbq.read_gbq(query, dialect="standard", project_id=gc_svc_account['project_id'], private_key=json.dumps(gc_svc_account))
    data_json = data.to_json()
    
    return json.loads(data_json)


# for local testing
if __name__ == "__main__":
    params = {}
    params['GC_SVC_PRIVATE_KEY'] = os.environ['GC_SVC_PRIVATE_KEY'].decode('string-escape')
    params['GC_SVC_PRIVATE_KEY_ID'] = os.environ['GC_SVC_PRIVATE_KEY_ID'].decode('string-escape')
    print(main(params))
