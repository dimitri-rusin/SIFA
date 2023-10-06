# Use an official NVIDIA CUDA base image with Python 2.7
FROM nvidia/cuda:11.8.0-base-ubuntu18.04

# Set Python 2.7 as the default Python version
RUN apt-get update && apt-get install -y \
    python2.7 \
    python-pip \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/bin/python2.7 /usr/bin/python

# Upgrade pip for Python 2.7
RUN python -m pip install --upgrade pip

# Copy requirements.txt into the container
COPY requirements.txt /tmp/

# Install Python packages from requirements.txt
RUN pip install --default-timeout=300 -r /tmp/requirements.txt

# Set the working directory
WORKDIR /app

# Copy the rest of the application into the container
COPY . /app/

# Add a non-root user with the same user and group ID as your host machine.
RUN addgroup --gid 1000 appuser && \
    adduser --uid 1000 --ingroup appuser --home /home/appuser --shell /bin/sh --disabled-password --gecos "" appuser

# Switch to the non-root user
USER appuser

# Command to run the application
CMD ["/bin/bash", "-c", "python utils/savenpz.py && python evaluate.py"]
