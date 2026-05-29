# 42 Málaga Tutorials

Tutorial collection for 42 Málaga students — Docker environments, Git workflows, and Shell scripting.

## Contents

- **[42Container](./42Container/)** — Docker-based 42 school environment (norminette, valgrind, Minishell libs). Run `42` from any project directory.
- **[GIT](./GIT/)** — Hands-on Git tutorials from setup to advanced workflows: cherry-pick, worktree, stashing, merge strategies, and best practices.
- **[Shells_42M](./Shells_42M/)** — Slidev presentation comparing Bash vs Zsh vs Fish with syntax comparisons, tables, and Fish productivity functions. Deployed via GitHub Pages.

## Quick Start

```bash
# 42Container (requires Docker)
cd 42Container && ./run.sh && ./setup_alias.sh

# View Git tutorials
open GIT/00_set_up.md

# Run Slidev presentation
cd Shells_42M && pnpm install && pnpm dev
```
