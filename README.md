# demo-k8s-concourse

# Requirements

Docker
Councourse
Fly

## Add docker repo
https://docs.docker.com/docker-hub/repos/

Be careful about pushing to public repos

```
docker build -t <hub-user>/<repo-name>[:<tag>]
docker tag <existing-image> <hub-user>/<repo-name>[:<tag>]
docker commit <existing-container> <hub-user>/<repo-name>[:<tag>]
docker push <hub-user>/<repo-name>:<tag>
```

## Spin up local concourse server

https://concourse-ci.org/quick-start.html
```
wget https://concourse-ci.org/docker-compose.yml
docker-compose up -d
```
## Initialize Fly CLI

https://concoursetutorial.com/
In these tutorial they call their target 'tutorial', we call ours 'local'

```
fly --target local login --concourse-url http://127.0.0.1:8080 -u admin -p admin
fly --target local sync
```

May have to log in on localhost web ui admin:admin

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
  
Be aware that as long as the Concourse server is running, any changes to the github repo will trigger this pipeline. If you need to pause the pipeline trigger you can use his command:

`fly -t local pause-pipeline --pipeline demo-ci`
  
## Check Concourse

Access pipelines at http://127.0.0.1:8080/teams/main/pipelines/demo-ci/jobs/job-hello-world/
You should see docker image build, and then display the output of `hello-world` script.