FROM ghcr.io/railwayapp/nixpacks:ubuntu-1725321821

ENTRYPOINT ["/bin/bash", "-l", "-c"]
WORKDIR /app/


COPY .nixpacks/nixpkgs-bf446f08bff6814b569265bef8374cfdd3d8f0e0.nix .nixpacks/nixpkgs-bf446f08bff6814b569265bef8374cfdd3d8f0e0.nix
RUN nix-env -if .nixpacks/nixpkgs-bf446f08bff6814b569265bef8374cfdd3d8f0e0.nix && nix-collect-garbage -d


ARG NIXPACKS_METADATA PIP_DEFAULT_TIMEOUT PIP_DISABLE_PIP_VERSION_CHECK PIP_NO_CACHE_DIR PYTHONDONTWRITEBYTECODE PYTHONFAULTHANDLER PYTHONHASHSEED PYTHONUNBUFFERED
ENV NIXPACKS_METADATA=$NIXPACKS_METADATA PIP_DEFAULT_TIMEOUT=$PIP_DEFAULT_TIMEOUT PIP_DISABLE_PIP_VERSION_CHECK=$PIP_DISABLE_PIP_VERSION_CHECK PIP_NO_CACHE_DIR=$PIP_NO_CACHE_DIR PYTHONDONTWRITEBYTECODE=$PYTHONDONTWRITEBYTECODE PYTHONFAULTHANDLER=$PYTHONFAULTHANDLER PYTHONHASHSEED=$PYTHONHASHSEED PYTHONUNBUFFERED=$PYTHONUNBUFFERED

# setup phase
COPY . /app/.
RUN  pip install --upgrade pip
RUN  pip install -r requirements.txt

# start phase
# noop

# install phase
ENV NIXPACKS_PATH=/opt/venv/bin:$NIXPACKS_PATH
COPY . /app/.
RUN --mount=type=cache,id=JfmXmcksRQ-/root/cache/pip,target=/root/.cache/pip python -m venv --copies /opt/venv && . /opt/venv/bin/activate && pip install -r requirements.txt

# build phase
COPY . /app/.
RUN  python manage.py migrate



RUN printf '\nPATH=/opt/venv/bin:$PATH' >> /root/.profile


# start
COPY . /app
CMD ["python manage.py migrate && gunicorn employee_app.wsgi"]

