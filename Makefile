.DEFAULT_GOAL := help

build-ml-runtime: ## docker build & push. creates the ml runtime container.
	cd actions/main; docker build -t luebken/python_ml_runtime .
	docker push luebken/python_ml_runtime

update: ## wsk action update. updates the openwhisk action.
	@cd actions/main;\
	bx wsk action update mainAction\
	 --docker luebken/python_ml_runtime\
	 --web true\
	 -p GC_SVC_PRIVATE_KEY "${GC_SVC_PRIVATE_KEY}"\
	 -p GC_SVC_PRIVATE_KEY_ID "${GC_SVC_PRIVATE_KEY_ID}"\
	 main.py

invoke: ## wsk action invoke. invokes the openwhisk action.
	bx wsk action invoke --result mainAction --param name World

# get the latest activation id
ACTIVATION_ID := $(shell bx wsk activation list |head -n2 | tail -n1 |awk '{ print $$1 }')

logs: ## wsk activation list & wsk logs. get the latest logs.
	bx wsk activation logs $(ACTIVATION_ID)

local: ## test locally
	python actions/main/main.py

curl: ## curl the action
	curl -s https://openwhisk.eu-gb.bluemix.net/api/v1/web/luebken_dev/default/mainAction.json?name=matt | jq .

# via http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
