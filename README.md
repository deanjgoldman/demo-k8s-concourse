# demo-k8s-concourse

This readme is a work-in-progress guide for setting up a git-triggered Concourse pipeline.
  
## Overview
  
This guide currently covers the following tasks:
- Create a Docker repo
- Add a build to the Docker repo from Github
- Start a local Concourse server
- Build a Concourse pipeline to automatically run a task when a change is made to the Github repo. The default task is the `hello-world` script.
- Deploy the pipeline, trigger it to test

## Requirements

Docker  
Councourse  
Fly  

## Add docker repo
https://docs.docker.com/docker-hub/repos/

Be careful about pushing to public repos! These instructions are for a demo Concourse setup.

```
docker build -t <hub-user>/<repo-name>[:<tag>]
docker tag <existing-image> <hub-user>/<repo-name>[:<tag>]
docker commit <existing-container> <hub-user>/<repo-name>[:<tag>]
docker push <hub-user>/<repo-name>:<tag>
```
  
## Open reference material
https://concoursetutorial.com/

This readme leverages the steps in https://concoursetutorial.com/, specifically the sections:

https://concoursetutorial.com/basics/basic-pipeline/
https://concoursetutorial.com/miscellaneous/docker-images/

So more can be read there if needed.

## Spin up local concourse server

https://concourse-ci.org/quick-start.html
```
wget https://concourse-ci.org/docker-compose.yml
docker-compose up -d
```
This will spin up a Concourse UI on localhost:8080, click into it and there will be a link to download Fly CLI.

## Initialize target with Fly

In the official concourse tutorial they call their target 'tutorial', we call ours 'local'

```
fly --target local login --concourse-url http://127.0.0.1:8080 -u admin -p admin
fly --target local sync
```

You may have to log in on localhost web ui admin:admin

## Build pipeline.yml

If you don't have easy access to credential storage, you can use this. Just be careful not to push the pipeline.yml file anywhere.

`python3 setup_pipeline_creds.py`

If you do have a credential storage system you can set that up, and just rename demo-pipeline.yml to pipeline.yml
  
## Push pipeline

```
fly -t local sp -p demo-ci -c pipeline.yml -n
fly -t local unpause-pipeline -p demo-ci
```

This command will trigger the job:

`fly -t local trigger-job -j demo-ci/job-hello-world -w`
  
Be aware that as long as the Concourse server is running, any changes to the Github repo will trigger this pipeline. If you need to pause the pipeline trigger you can use his command:

`fly -t local pause-pipeline --pipeline demo-ci`
  
## Check Concourse

Access pipelines at http://127.0.0.1:8080/teams/main/pipelines/demo-ci/jobs/job-hello-world/
You should see docker image build, and then display the output of _hello-world_ script.
  
## TODO

- Host repositories on private Docker Hub or Artifactory
- Incorporate actual test scripts
- Manage docker containers with Kubernetes
