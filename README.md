# micro-commander
An application that lets you control your operating system using speech.

## System Requirements
- `python3.5`

## Installation
Run `make install` or
- manually create virtualenv
- `pip install -r requirements.txt` 

## PyCharm configuration
 - Right click on `src` and `test`, then `Mark Directory as` > `Sources Root`
 - To configure virtualenv: `Settings` > `Project: micro-commander` > `Project Interpreter`
 - To configure tests: `Settings` > `Tools` > `Python Integrated Tools` > `Testing` > `Default test runner` = `pytest`

## Hints
- run `make help`
- In case of `PyAudio` collecting issue, your device probably does not have the `portaudio` library. Please consider installig the module by typing `sudo apt-get install libasound-dev` or building it manually.

## Authors

* **Adrian Wysocki** - [theratty](https://github.com/theratty)
* **Michał Szczepańczyk** - [Shaid3r](https://github.com/Shaid3r)
* **Jakub Wojtyczko** - [JakubWojtyczko](https://github.com/JakubWojtyczko)
* **Kamil Warchoł** - [fisheye36](https://github.com/fisheye36)
* **Kamil Tomczyk** - [KamTomczyk](https://github.com/KamTomczyk)
* **Karol Cedro** - [Emu-Emax](https://github.com/Emu-Emax)
