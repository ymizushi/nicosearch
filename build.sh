cp README.md README
git add .
git commit -m "build project"
git push origin master
python setup.py register sdist upload
