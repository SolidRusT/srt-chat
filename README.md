# CLI Client for srt-core

This project provides a CLI client for the `srt-core` package.

## Installation

Clone the repository and install the dependencies:

```sh
git clone https://github.com/yourusername/new-repo.git
cd new-repo
mkdir -p ~/venvs
python -m venv ~/venvs/venv-srt-chat-dev
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage

To use the CLI client, run the following command:

```sh
cli-client --config-file=config.yaml
```

Ensure you have a `config.yaml` file in the root of your project with the necessary configuration.
