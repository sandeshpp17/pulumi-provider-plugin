<<<<<<< HEAD
# Infrastructure as Code (IaC) with Pulumi, Python, and uv

This repository demonstrates using [Pulumi](https://www.pulumi.com/) and a custom Python dynamic provider to manage resources via infrastructure code. The project leverages [uv](https://astral.sh/docs/uv/) for Python dependency management and virtual environment creation, and includes a simple Flask service as a backend API.

## Features

- **Python dynamic provider** for Pulumi (no official provider required)
- **uv** for super-fast Python workflows (package management, running scripts)
- **Flask-based mock API** service for CRUD operations on “tables”
- Infrastructure code and Python app all in a single, easy repo

## Quick Start

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- [uv](https://astral.sh/docs/uv/) for Python (see install below)

### 1. Clone the Repo

```bash
git clone https://gitlab.com/your-org/iac.git
cd iac
```

### 2. Install Pulumi CLI

```bash
curl -fsSL https://get.pulumi.com | sh
```

### 3. Install uv (Python workflow tool)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
If you get a permission or PATH error:
- Restart your shell, or
- `export PATH="$HOME/.local/bin:$PATH"`

### 4. Install Project Dependencies

This project uses `pyproject.toml` for dependency management.

```bash
uv sync
```

You can check for dependencies:
```bash
uv pip list
```

### 5. Start the Mock Flask Service

The mock API service (for Pulumi resource CRUD) runs on port 8000:

```bash
uv run service.py 8000
```

You should see logs from Flask indicating it’s listening on `http://localhost:8000`.

### 6. Configure Pulumi

Tell Pulumi where the backend API runs:

```bash
pulumi config set mock-service:endpoint http://localhost:8000
```

### 7. Deploy Your Infrastructure

Initialize or select your Pulumi stack and run an update:

```bash
pulumi up
```

Approve when prompted. On success, your resource will be created via HTTP POST to the mock service.

### 8. Explore/Debug

See current tables in the mock service with:

```bash
curl -X GET http://localhost:8000/table
```

## Common Commands

- **Run Flask service**  
  `uv run service.py 8000`

- **Install (or update) dependencies**  
  `uv sync`

- **Add packages**  
  `uv add flask`

- **Preview infra changes**  
  `pulumi preview`

- **Deploy infra changes**  
  `pulumi up`

- **Destroy resources**  
  `pulumi destroy`

## Repo Structure

```
├── __main__.py           # Pulumi program entry-point
├── table_resource.py     # Dynamic resource class
├── table_provider.py     # Provider implementation (CRUD logic)
├── service-api
│   └── service.py        # Flask mock service
├── pyproject.toml        # Python dependencies (for uv)
├── Pulumi.yaml           # Pulumi project metadata
├── requirements.txt      # (Optional; legacy support)
└── README.md             # This file!
```

## Troubleshooting

- **Type errors (e.g., “Field size should be type int, received type float”)**  
  Ensure your Pulumi dynamic provider casts numbers to `int` before sending them to the backend.

- **Module/Import errors**  
  Make sure all .py files are at the repo root and that uv has synced your dependencies (`uv sync`).

- **Service not reachable**  
  Double-check Flask is running at the same port you’ve set in `pulumi config`.

## References

- [Pulumi: Python Dynamic Providers](https://www.pulumi.com/docs/intro/concepts/resources/dynamic-providers/)
- [uv: Fast Python Workflow Tool](https://astral.sh/docs/uv/)
- [Flask: Python Web Microframework](https://flask.palletsprojects.com/)
- [pyproject.toml specification](https://peps.python.org/pep-0518/)

[1] https://get.pulumi.com
[2] https://astral.sh/uv/install.sh
=======
# iac



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://git.enlight.dev/enlight360containers/iac.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://git.enlight.dev/enlight360containers/iac/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
>>>>>>> 0cddb5d (Initial commit)
