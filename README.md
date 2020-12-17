# OpenSfm

## Prerequisites
#### 1. **[django_project](https://github.com/ArthurWuTW/django_project)** Run website app in its own docker container
#### 2. **[django_project](https://github.com/ArthurWuTW/django_project)** Server has received a sequence of images from raspberry in the field
#### 3. **[docker-script-opensfm](https://github.com/ArthurWuTW/docker-script-opensfm)** Build Docker Image

# Run 3D reconstructon app
#### 1. start container and enter container shell in **[docker-script-opensfm](https://github.com/ArthurWuTW/docker-script-opensfm)**
#### 2. setup params in scripts/generate_and_copy_file_to_django_dir.sh. If you place django_project in Desktop directory, use default settings and skip this step.
```sh

export DJANGO_PROJECT_DIR=$HOME/Desktop/django_project
export REPO_DIR=$(realpath $(realpath $(dirname $PWD)))
export OPENSFM_DATA_PLANTS_DIR=$REPO_DIR/data/plants
export OPENSFM_PLANT_DATA_IMAGES_DIR=$REPO_DIR/data/plants/images
export DJANGO_3DCONSTRUCTION_IMAGE_DIR=$DJANGO_PROJECT_DIR/data_3dConstruction_image
export DJANGO_MESH_JSON_DIR=$DJANGO_PROJECT_DIR/data_3dConstruction_meshJson

...

```

#### 3. Run the app
```sh
cd scripts
python3 django_3d_reconstruction.py
```
