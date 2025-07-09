FROM python:3.10.12-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y git 

RUN pip install "mlip>=0.1.2" "jax[cuda12]==0.4.33" huggingface_hub git+https://github.com/jax-md/jax-md.git notebook

COPY starter_notebook.ipynb .
COPY data data
COPY training training

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]