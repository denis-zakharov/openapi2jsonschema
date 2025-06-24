#!/bin/sh

echo "JSON output:"
kubeconform -summary -output json -strict -schema-location schemas k8s-yamls

echo

echo "JUnit output:"
kubeconform -output junit -strict -schema-location schemas k8s-yamls
