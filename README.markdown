# Notifo IMAP Listener [![status](http://stillmaintained.com/vrillusions/notifo-imap-listener.png)](http://stillmaintained.com/vrillusions/notifo-imap-listener)

# IMPORTANT NOTICE

As of September 8, 2011 notifo is no longer being actively developed ([source](http://blog.notifo.com/notifo)).  I will do my best to hammer out the remaining big bugs this has but you should look into other services.  I've started to use [boxcar](http://boxcar.io/) and may make a similar project for that as boxcar's email notification also does not send the content of the email.

As the name suggests, this connects to a mail server over IMAP and waits for any incoming emails.  When it receives a message it sends it off to notifo.

While notifo has a built in email notification this script is still useful since you can send the content of the message where notifo's built in notification only parses the subject (as of Aug 2011).

## Requirements

- Python 2.6 (May work with 2.5 but development is done on 2.6)
- An email that receives incoming messages
- An account on http://notifo.com

## Usage

Please note that durring development some options may not actually do anything.

- Create an email that will be the listener
- Copy config.ini.sample to config.ini and edit with connection info
- test with `./notifo-imap-listener.py`.
- if no errors use ctrl-c and then start with `./notifo-imap-listener.py >output.log 2>&1 &`
- test it by sending an email to the address and it should show up on phone within a second or two.
- to properly kill use either ctrl-c if interactive or send SIGINT to process `kill -INT 123` where 123 is process id

## Config.ini Options

- Mail section is for setup of email address.
- Mail.ssl is if the client should connect to the server via SSL (highly recommended).
- Notifo section is for setup of notifo credentials
- Notifo.username is your api username which is usually the same as your actual username
- Notifo.secret is your api secret which you can get from logging in to notifo and click on settings.
- Security is for ways to prevent anyone from posting to account
- Security.from, if set to something other than None, will require messages to come from the specified email.  All others will be silently dropped
- Logging is for the logging system
- Logging.file is the file to log to. If you don't want to log to a file use /dev/null
- Logging.level one of debug, info, warning, error, or critical. Used for both console and log file

## Initial Goals

- constantly listens for new mail to relay the message as quick as possible
- single user for now
- basic user validation (must come from an authorized email address)

## Future Goals

- multi-user (using twisted)
