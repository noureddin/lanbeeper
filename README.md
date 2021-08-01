# LanBeeper

Flask-based LAN communication tool, to be run by a technical user but used by non-technical users on the same nework.

- Simple, minimal UI, very easy for non-technical users.
- Responsive design, viewable on desktop and mobile.
- Easily localizable and customizable.

## Functions

- Send a beep (just a notification).
- Send a text message.

### To-do

- Send a voice message.
- Initiate a voice call.

## Installation and Usage

1. Make sure Flask is installed:

        python3 -m pip install --user --upgrade flask

2. Clone this repo:

        git clone https://github.com/noureddin/lanbeeper

3. Run the server (no need to change directory; it can be run from anywhere):

        python3 lanbeeper/lanbeeper.py

    **(OR)** Run the server with a specific language (See *Localization* section below):

        python3 lanbeeper/lanbeeper.py ar

### Localization

The first argument to the script can be a translation file or a language code.

For a language code to be understood by LanBeeper, it must exist in the `translation/` directory, e.g., `ar.ini` and `en.ini`.

For a translation file to be understood, it must be essentially the same as the files in the `translation/` directory, with only the values changed.


## License

Apache License, Version 2.

Copyright 2021 Noureddin.
