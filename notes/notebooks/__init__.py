import logging
import os  # noqa: E402

# Third Party
import numba as nb  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib import pyplot as plt  # noqa: E402


def _get_logger() -> logging.LoggingAdapter:
    app_logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARNING)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s > %(message)s",
            datefmt="%d%m%y %I:%M:%S",
        )
    )
    app_logger.addHandler(handler)
    return logging.LoggerAdapter(app_logger)


logger = _get_logger()


try:
    # Third Party
    from IPython import get_ipython

    _ipy = get_ipython()
    _ipy.run_line_magic("load_ext", "autoreload")
    _ipy.run_line_magic("autoreload", "2")
    del _ipy
except Exception as e:
    logger.warning(f"couldnt set up autoreload: {e}")


try:
    # Third Party
    from tqdm.notebook import tqdm, trange
except Exception as e:
    logger.warning(f"not in a notebook; using the standard tqdm: {e}")
    # Third Party
    from tqdm import tqdm, trange
