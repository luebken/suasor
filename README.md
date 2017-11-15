# Suasor

Suasor [latin: recommender] is a playground for building recommender systems in a serverless environment.

The first POC is based on the blogpost: [Recommending GitHub Repositories with Google BigQuery and the implicit library](https://medium.com/towards-data-science/recommending-github-repositories-with-google-bigquery-and-the-implicit-library-e6cce666c77).

## Development

### Prerequisites

* The compute runs on OpenWhisk on BlueMix/IBM Cloud. This guide assumes you have an account and the [bx CLI](https://console.bluemix.net/docs/cli/reference/bluemix_cli/download_cli.html) installed.

* The data is in Google BigQuery.  This guide assumes you have Google Cloud account. 

### Setup

* Go to you Google IAM Admin and [create a service account](https://console.cloud.google.com/iam-admin/serviceaccounts/) with the Roles "Big Query Data Viewer" and "Big Query Job User". 

* Create and download the pivatekey. Export they key and the key id as `GC_SVC_PRIVATE_KEY` and `GC_SVC_PRIVATE_KEY_ID`. We recommend using a tool like [direnv](direnv.net). See [.envrc_tmpl](.envrc_tmpl).

## Deployment

Please consult the [Makefile](Makefile).

  ````
  $ make help
  build-ml-runtime               docker build & push. creates the ml runtime container.
  update                         wsk action update. updates the openwhisk action.
  invoke                         wsk action invoke. invokes the openwhisk action.
  logs                           wsk activation list & wsk logs. get the latest logs.
  local                          test locally
  curl                           curl the action 

  $ make update
  ok: updated action mainAction

  $ make invoke
  bx wsk action invoke --result mainAction --param name World
  {
    "gestation_weeks": {
        "0": 47,
        "1": 40,
        "2": 38,
        "3": 34,
        "4": 39,

  ````

## Status / Roadmap

Please consult https://github.com/luebken/suasor/projects/1

## Links / Resources

* Lambda on OpenWhisk: http://jamesthom.as/blog/2017/08/04/large-applications-on-openwhisk/

* https://moderndata.plot.ly/using-google-bigquery-with-plotly-and-pandas/

