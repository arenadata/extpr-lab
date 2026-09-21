# Contributing

A draft; the full version comes with stage 7 of the plan.

1. Fork the repository, create a branch and open a pull request into `develop`.
2. Unit tests run automatically (GitHub Actions) on every push to the pull request.
3. Once the unit tests are green, a maintainer reviews the code and applies the `ok-to-test` label.
   This starts the full internal check **for the current commit**.
4. Any new push to the pull request removes the label: an approval is bound to a specific SHA,
   so a maintainer has to approve the new revision again. This includes syncing your fork,
   merging `develop` into your branch, rebasing and force-pushing.
5. If your branch has many work-in-progress commits, please squash them yourself before asking
   for the label: the pull request is merged as is, with a merge commit, to keep your authorship.
6. Pull requests that add or change `.gitlab-ci.yml` are not accepted: the internal CI
   configuration is maintained separately.
