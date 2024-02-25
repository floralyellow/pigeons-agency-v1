#!/bin/sh

if [ "$NODE_ENV" = "production" ]; then
    sh entrypoint_prod.sh
else
    sh entrypoint.sh
fi