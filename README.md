# VPet
Lightweight reimplementation of [VPet](https://github.com/LorisYounger/VPet)

Supports only Linux and X11. Written using C.

Currently WIP.

### Usage

```sh
# create virtual env
python3 -m venv venv

# activate venv
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt

# convert sprites to spritesheets
python3 scripts/convert-assets.py

# compile program
make

# launch program
./vpet
```
