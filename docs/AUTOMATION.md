# How profile activity updates work

The workflow in `.github/workflows/profile-activity.yml` runs once a week and can also be started manually via **Actions > Suggest profile activity updates > Run workflow**.

It gathers:
- Recently merged upstream PRs by `Manantra` (from repositories owned by others).
- Recently active public repositories owned by `Manantra` that are **not forks**.

It updates only the content between `<!-- PROFILE_ACTIVITY:START -->` and `<!-- PROFILE_ACTIVITY:END -->` in the profile `README.md`. Every change becomes a **draft pull request**. It never merges anything itself. When there is no change, no PR is created.

## One-time GitHub setting

Visit the repository **Settings → Actions → General → Workflow permissions**, then enable **Allow GitHub Actions to create and approve pull requests** and save. The workflow declares `contents: write` and `pull-requests: write` for its limited-purpose token. Without the repository setting, the workflow can run but PR creation will fail. No paid Copilot subscription, personal access token, or third-party API key is required.

## Manual test

```bash
python -m unittest discover -s tests -v
GH_TOKEN="<a GitHub token>" python scripts/update_activity.py
```

The second command modifies only the managed section in your local README; use `git diff README.md` to inspect.

## Review policy

Titles and links come from the GitHub API. Submitted/closed-but-unmerged work is excluded from the automatic merged-PR list. Hand-selected descriptions and links elsewhere in the profile remain editorial content and are not rewritten by this workflow.

**Note:** A GitHub profile README is displayed only after the public `Manantra/Manantra` repository contains a root `README.md` on the default branch.
