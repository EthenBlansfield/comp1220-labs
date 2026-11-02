# COMP1220 Labs: Intro to Computer Science (NNU, Fall 2026)

This repository holds the starter files for the COMP1220 programming labs. You will **fork** it, do your work in your own fork, and **push** your changes there.

| Lab | Folder | Instructions |
|---|---|---|
| Lab 5: Algorithms in Python | `Lab5/` | [Lab5/Main_Lab_Instructions.md](Lab5/Main_Lab_Instructions.md) |
| Lab 7: Classes in Python | `Lab7/` | [Lab7/README.md](Lab7/README.md) |

---

## One-time setup (about 15 minutes)

### 1. Install the tools

- **Git**: <https://git-scm.com/downloads>. On Windows, accept the defaults. This also installs **Git Bash**.
- **Python 3.10 or newer**: <https://www.python.org/downloads/>. On Windows, check **"Add python.exe to PATH"** on the first screen of the installer.
- **An editor**: VS Code (<https://code.visualstudio.com/>) is recommended.

Check that both work. Open a terminal (Git Bash on Windows, Terminal on Mac) and run:

```bash
git --version
python --version
```

(On a Mac, use `python3` wherever these instructions say `python`.)

### 2. Make a GitHub account

Sign up at <https://github.com/signup>. Using your `@my.nnu.edu` email is fine.

### 3. Tell Git who you are

Use the **same email** as your GitHub account:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@my.nnu.edu"
```

### 4. Fork this repository

1. Make sure you are signed in to GitHub, then open this repository's page.
2. Click **Fork** (top right), then **Create fork**.
3. You now have your own copy at `https://github.com/<your-username>/comp1220-labs`. **All of your work goes there**, not into the instructor's repository.

> Forks of a public repository are public. Do your own work, and do not copy from a classmate's fork. NNU's academic integrity policy applies.

### 5. Clone **your fork** to your computer

On your fork's page, click the green **Code** button and copy the HTTPS URL. Then run:

```bash
git clone https://github.com/<your-username>/comp1220-labs.git
cd comp1220-labs
```

The first time you push, Git opens a browser window so you can sign in to GitHub. Choose **Sign in with your browser**.

---

## Doing a lab

```bash
cd comp1220-labs/Lab5
python p1_loop_control.py        # run a problem's self-checks
```

Edit the files in your editor and run them again until the checks pass.

### Save your work to GitHub (do this often)

```bash
git add .
git commit -m "Finish Problem 1"
git push
```

- **`git add .`** stages every changed file.
- **`git commit`** saves a snapshot with a message describing what you did.
- **`git push`** uploads your commits to your fork on GitHub.

Commit after each problem, not only at the end. If your laptop dies, everything you pushed is safe.

Refresh your fork's page on GitHub to confirm your changes are there. **What is on GitHub at the deadline is what gets graded.**

### Submitting

Submit your fork's URL (`https://github.com/<your-username>/comp1220-labs`) on the Canvas assignment. Your last push before the due time is graded.

---

## When a new lab is released

New lab folders are added to this repository during the semester. To pull them into your fork:

1. On **your fork's** GitHub page, click **Sync fork**, then **Update branch**.
2. On your computer, run:

   ```bash
   git pull
   ```

Do this **after** you have committed and pushed your own work.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `python: command not found` | Try `python3` or `py`. On Windows, reinstall Python with "Add to PATH" checked. |
| `ModuleNotFoundError: lab5_checks` | Run the file from **inside** the `Lab5` folder (`cd Lab5` first). |
| `git push` is rejected with `fetch first` | Run `git pull`, then `git push` again. |
| `Permission denied` / `403` on push | You cloned the instructor's repo instead of your fork. Check with `git remote -v`. It should show **your** username. |
| Git asks for a password | GitHub no longer accepts account passwords here. Choose the browser sign-in option. |
| Something is very wrong | Ask in class or office hours. Don't delete your fork. |
