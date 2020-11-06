lint:
	python3 -m flake8 mta_data 

lint-fix:
	python3 -m autopep8 --in-place -r -a -a mta_data
	make lint