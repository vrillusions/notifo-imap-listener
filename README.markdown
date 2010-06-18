# Notifo IMAP Listener

As the name suggests, this connects to a mail server over IMAP and waits for any incoming emails.  When it receives a message it sends it off to notifo.  The key thing it must do is offer as close to realtime as possible.

## Requirements

- Python 2.6 (May work with 2.5 but development is done on 2.6)
- An email that receives incoming messages
- An account on http://notifo.com

## Setup

- Create an email that will be the listener
- Copy config.ini.sample to config.ini and edit with connection info

## Initial Goals

- constantly listens for new mail to relay the message as quick as possible
- single user for now
- basic user validation (must come from an authorized email address)

## Future Goals

- multi-user (using twisted)
