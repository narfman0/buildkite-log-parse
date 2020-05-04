import argparse
import os


class Parser:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Extract string from buildkite job"
        )
        parser.add_argument("--organization", help="Organization name, e.g. org-1")
        parser.add_argument("--pipeline", help="Pipeline slug")
        parser.add_argument("--token", help="Buildkite token")
        parser.add_argument("--regex", help="Regex to search in logs")
        parser.add_argument("--build", help="Build message")
        parser.add_argument("--job", help="Job name")
        parser.add_argument("--state", help="Build state, e.g. running")
        self.args = parser.parse_args()

    def organization(self):
        return self.args.organization or os.environ["ORGANIZATION"]

    def pipeline(self):
        return self.args.pipeline or os.environ["PIPELINE"]

    def token(self):
        return self.args.token or os.environ["TOKEN"]

    def regex(self):
        return self.args.regex or os.environ["REGEX"]

    def build(self):
        return self.args.build or os.environ["BUILD"]

    def job(self):
        return self.args.job or os.environ["JOB"]

    def state(self):
        return self.args.state or os.environ["STATE"]
