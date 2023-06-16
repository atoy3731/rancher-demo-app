#!/bin/bash

sed -i -e "s/REPLACE_APP/$BACKEND_APP/g; s/REPLACE_NAMESPACE/$NAMESPACE/g; s/REPLACE_PORT/$PORT/g" /etc/nginx/conf.d/default.conf

/docker-entrypoint.sh