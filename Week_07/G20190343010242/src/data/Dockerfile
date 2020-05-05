# Use base Python image from Docker Hub
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY data/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install ptvsd for debugging
RUN pip install ptvsd

# Copy the rest of the working directory contents into the container at /app
COPY data/. .

COPY common/. .

COPY setup.py .

RUN pip install -e .

RUN pip freeze

# Run data_pipeline.py when the container launches
ENTRYPOINT ["python", "data_pipeline.py"]
