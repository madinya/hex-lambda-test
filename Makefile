LOGIN=1
ENV=stage
ECR_URI=TODO
ECR_NAME=fast-api-lambda
AWS_REGION=us-east-1
login_ecr:
	if [ "$(LOGIN)" = "1" ]; then \
		echo "LOGGING INTO THE ECR" ; \
		aws ecr get-login-password --region $(AWS_REGION) | docker login --username AWS --password-stdin $(ECR_URI) ; \
	else \
		echo "LOGIN SKIPPED" ; \
	fi

build_lambda: OSX=$(if $(filter $(shell uname -s),Darwin),1,0)
build_lambda: TIMESTAMP=$$(date --utc +%Y-%m%d-%H%M-%S)
build_lambda: GIT_HASH=$$(git rev-parse --short HEAD)
build_lambda: ENV_NAME=''
build_lambda: PUSH=1
build_lambda: OSX=0
build_lambda: Dockerfile login_ecr
	PUSH=$(PUSH) ECR_URI=$(ECR_URI) OSX=$(OSX) \
		TIMESTAMP=$(TIMESTAMP) GIT_HASH=$(GIT_HASH) \
		DOCKER_FILE=$< ./docker-build-and-push.sh

## Build docker image for app locally (credentials aren't needed)
## ENV variable has to be provided (e.g. make build_app ENV=stage)
## ENV -> prod | stage
build_app: OSX=$(if $(filter $(shell uname -s),Darwin),1,0)
build_app: TIMESTAMP=$$(date $(if $(filter $(OSX),0),--utc,) +%Y-%m%d-%H%M-%S)
build_app: GIT_HASH=test-$(ENV)
build_app: ECR_URI=test-$(ENV)
build_app: AWS_REGION=us-east-1
build_app: LOGIN=0
build_app: PUSH=0
build_app: Dockerfile login_ecr
	PUSH=$(PUSH) ECR_URI=$(ECR_URI) OSX=$(OSX) \
		TIMESTAMP=$(TIMESTAMP) GIT_HASH=$(GIT_HASH) LATEST=$(LATEST) \
		DOCKER_FILE=$< ./docker-build-and-push.sh


## Build docker image for app and push it to remote docker repo (ECR)
## ENV variable has to be provided (e.g. make build_and_push_app ENV=stage)
## ENV -> prod | stage
## LOGIN -> 0 | 1
build_and_push_app: GIT_HASH=$$(git rev-parse --short HEAD)
build_and_push_app:
	make build_app LOGIN=$(LOGIN) PUSH=1 ENV=$(ENV) \
	GIT_HASH=$(GIT_HASH) ECR_URI=$(ECR_URI) AWS_REGION=$(AWS_REGION)
