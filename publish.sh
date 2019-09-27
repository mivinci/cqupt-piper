set -e

rm -rf build dist cqupt.egg-info

python3 setup.py sdist bdist_wheel

twine upload dist/*
