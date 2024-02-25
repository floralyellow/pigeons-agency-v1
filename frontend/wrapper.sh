#!/bin/sh

if [ "$FRONTEND_ENV" = "production" ]; then
    sh entrypoint_prod.sh
else
    sh entrypoint.sh
fi