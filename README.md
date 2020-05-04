# buildkite-log-parse

Parse orgs pipelines for active build/job and parse string


## Example

```
python -m buildkite_log_parse.main --organization org-1 \
    --pipeline bastion-server \
    --token qwertyuiopasdfghjklzxcvbnm1234567890asda \
    --regex "Access it for the next hour by running ssh (.*)" \
    --build_message "Common bastion.*" \
    --build_state "running" \
    --job "Run Server"
```
