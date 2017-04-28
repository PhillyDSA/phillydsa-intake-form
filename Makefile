info:
	@python --version
	@pyenv --version
	@pip --version

clean:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' ! -name '*.un~' -exec rm -f {} \;

lint:
	pre-commit run -a

test:
	pytest --cov
	coverage html

dev:
	pyenv install -s 3.6.0
	# Make will continue here in the event that the virtualenv already exists
	- pyenv virtualenv 3.6.0 phillydsa-intake-form
	pyenv local phillydsa-intake-form
	pip install -r requirements/dev.txt
	pre-commit install

install:
	pip install -Ur requirements/dev.txt

env:
	pyenv install -s 3.6.0
	pyenv local 3.6.0

ci: clean env info test
	codecov

deploy:
	ansible-playbook --private-key=.vagrant/machines/default/virtualbox/private_key -u vagrant -i ansible/hosts ansible/dsa_intake.yml -vvvv
