"""drypy - dryrun for python

.. moduleauthor:: Daniele Zanotelli <dazano@gmail.com>
"""

import logging
from . import version

logger = logging.getLogger(__name__)

def get_version():
    """Returns the current drypy version.

    Returns:
        A string with the current drypy version.
    """
    return version._version

# dryrun switcher
_dryrun = False

def get_status():
    """Returns True if the dryrun system is active.

    Returns:
        True or False
    """
    if _dryrun not in (True, False):
        msg = "Don't manually change the _dryrun flag! Use 'set_dryrun' "
        msg += "instead. Dryrun set to False."
        logger.warning(msg)
        set_dryrun(False)
    return _dryrun

def set_dryrun(value):
    """Set the dryrun mode on or off.

    Args:
        value (bool): Mode to be in.
    """
    global _dryrun
    if type(value) is not bool:
        raise TypeError("Boolean required")
    _dryrun = value

def toggle_dryrun():
    """Toggle the current dryrun mode.
    """
    if get_status() is True:
        set_dryrun(False)
    else:
        set_dryrun(True)
