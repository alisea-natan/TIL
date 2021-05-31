#! /bin/bash
TOKEN=`curl -d "username=$1&password=secret" http://localhost:8000/auth | sed -n '/ *"access_token": *"/ { s///; s/^.//; s/".*//; p; }'`
curl http://localhost:8000/image -H "Accept: application/json" -H "Authorization: Bearer ${TOKEN}" -o $2