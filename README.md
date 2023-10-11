
## 
```bash
# create virtual environment
python3 -m venv .env

# activate virtual environment
source .env/bin/activate

# install dependencies
pip install -r requirements.txt

# freeze dependencies
pip freeze > requirements.txt

# run server
python3 manage.py runserver
```

## Git setup
```bash
# show git folder on mac
defaults write com.apple.finder AppleShowAllFiles YES

# show git folder on vscode
command + shift + p
# > toggle hidden filesi
# en francais
# > basculer les fichiers masqués
```

```bash

# view .git folder
ls -a .git

# delete .git folder
rm -rf .git

# stop tracking files
git rm -r --cached .

# view current git config
git config --list