from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

class TestCaseBaidu(HttpRunner):
    config("百度")
    .base_url