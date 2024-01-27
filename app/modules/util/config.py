"""

Utility methods for the config
----------------

"""


def eval_bool_env_var(env_var: str) -> bool:
    """Evaluates a boolean environment variable

    :param env_var: The environment variable to evaluate
    :return: The evaluated boolean value
    """
    # XXX: python-dotenv doesn't support boolean values nicely, so we have to
    # do this ourselves
    return True if env_var.lower() in ("true", "t", "1") else False
