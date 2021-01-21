# The MIT License (MIT)
#
# Copyright (c) 2015-2017 Stefan Fischer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Prompt and verify user input on the command line.

The project was initiated by Stefan Fischer.

Note
----
    This project is still a work in progress.

"""

import getpass
import re

__author__ = "Stefan Fischer"
__contact__ = "Stefan Fischer <sfischer13@ymail.com>"
__copyright__ = "Copyright (c) 2015-2017 Stefan Fischer"
__credits__ = []
__date__ = "2017-06-05"
__license__ = "MIT"
__status__ = "development"
__version__ = "0.4.1"

PROMPT = "? "
"""Prompt that will be shown by default."""
RE_EMAIL_SIMPLE = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
"""Regular expression for email addresses."""


def character(prompt=None, empty=False):
    """Prompt a single character.

    Parameters
    ----------
    prompt : str, optional
        Use an alternative prompt.
    empty : bool, optional
        Allow an empty response.

    Returns
    -------
    str or None
        A str if the user entered a single-character, non-empty string.
        None if the user pressed only Enter and ``empty`` was True.

    """
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    elif len(s) == 1:
        return s
    else:
        return character(prompt=prompt, empty=empty)


def email(prompt=None, empty=False, mode="simple"):
    """Prompt an email address.

    This check is based on a simple regular expression and does not verify
    whether an email actually exists.

    Parameters
    ----------
    prompt : str, optional
        Use an alternative prompt.
    empty : bool, optional
        Allow an empty response.
    mode : {'simple'}, optional
        'simple' will use a simple regular expression.
        No other mode is implemented yet.

    Returns
    -------
    str or None
        A str if the user entered a likely email address.
        None if the user pressed only Enter and ``empty`` was True.

    """
    if mode == "simple":
        s = _prompt_input(prompt)
        if empty and not s:
            return None
        else:
            if RE_EMAIL_SIMPLE.match(s):
                return s
            else:
                return email(prompt=prompt, empty=empty, mode=mode)
    else:
        raise ValueError


def integer(prompt=None, empty=False):
    """Prompt an integer.

    Parameters
    ----------
    prompt : str, optional
        Use an alternative prompt.
    empty : bool, optional
        Allow an empty response.

    Returns
    -------
    int or None
        An int if the user entered a valid integer.
        None if the user pressed only Enter and ``empty`` was True.

    """
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    else:
        try:
            return int(s)
        except ValueError:
            return integer(prompt=prompt, empty=empty)


def real(prompt=None, empty=False):
    """Prompt a real number.

    Parameters
    ----------
    prompt : str, optional
        Use an alternative prompt.
    empty : bool, optional
        Allow an empty response.

    Returns
    -------
    float or None
        A float if the user entered a valid real number.
        None if the user pressed only Enter and ``empty`` was True.

    """
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    else:
        try:
            return float(s)
        except ValueError:
            return real(prompt=prompt, empty=empty)


def regex(pattern, prompt=None, empty=False, flags=0):
    """Prompt a string that matches a regular expression.

    Parameters
    ----------
    pattern : str
        A regular expression that must be matched.
    prompt : str, optional
        Use an alternative prompt.
    empty : bool, optional
        Allow an empty response.
    flags : int, optional
        Flags that will be passed to ``re.match``.

    Returns
    -------
    Match or None
        A match object if the user entered a matching string.
        None if the user pressed only Enter and ``empty`` was True.

    See Also
    --------
    re.match

    """
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    else:
        m = re.match(pattern, s, flags=flags)
        if m:
            return m
        else:
            return regex(pattern, prompt=prompt, empty=empty, flags=flags)


def secret(prompt=None, empty=False):
    """Prompt a string without echoing.

    Parameters
    ----------
    prompt : str, optional
        Use an alternative prompt.
    empty : bool, optional
        Allow an empty response.

    Returns
    -------
    str or None
        A str if the user entered a non-empty string.
        None if the user pressed only Enter and ``empty`` was True.

    Raises
    ------
    getpass.GetPassWarning
        If echo free input is unavailable.

    See Also
    --------
    getpass.getpass

    """
    if prompt is None:
        prompt = PROMPT
    s = getpass.getpass(prompt=prompt)
    if empty and not s:
        return None
    else:
        if s:
            return s
        else:
            return secret(prompt=prompt, empty=empty)


def string(prompt=None, empty=False):
    """Prompt a string.

    Parameters
    ----------
    prompt : str, optional
        Use an alternative prompt.
    empty : bool, optional
        Allow an empty response.

    Returns
    -------
    str or None
        A str if the user entered a non-empty string.
        None if the user pressed only Enter and ``empty`` was True.

    """
    s = _prompt_input(prompt)
    if empty and not s:
        return None
    else:
        if s:
            return s
        else:
            return string(prompt=prompt, empty=empty)


def _prompt_input(prompt):
    if prompt is None:
        return input(PROMPT)
    else:
        return input(prompt)
