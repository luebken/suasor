install:
	 cd actions/hello; ls; docker run --rm -v "$(PWD)/actions/hello:/tmp" openwhisk/python3action sh -c "cd tmp; virtualenv virtualenv; source  virtualenv/bin/activate; pip install -r requirements.txt;"

zip:
	 cd actions/hello; zip -r helloPython.zip virtualenv __main__.py

update:
	bx wsk action update helloPython --kind python:3 actions/hello/helloPython.zip

invoke:
	bx wsk action invoke --result helloPython --param name World