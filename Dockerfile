FROM public.ecr.aws/lambda/python:3.8


COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt --target "${LAMBDA_RUNTIME_DIR}"
RUN pip install --no-cache-dir --upgrade  mangum --target "${LAMBDA_RUNTIME_DIR}"

COPY ./app ./app
COPY ./runner_lambda.py ./runner_lambda.py

CMD [ "runner_lambda.handler" ]
