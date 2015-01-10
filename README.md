Install
=======

    aptitude install virtualenvwrapper
    mkvirtualenv mobiezit
    pip install -r requirements/development.txt

You need to add to $VIRTUAL_ENV/bin two file:

- postactivate 
    
    #!/bin/bash
    # This hook is run after every virtualenv is activated.
    export DJANGO_SETTINGS_MODULE="mobiezit.settings.development"
    export SECRET_KEY="your_secret_key"

- predeactivate

    #!/bin/bash
    # This hook is run before every virtualenv is deactivated.
    unset DJANGO_SETTINGS_MODULE
    unset SECRET_KEY

