# Tanks of Freedom Server

![Tanks of Freedom](https://i.imgur.com/Xa66BXO.png)

## Indie Turn Based Strategy in Isometric Pixel Art

This project is a server for Tanks of Freedom game. It allows players to share custom maps and play online matches (multiplayer is still in development)

## Client

For the source code of the client please visit [https://github.com/w84death/Tanks-of-Freedom](https://github.com/w84death/Tanks-of-Freedom)

## Requirements

- Python 3.x
- MySQL 5.x server
- MySQL driver for Python 3.x
- Flask
- Virtualenv and PIP (recommended)

## Instalation

- Create virtualenv for the application
- clone the source into the new environment
- install requirements.txt using pip
- create empty database and fill it using sql/database_bootstrap.sql file
- configure app in tof_server/config.py (.dist provided)
- bind the app to the webserver of your choice (example .wsgi for apache2 provided)

## Official pages:
- Official game page: [tof.p1x.in](http://tof.p1x.in)
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
