#!/bin/sh

# Reading variables from .env file.
if [ -f .env ] && [ -s .env ]
then
    export $(xargs <.env)
    # Check for DEVELOPMENT_IDE env variable.
    if [ "$DEVELOPMENT_IDE" = "vscode" ]; then
        tail -f /dev/null
    fi
fi
