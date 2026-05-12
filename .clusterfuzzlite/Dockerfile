FROM gcr.io/oss-fuzz-base/base-builder-python@sha256:12ff780af15b8c65c24b544781a8b7576e740ac4fbc0c9a04d70d9256582a9f3

COPY . $SRC/skeuomorphic-forge
WORKDIR $SRC/skeuomorphic-forge
COPY .clusterfuzzlite/build.sh $SRC/
