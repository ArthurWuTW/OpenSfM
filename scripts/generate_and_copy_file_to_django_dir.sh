source ./param.sh

cd $DJANGO_PROJECT_DIR
ls
TODAY=$(date +"%Y_%m_%d_*")
echo $TODAY

# clean opensfm images directory
cd $OPENSFM_PLANT_DATA_IMAGES_DIR
rm -r *

# copy from django 3dconstruction_image dir
# to opensfm image directory
cp $DJANGO_3DCONSTRUCTION_IMAGE_DIR/$TODAY \
   $OPENSFM_PLANT_DATA_IMAGES_DIR/

# run opensfm_run_all
cd $REPO_DIR
bin/opensfm_run_all data/plants/

# copy mesh.json to django_project
cp $OPENSFM_DATA_PLANTS_DIR/reconstruction.meshed.json \
   $DJANGO_MESH_JSON_DIR/

#  copy images to mesh_dir/images
cd $DJANGO_MESH_JSON_DIR/images/
rm -r *.jpg
cp $OPENSFM_PLANT_DATA_IMAGES_DIR/* $DJANGO_MESH_JSON_DIR/images/
