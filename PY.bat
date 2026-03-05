@echo off
mkdir packages

pip download av -d packages
pip download pygame -d packages
pip download pillow -d packages

pip install --no-index --find-links=packages av
pip install --no-index --find-links=packages pygame
pip install --no-index --find-links=packages pillow

pause