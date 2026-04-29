# webhooks

Centralised GitHub Actions reusable workflows for the
[event-driven-vision-school](https://github.com/event-driven-vision-school) organisation.

All assignment repositories (and their student forks) reference these workflows
via the `uses:` key, so every repo automatically picks up the latest version
without needing to update individual forks.

## Workflows

| Workflow | Description |
|---|---|
| [`classroom.yml`](.github/workflows/classroom.yml) | Runs the smoke-test suite inside the Codespaces Docker image and updates the gradebook |
| [`publish-docker.yml`](.github/workflows/publish-docker.yml) | Builds and pushes the Codespaces Docker image to GHCR |
| [`build-hidden-tests.yml`](.github/workflows/build-hidden-tests.yml) | Compiles the Cython hidden-test extension and commits the `.so` files to `main` |

## Usage

In any assignment repository, replace each workflow body with a single `uses:` call:

```yaml
jobs:
  call-smoke-test:
    uses: event-driven-vision-school/webhooks/.github/workflows/classroom.yml@main
    secrets: inherit
```

Inputs accepted by `classroom.yml`:

| Input | Default | Description |
|---|---|---|
| `gradebook_repo` | `event-driven-vision-school/gradebook` | Org/repo of the gradebook to update |

## Required secrets

| Secret | Where to store it | Used by |
|---|---|---|
| `GRADEBOOK_TOKEN` | Assignment repo or org-level secret | `classroom.yml` |
| `GITHUB_TOKEN` | Automatic | `publish-docker.yml`, `build-hidden-tests.yml` |
