import re

from buildkite_log_parse import fetch, parser, util


def bastion_build_and_job(job_name, build_state, build_message, organization, pipeline, token):
    """ Parse pipelines for active build and extract string """
    builds_response = fetch.builds(build_state, organization, pipeline, token)
    for build in builds_response:
        if build["message"].startswith("Common bastion"):  # TODO
            for job in build["jobs"]:
                if job["name"] == job_name:
                    return build, job
    return None


def extract_bastion_string(job_log, regex):
    """ Extract the ssh string to connect to from log """
    matcher = re.compile(regex, re.MULTILINE)
    match = matcher.match(job_log)
    # breakpoint()
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
    log = fetch.build_job_log(
        build, job, parser.organization(), parser.pipeline(), parser.token()
    )
    # with open("raw_log_response.txt") as response_file:
    extract_bastion_string(response_file.read(), parser.regex())
