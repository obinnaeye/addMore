[![Build Status](https://travis-ci.com/obinnaeye/addMore.svg?branch=master)](https://travis-ci.com/obinnaeye/addMore)
[![Code Climate](https://codeclimate.com/github/obinnaeye/addMore/badges/gpa.svg)](https://codeclimate.com/github/obinnaeye/addMore)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2a126147a4515f9e9490/test_coverage)](https://codeclimate.com/github/obinnaeye/addMore/test_coverage)

# AddMore
 **_Introduction/Background Information_**:
 
 A simple app used internally in an organization to record client's feature requests. A "feature request" is a request for a new feature that will be added onto an existing piece of software.

View the app [here](https://addmore.herokuapp.com)

 **_Features_**:
 
The app has the following main features:
* A UI where the user can submit a new feature request
* A UI where the user can see all feature requests
* The Client Priority of a feature is auto-rearranged in a case where a new feature request request by a client has a conflicting priority with an existing request. 
    * Case 1: When there are feature requests a, b, c, d with priorities 1, 2, 3, 4 respectively. If a new feature request e is created with priority 3, we will have a - 1, b - 2, e - 3, c - 4, d - 5. Request e has a priority of 3 while c and d changes to 4 and 5 respectively.
    * Case 2: When there are feature requests a, b, c, d with priorities 1, 2, 4, 5 respectively. If a new feature request e is created with priority 3, we will have a - 1, b - 2, e - 3, c - 4, d - 5. Request e has a priority of 3 while c and d remains 4 and 5 respectively.
    * Case 3: When there are feature requests a, b, c, d with priorities 1, 2, 4, 5 respectively. If a new feature request e is created with priority 1, we will have e - 1, a - 2, b - 3, c - 4, d - 5. Request e has a priority of 1 while a and b changes to 2 and 3 respectively, c and d remains unchanged.
    * Case 4: When there are feature requests a, b, c, d with priorities 1, 2, 4, 5 respectively. If a new feature request e is created with priority 6, we will have a - 1, b - 2, c - 4, d - 5, e - 6. Request e has a priority of 6 while the rest remains unchanged.

## API Summary

#### Note

API documentation (using swagger) is still in progress.

### Feature Requests

EndPoint | Functionality
-------- | -------------
POST /feature-request | Create a new feature request.
GET /feature-requestn | Get all feature requests

## Getting Started

#### Via Cloning The Repository:

```
# Clone the app
git clone 

# And then..
cd addmore

# Set up your virtual env and ensure you activate

# Create config file in the root directory
You can just rename configExample.py to config.py and edit the content to suit your environment

# Create a database (this project uses postgresql, but you can use any ORM database)
# Then update the configuration file with your database credentials

# Install dependencies 
pip install requirements.txt

# Run database init
python migrate.py db init

# Run database migrations with
python migrate.py db migrate

# Run the upgrade command
python migrate.py db upgrade

# You can seed your database (Optional)
python bulkInsert.py  (You can wipe the database by running python bulkDelete.py)

# Start the app
python app.py

# View the app
Navigate to http://127.0.0.1:5000/ to view the app
To see all feature requests go to http://127.0.0.1:5000/feature-request

# For test: migrate and upgrade the test db (ensure you've created the db before now)
python migrateTest.py db init --directory travisMigrations 
python migrateTest.py db migrate --directory travisMigrations 
python migrateTest.py db upgrade --directory travisMigrations 

# To run test
coverage run --source=resources,Model,app -m pytest  (this generates the coverage and also ensures that imports are not skipped in coverage)
coverage report (this displays the coverage report)
```

## Deploying to web

```
This app has been deployed to the web using passenger (and apache). See [a simple guide](https://www.phusionpassenger.com/library/walkthroughs/deploy/python/) for deploying flask app on Ubuntu.
The two required files are Passengerfile.json and passenger_wsgi.py.
In Passengerfile, we specify deployment configs. Then in passenger_wsgi, we create our app instance.
You can name passenger_wsgi anything you want, just ensure you also use the same name in Passengerfile.
With all setup completed, running the app is as simple as executing this command in the terminal
  passenger start

Currently, this app is made available to public by port forwarding. It is hosted locally and exposed to public using [localtunnel](https://localtunnel.github.io/www/). 
```


## Contributing to the project

If you are interested in participating in the development of AddMore, your ideas and contributions are welcome! It is always better to start by identifying a specific part of the app you can make better. Taking a look at the limitations is a good starting point. You can reach out to the team through the comments or [create a new issue](https://github.com/obinnaeye/addMore/issues/new).

### Git Workflow

```
git checkout develop
git pull origin develop
git checkout -b branchname
Branch Naming convention: JiraBoard-TicketNumber. eg. SR-106
Always review changes for styleguide and debug lines
git commit -m “message” (Commit messages convetion: 'BranchName:What you have done' eg. 'SR-106:Add user authentication')
git push origin branchname

Opening PR - (only against develop)

git pull --rebase origin develop
fix merge conflicts if any
git add . & git rebase --continue (if there is merge conflict)
All conflicts resolved, git push, open PR

NOTE: Pull request should be as decriptive as possible; should explain what task has been completed
```

### Style Guide & Continous Integration

```
The project is PEP8 compliant and embodies the concepts of the Zen of Python.
On github, we have integrated Hounds for automated quality checks.
TravisCI is also integrated for build. Although you can raise a PR even when build fails, Merged PRs are only automatically deployed if build passes.
With this, your PRs will not be merged if the build fails. 
```

## Limitations of the project
    Currently the project has the following limitations:

    * The feature requests are not paginated on the UI
    * The user cannot filter feature requests

    The above limitations will be handled in later versions.


## Issues?
Submit your issue [here](https://github.com/obinnaeye/addMore/issues/new)

## License

[MIT][license] Copyright (c) Nnenanya Obinna K. 2018.

<!-- Definitions -->

[license]: LICENSE
