
import os, sys

# change cwd to project dir
import sys

proj_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
print('proj_dir:', proj_dir)
os.chdir(proj_dir)

# START
# PYTHON = '/data/hqx/miniconda3/envs/GeoFormer/bin/python -u'
PYTHON = sys.executable
os.system(f'cd lightning && PYTHONPATH=../ {PYTHON} train_homo_geoformer.py')
