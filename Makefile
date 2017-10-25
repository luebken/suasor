# via http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## pip install dependencies
	 cd actions/hello; ls; docker run --rm -v "$(PWD)/actions/hello:/tmp" openwhisk/python3action sh -c "cd tmp; virtualenv virtualenv; source  virtualenv/bin/activate; pip install -r requirements.txt;"

zip: ## create zip
	 cd actions/hello; zip -r helloPython.zip virtualenv __main__.py

update: ## wsk action update
	bx wsk action update helloPython --kind python:3 --web true actions/hello/helloPython.zip

invoke: ## wsk action invoke
	bx wsk action invoke --result helloPython --param name World

curl: ## curl
	curl -s https://openwhisk.eu-gb.bluemix.net/api/v1/web/luebken_dev/default/helloPython.json?name=matt | jq .