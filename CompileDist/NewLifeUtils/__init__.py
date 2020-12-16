__version__ = "5.0.1"
name = "NewLifeUtils"

lang = "en"

try:
    import os
    import datetime
    import re
    import traceback
    import time
    import random
    import sqlite3
    import json
    import inspect

    from pathlib import Path
    from itertools import islice
except ModuleNotFoundError as e:
    print(f"Unable to import dependences: {e}")
    exit(-1)
except Exception as e:
    print(e)
    exit(-1)