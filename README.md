# test-project

Small, deliberately boring repository used to exercise the multi-agent
orchestrator end to end: one route table, one test file, one `verify` entry
point.

## Verify

```sh
./verify
```

Runs the whole local check set (currently `python3 -m unittest discover`).
The orchestrator runs exactly this command before it is allowed to push
anything, so keep it fast and keep it honest.
