#!/usr/bin/env python3

import json
import subprocess
import sys

def list_databases():
    if len(sys.argv) == 1:
        process = subprocess.run(["./terminusdb", "list", "--json"], capture_output=True)
    else:
        process = subprocess.run(["sudo", "docker", "exec", "-it", "terminusdb", "./terminusdb", "list", "--json"], capture_output=True)
    return json.loads(process.stdout)

def run_optimize(descriptor: str):
    if len(sys.argv) == 1:
        process = subprocess.run(["./terminusdb", "optimize", descriptor])
    else:
        process = subprocess.run(["sudo", "docker", "exec", "-it", "terminusdb", "./terminusdb", "optimize", descriptor])

def run_commits_for_all_dbs(dbs):
    for db in dbs:
        commit_graph = db['database_name'] + '/local/_commits'
        run_optimize(commit_graph)

def run_meta_for_all_dbs(dbs):
    for db in dbs:
        meta_graph = db['database_name'] + '/_meta'
        run_optimize(meta_graph)


dbs = list_databases()
run_meta_for_all_dbs(dbs)
run_commits_for_all_dbs(dbs)
run_optimize('admin/profiles')
run_optimize('_system')
