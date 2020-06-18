#! /usr/local/bin python3

PIPELINE_PATH_IN = "./demo-pipeline.yml"
PIPELINE_PATH_OUT = "./pipeline.yml" 

def main():
	text = open(PIPELINE_PATH_IN, "r").read()

	# make replacements
	github_uri          = input("Enter Github uri to sync with Concourse: ")
	github_branch       = input("Enter Github branch name to monitor: ")
	docker_email        = input("Enter docker email: ")
	docker_hub_username = input("Enter Docker username: ")
	docker_hub_password = input("Enter Docker password:")
	docker_hub_repo     = input("Enter Docker repo name (The github uri will send a build to this repo): ")

	text = text.replace("((github-uri))", github_uri)
	text = text.replace("((github-branch))", github_branch)
	text = text.replace("((docker-email))", docker_email)
	text = text.replace("((docker-hub-username))", docker_hub_username)
	text = text.replace("((docker-hub-password))", docker_hub_password)
	text = text.replace("((docker-hub-repo))", docker_hub_repo)
	
	# write out
	with open(PIPELINE_PATH_OUT, "w") as out:
	    out.write(text)

if __name__ == "__main__":
	main()