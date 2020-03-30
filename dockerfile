# Sets up docker image for NVIDIA
#FROM tensorflow/tensorflow:2.1.0-py3

# Sets up docker image for AMD using ROCm stack
# Using TF2.0 due to generator warning with :rocm3.1-tf2.1-python3
# Location of rocm/tensorflow builds: https://hub.docker.com/r/rocm/tensorflow/tags
FROM rocm/tensorflow:rocm3.1-tf2.0-python3

# Required for both NVIDIA and AMD
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  ffmpeg \
  python3-tk

COPY requirements.txt ./
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt
