#!/bin/bash
playwright install-deps
playwright install firefox
gunicorn -w 4 -b 0.0.0.0:8080 main:app
