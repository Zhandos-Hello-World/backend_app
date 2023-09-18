FROM python:3.11 as requirements-stage

WORKDIR /tmp

RUN pip install poetry==1.5.0

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --with=dev

FROM python:3.11



WORKDIR /app
# Copy the generated requirements.txt from the requirements stage
COPY --from=requirements-stage /tmp/requirements.txt .

# Install project dependencies using pip
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt


COPY . . 

ENTRYPOINT ["sh", "./scripts/launch_prod.sh"]