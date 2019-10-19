#!/bin/sh
echo "Installing python libraries in a venv. Ensure you have python virtualenv installed"

virtualenv .env && source .env/bin/activate && pip3 install -r requirements.txt
