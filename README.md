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
git clone https://github.com/sandeshpp17/pulumi-provider-plugin
cd pulumi-provider-plugin 
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
