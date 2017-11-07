import numpy
import pandas as pd
import sklearn
import scipy
import json



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

project_id = "suasor-184008"
private_key = {
  "type": "service_account",
  "project_id": "suasor-184008",
  "private_key_id": "1b4ad09ce7e997d30290edbe5f7026aa0375f17a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDI/zxJ/dAutFpA\nPiQ8AU6a9R1sQVOv+5oCIBcHoDLLRZo4Xuok3DM5UHmHWPmy8l30OFLldKW3swiq\nL3TBA9lnVeVUrSB9eWRq5Ozbu6Ir2MoTTCPlJO6nIJyN/TZetySu2fireBb1TS6U\nWKCCGVod802TpdMjAMjM3ATEbetBskNl43h7MdyC4J8ERFYwBpNipMPZr/Z/jDcD\nYsQbx1GtR7V+M7oODKJ7yI2mUrNiQERNhCRgEkcPiamgmsNDrBFZnk4utviDKuce\ntcyDvFCFgdeYpK034GfpzkfiGfpTPPzJUw05aUkmzvWApFNbIFJsX2eIdE4AuLXw\n7j3UZHLjAgMBAAECggEAA6z7PsUn/fqpXdxlED3b4KST5atqKuE4h0pr8WVCGIqM\nz/QYZxUp0KYCmvGLG3UoN7Oh/HU+JJZfFbGpenAmFSgyefJykijap8PI+xm61P9x\nbpnpXCLpRGApzMTxLhk+T/5HeGdJUDIZpHfcc5SgG8UbyZPyQQUeJvTtF2SFNV3T\nXaLkoAbjLpVUhoj/PhCO8F9loEWkuQWpHd9CMl1f94uWngaME8lYTis4dyS+6J8k\n0yKAAnfQd3LaCDPxuAdom4EiV+BFqIe0lS63o4CImI9d+f9x6puyXMGDXhnMfTcV\nbCgKRpvRuBlMVbciH5abofeVQhlN9kqkq484JDAdjQKBgQD43ZmhuF40iEe3CuDp\ndvanrAwhzleuIG/7FjaTyjlSWkhnOMOL4OByBdENw7b//AQBcUNJ/tuPFKprQspp\n3uVa7jv/tuOeHr1XydkM0iL8uajAkVHghyxAqqxPIv2dlkAZ4B6+igtvwQBFPci2\nKztozF8A2k6J5OKCdkQar9xwNwKBgQDOwlUamKNWfyI6WIrhp+jwG1gE57kLdcbf\nANm5bHP5XEbvFoSOpwxX3fwQM4SDlMn/FuyOjvY5r53i07nwGCxbcb2L4EBjgzcs\nrA3O61dNy6Rt/ifHBLs1Wra3yaYCKzCnsT+/3IXUSe3IEyAAJLzQuXsQ/NiJWR4V\n9YImr9nEtQKBgFZZ7fjjVCy+LMQiji/0C1napMsGIf5VWwWwi3d0b7dXhE/srk1W\n1go6YnN4OYNRGsK1XjfKqrxW21skbb+Wi9alW0Q7XXd8Cw7vBtUgBOvUL+3Bfrt9\nq6k0j11WMtH/VHamAYTzuUwpl8Ju0boD/jU61KwjE6VdOgsypibsZny5AoGBAMlm\nJrv3fvOcd1zaLr5Mbuyj1gNBLNDq8sL68xpZeEaoCjiOeKT0N2PHyeaGKEh7wJ+I\nVvkubM4YMPVoRDCJe3u/uWDtGgtVH4OWPQUX3TzcZtj1vw1voGQCbwVrmRd3trdC\nQtTDHGGDeelwJ7W8E2hFpIkRomN3uYSuVw8UME4ZAoGBAMOQQgeKODV99zNPgTmX\nHhOcx55hhBoOo8muH9yiPWfn8iGxf9rshuZjxXTX6NLruWsZtiD7LheJHdz+nFPe\nnul8b233CIn5aoFOV9EZszLm5/RrcB2733Qf50si/pCHBaRV4N1MvZNg8yeaEGhc\nQ/djJDPSEKm8ewWW7JlnRlJm\n-----END PRIVATE KEY-----\n",
  "client_email": "webquery@suasor-184008.iam.gserviceaccount.com",
  "client_id": "103981968423963988522",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/webquery%40suasor-184008.iam.gserviceaccount.com"
}

def main(params):

    data = pd.io.gbq.read_gbq(query, dialect="standard", project_id=project_id, private_key=json.dumps(private_key))

    data_json = data.to_json()
    
    return json.loads(data_json)


# for local testing
if __name__ == "__main__": 
    print(main({}))
