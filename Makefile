.DEFAULT_GOAL := help

build: ## docker build & push. creates the ml runtime container 
	cd actions/main; docker build -t luebken/python_ml_runtime .
	docker push luebken/python_ml_runtime

update: ## wsk action update
	cd actions/main; bx wsk action update mainAction --docker luebken/python_ml_runtime --web true main.py

invoke: ## wsk action invoke
	bx wsk action invoke --result mainAction --param name World

local: ## test locally
	python actions/main/main.py

curl: ## curl the action
	curl -s https://openwhisk.eu-gb.bluemix.net/api/v1/web/luebken_dev/default/mainAction.json?name=matt | jq .

# via http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
