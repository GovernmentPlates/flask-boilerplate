"""

Utility methods for forms
----------------

"""


def collect_form_data(*args) -> dict:
    """
    Collects form data from a list of fields (used for form repopulation).

    :param args: list of fields to collect data from
    :return: dictionary of form data
    """
    data = {}
    for field in args:
        data[field.name] = field.data
    return data
