rm requirements.txt
pipreqs .
rm -r build
rm -r infer_gender.egg-info
rm -r dist
python setup.py sdist bdist_wheel
twine check dist/*
#twine upload --repository testpypi dist/*
twine upload --repository pypi dist/*