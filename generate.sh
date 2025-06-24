#!/bin/sh

rm -rf schemas

# fetch the OpenAPI specification from the Kubernetes API server
kubectl get --raw "/openapi/v2" > swagger.json

# generate JSON Schema files from the OpenAPI specification
python openapi2jsonschema/command.py \
    --expanded --kubernetes --stand-alone --strict \
    -o schemas/master-standalone-strict \
    swagger.json
