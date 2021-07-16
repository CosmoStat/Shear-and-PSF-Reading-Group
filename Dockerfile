FROM continuumio/miniconda3

LABEL Description="ShearBook Docker Image"
WORKDIR /home
ENV SHELL /bin/bash

RUN git clone https://github.com/CosmoStat/Shear-and-PSF-Reading-Group.git

RUN cd Shear-and-PSF-Reading-Group && \
    git checkout develop && \
    conda env create -f environment.yml

ENV PATH /opt/conda/envs/shearbook/bin:$PATH

RUN echo "path: $PATH"

RUN echo "path: $PATH" && \
    cd Shear-and-PSF-Reading-Group && \
    python setup.py install
