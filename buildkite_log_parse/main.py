import argparse
import re

import requests

from buildkite_log_parse import parser, util

API_ROOT = "https://api.buildkite.com/v2"


def bastion_build_and_job(job_name, build_state, organization, pipeline, token):
    """ Parse pipelines for active build and extract string """
    builds_url = f"{API_ROOT}/organizations/{organization}/pipelines/{pipeline}/builds"
    params = {"state": build_state}
    builds_response = requests.get(
        builds_url, params=params, headers=util.build_headers(token)
    )
    util.write_log(builds_response.text, "json", "builds")
    for build in builds_response.json():
        if build["message"].startswith("Common bastion"):  # TODO
            for job in build["jobs"]:
                if job["name"] == job_name:
                    return build, job
    return None


def build_job_log(build, job, organization, pipeline, token):
    """ Fetch log for the build's job """
    builds_url = f"{API_ROOT}/organizations/{organization}/pipelines/{pipeline}/builds"
    log_url = f"{builds_url}/{build['number']}/jobs/{job['id']}/log.txt"
    log_response = requests.get(log_url, headers=util.build_headers(token)).text
    util.write_log(log_response, "txt", "raw_log")
    return log_response


def extract_bastion_string(job_log, regex):
    """ Extract the ssh string to connect to from log """
    matcher = re.compile(regex, re.MULTILINE)
    match = matcher.match(job_log)
    breakpoint()
    return match.group()


if __name__ == "__main__":
    parser = parser.Parser()
    build, job = bastion_build_and_job(
        parser.job(),
        parser.state(),
        parser.organization(),
        parser.pipeline(),
        parser.token(),
    )
    log = build_job_log(
        build, job, parser.organization(), parser.pipeline(), parser.token()
    )
    #with open("raw_log_response.txt") as response_file:
    extract_bastion_string(response_file.read(), parser.regex())
