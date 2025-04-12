from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello_elastic_beanstalk():
    return "Hello 9 Palms!"
