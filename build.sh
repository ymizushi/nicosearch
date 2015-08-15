cp README.md README
python setup.py register sdist upload
git add .
git commit -m "build project"
