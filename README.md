# The GDELT Project Tools

See [GDELT 2.0: Our Global World in Realtime](https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/)


### Command line parameters
```
python manage.py --help
```

- extract {options} - extract/dowload raw source data set
```
python manage.py extract -b /media/vola/gdelt2 -d 2015-01-01T00:00:00 -n 2015-12-31T23:59:59   
  
```

### Development convention
- use python v. 3.8;
- use [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) as coding convention;
- use pytest as project test framework, test coverage: standard input and corner cases, exception/IO errors;
- use pylint for code style check, requirement: 0 warnings;
- use mypy for static code check, requirement: 0 warnings. 
- use [git workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) convention while development.
- branch naming convention: ```(feature|hotfix)/<task_num>-short-description```
- commit comment convention: ```<task_num> | short description```

### Local development environment

- Install Dependencies
```
virtualenv -p python3.8 .venv
source .venv/bin/activate
pip install --upgrade pip && pip install -r requirements/requirements_dev.txt
```

- Run tests

```
source .venv/bin/activate
pytest
```

- Run code style and type checks

```
source .venv/bin/activate
pylint gdelt20*
mypy gdelt20*
```

###### Avro schema validation

Please use fast avro [command line script](https://fastavro.readthedocs.io/en/latest/command_line_script.html) to validate are generated schemas


# Environment variables (local & CI/CD environments)

For CI/CD branch-dependent target build should be set following environment variables: 
- build from master branch:
```
ENV  
```

- build from develop branch:
```
ENV  
```

## CI/CD builds

### Docker build
- set Environment variables
(TODO: fix after Fargate implementation)
```
```
- build container & run
```
bin/docker_build.sh
bin/docker_run.sh
```

### make build & run
Please run make to get help for are defined targets:

```make```

```
output - 
make help              - print target list
make venv_create       - create virtual environment
make venv_packages     - install dependencies to virtual environment
...

Note: for local & CI/CD pre-reqirements please see Environment variables
