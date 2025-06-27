FROM public.ecr.aws/lambda/python:3.12

COPY app ${LAMBDA_TASK_ROOT}
COPY requirements.txt  .

RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD ["create_order_handler.handler"]