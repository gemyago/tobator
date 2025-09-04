# Instruction to create pull request

1. Look on a commit history between a base (if not mentioned otherwise, use **main**). You will need to run command like below 
```bash
#  to get current branch, you will use it in step 5
git branch --show-current

# Get most recent changes from base branch
git fetch origin <base branch>

# git log (add origin to base branch when comparing)
git log origin/<base branch>..HEAD --oneline | cat
```

2. Review commit history and come up with a sensible PR title
3. Review commit history and come up with a sensible PR description, it should follow the following format:
  * Short change description 1
  * Short change description 2
  * ...
4. Prepare PR title and description in the following format:
  ```md
  **PR title**: 
  <PR title>
  ---
  **PR description**: 
  <PR description>
  ```
5. Push pending changes and create a PR with a command below:
```bash
git push origin <current branch> --set-upstream

# Create a PR with a properly formatted, multi-line body using a here-document and --body-file -
gh pr create --title "<PR title>" --body-file - --base <base branch> --head <current branch> <<EOF
<PR description>
EOF
```
6. Show the PR to the user as a clickable URL so user can click it, as well as full URL for copying.