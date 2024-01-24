# Tanks of Freedom Server

![Tanks of Freedom](https://img.itch.io/aW1hZ2UvMTc3MDUvMjI3Mzk3LnBuZw==/original/jFFytG.png)

![Tanks of Freedom II](https://img.itch.zone/aW1nLzg4NDUzNDMucG5n/original/xkK2BE.png)

## Indie Turn Based Strategy in Isometric Pixel Art

This project is a server for Tanks of Freedom and Tanks of Freedom II games. It allows players to share custom maps. It also enables online play for ToF 1.

## Client

For the source code of the clients please visit [https://github.com/w84death/Tanks-of-Freedom](https://github.com/w84death/Tanks-of-Freedom) and [https://github.com/P1X-in/tanks-of-freedom-ii](https://github.com/P1X-in/tanks-of-freedom-ii)

## Requirements

- Python 3.11.x or newer
- MySQL 5.x server
- MySQL driver for Python 3.x
  - pkg-config
  - python3-dev
  - default-libmysqlclient-dev
  - build-essential
- Virtualenv and PIP (recommended)

## Deployment

- clone the source
- Create virtualenv for the application
  - virtualenv -p /usr/bin/python3 flask
  - source flask/bin/activate
- install requirements.txt using pip
  - pip install -r requirements.txt
- create empty database and fill it using sql/database_bootstrap.sql file
  - run database migrations from sql folder
- configure app in tof_server/config.py (.dist provided)
- use run.py script to test if app works
- bind the app to the webserver of your choice (example .wsgi for apache2 provided)

## Official pages:
- Official ToF page: [tof.p1x.in](http://tof.p1x.in)
- Official ToF II page: [czlowiekimadlo.itch.io/tanks-of-freedom-ii](https://czlowiekimadlo.itch.io/tanks-of-freedom-ii)
- Official P1X page: [p1x.in](http://p1x.in)

## The MIT License (MIT)

Copyright (c) 2016 P1X

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
