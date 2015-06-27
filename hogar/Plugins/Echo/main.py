#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2015 Leon Jacobs
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

''' A simple echo plugin '''

def applicable_types():

    '''
        Applicable Types

        Returns the type of messages this plugin is for.
        See: hogar.static.values

        --
        @return list
    '''

    return ['text']

def commands():

    '''
        Commands

        In the case of text plugins, returns the commands
        that this plugin should trigger for. For other
        message types, a empty list should be returned.

        --
        @return list
    '''

    return ['echo', 'say']

def should_reply():

    '''
        Should Reply

        Specifies wether a reply should be sent to the original
        sender of the message that triggered this plugin.

        --
        @return bool
    '''

    return True

def run(message):

    '''
        Run

        Run the custom plugin specific code. A returned
        string is the message that will be sent back
        to the user.

        --
        @param  message:dict    The message sent by the user

        @return str
    '''

    # Get the message contents
    text = message['text']

    # Remove a mention. This could be the case
    # if the bot was mentioned in a chat room
    if text.startswith('@'):
        text = text.split(' ', 1)[1].strip()

    # Some bots will accept commands that started
    # with a '/'
    if text.startswith('/'):
        text = text.replace('/', '', 1).strip()

    # Remove the trigger command
    for command in commands():
        text = text.replace(command, '', 1).strip()

    return text