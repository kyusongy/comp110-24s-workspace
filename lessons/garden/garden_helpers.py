"""Some functions for my garden plan!"""

__author__ = "730720425"


def add_by_kind(inp_dict: dict[str, list[str]], kind: str, stuff: str) -> None:
    """Adds a plant to a garden dictionary that is sorted by the kind of plant."""
    if kind in inp_dict:
        inp_dict[kind].append(stuff)
    else:
        inp_dict[kind] = [stuff]


def add_by_date(inp_dict: dict[str, list[str]], month: str, stuff: str) -> None:
    """Adds a plant to a garden dictionary that is sorted by the date in which the seeds should be sown."""
    if month in inp_dict:
        inp_dict[month].append(stuff)
    else:
        inp_dict[month] = [stuff]


def lookup_by_kind_and_date(dict1: dict[str, list[str]], dict2: dict[str, list[str]], kind: str, month: str) -> str:
    """Searches through both dictionaries and returns a list of what plants of a certain kind to plant at a certain date."""
    plant_list: list[str] = []
    for i in dict1[kind]:
        if i in dict2[month]:
            plant_list.append(i)
    if len(plant_list) != 0:
        return f"{kind} to plant in {month}: {plant_list}"
    else:
        return "No flowers to plant in June."