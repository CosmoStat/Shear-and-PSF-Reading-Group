# Contribution Guidelines

This book is an open source project and we welcome contributions from anyone. We do, however, request that you adhere to the following guidelines so that we can ensure that we maintain the best possible quality and standards.

## Issues

The easiest way to contribute to this project is by raising a "New issue". This will give you the opportunity to ask questions, report errors or even request new content.

Remember to use clear and descriptive titles for issues. We also ask that you read the available documentation and browse existing issues on similar topics before raising a new issue in order to avoid repetition.  

## Pull Requests

If you would like to take a more active roll in the development of this project you can do so by submitting a "Pull request". A Pull Requests (PR) is a way by which you can directly submit modifications or additions the content. PRs need to be reviewed by the package moderators and if accepted are merged into the master branch of the repository.

Before making a PR, be sure to carefully read the following guidelines.

### Before Making a PR

The following steps should be followed before making a pull request:

1. Log into your GitHub account or create an account if you do not already have one.

1. Go to the main repository page: [https://github.com/CosmoStat/Shear-and-PSF-Reading-Group](https://github.com/CosmoStat/Shear-and-PSF-Reading-Group)

1. Fork the repository, *i.e.* press the button on the top right with this symbol <img src="https://upload.wikimedia.org/wikipedia/commons/d/dd/Octicons-repo-forked.svg" height="20">. This will create an independent copy of the repository on your account.

1. Clone your fork of the repository.  

```bash
  git clone https://github.com/YOUR_USERNAME/Shear-and-PSF-Reading-Group
```

5. Add the original repository (*upstream*) to remote.

```bash
  git remote add upstream https://github.com/CosmoStat/Shear-and-PSF-Reading-Group
```

### Making a PR

The following steps should be followed to make a pull request:

1. Pull the latest updates to the original repository.

```bash
  git pull upstream develop
```

2. Create a new branch for your modifications.

```bash
  git checkout -b BRANCH_NAME
```

3. Make the desired modifications to the relevant pages.

4. Add the modified files to the staging area.

```bash
  git add .
```

5. Make sure all of the appropriate files have been staged. Note that all files listed in green will be included in the following commit.

```bash
  git status
```

6. Commit the changes with an appropriate description.

```bash
  git commit -m "Description of commit"
```

7. Push the commits to a branch on your fork of ModOpt.

```bash
  git push origin BRANCH_NAME
```

8. Make a pull request for your branch with a clear description of what has been done, why and what issues this relates to.

9. Wait for feedback and repeat steps 3 through 7 if necessary.

### After Making a PR

If your PR is accepted and merged it is recommended that the following steps be followed to keep your fork up to date.

1. Make sure you switch back to your local master branch.

```bash
  git checkout master
```

2. Delete the local branch you used for the PR.

```bash
  git branch -d BRANCH_NAME
```

3. Pull the latest updates to the original repository, which include your PR changes.

```bash
  git pull upstream master
```

4. Push the commits to your fork.

```bash
  git push origin master
```

### Content

Every PR should correspond to a issue that has already been raised. When you make a PR be sure to tag the issue that it resolves (*e.g.* this PR relates to issue #1). This way the issue can be closed once the PR has been merged.

### CI Tests

Continuous Integration (CI) tests are implemented via [GitHub Actions](https://docs.github.com/en/free-pro-team@latest/actions). All PRs must pass the CI tests before being merged. Your PR may not be reviewed by a moderator until all CI test are passed. Therefore, try to resolve any issues in your PR that may cause the tests to fail.
