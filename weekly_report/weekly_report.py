from weekly_report.cfg import load_config
import os

config = load_config(os.environ.get('env'))


##Phase 1 - COMAND LINE
"""
I want to be able to run the report from the command line
I want to be able to pass in the environment when initiallising the package
I want to be able to perform all the required functions from the command line
"""

##Phase 2 - FLASK
"""
I want to crate a web page that displays the report nicely in HTML. This will use flask.
The report will need to be able to be lifted and pasted into an email
I want a web page that will enable me to perform functions such as archive done tasks
"""
