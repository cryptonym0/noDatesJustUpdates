#!/bin/bash
echo "Installing Poetry for Azure Devops Build"
curl -sSL https://install.python-poetry.org | python3 -
export PATH=$PATH:$HOME/.local/bin
echo "##vso[task.prependpath]$HOME/.local/bin"
poetry install --no-root
