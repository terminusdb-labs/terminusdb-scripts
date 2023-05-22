#!/bin/bash
BRANCH=$1
TERMINUSDB_FOLDER="${BRANCH}_${RANDOM}"

git clone https://github.com/terminusdb/terminusdb.git --branch $BRANCH --single-branch "$TERMINUSDB_FOLDER"
cd "$TERMINUSDB_FOLDER"
sudo docker buildx build . -t "terminusdb/terminusdb-server:$BRANCH"
sudo docker push "terminusdb/terminusdb-server:$BRANCH"

