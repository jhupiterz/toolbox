# Project description

!!! This package is under construction !!!

- Data Science and Machine Learning `toolbox` package containing useful functions for future DS and ML projects
- `test` contains Python codes for testing each function (e.g. `tests/test_weather_forecast.py` tests `weatherforecast.py`)

# Next adds to the toolbox

- Baseline functions for data visualization including: 
    * distribution graphs
    * boxplots
    * pairplots
    * correlation heatmaps

- Baseline pipelines for data preprocessing including:
    * Handle NaNs, duplicates, and outliers
    * Data type conversions
    * Scaling

- More to come...

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for toolbox in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/toolbox`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "toolbox"
git remote add origin git@github.com:{group}/toolbox.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
toolbox-run
```

# Install

Go to `https://github.com/{group}/toolbox` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/toolbox.git
cd toolbox
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
toolbox-run
```
