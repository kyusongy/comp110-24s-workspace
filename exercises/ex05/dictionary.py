"""EX05 - Dictionary Utility Functions."""

__author__ = "730720425"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Return a dict[str, str] that inverts the keys and the values."""
    list_of_keys: list[str] = []
    list_of_values: list[str] = []
    output: dict[str, str] = {}
    for keys in inp_dict:
        list_of_keys.append(keys)
        list_of_values.append(inp_dict[keys])
    for i in range(0, len(inp_dict)):
        output[list_of_values[i]] = list_of_keys[i]
    if len(output) != len(inp_dict):
        raise KeyError("Change your input!")
    else:
        return output
    

def favorite_color(inp_dict: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    list_of_colors: list[str] = []
    color_count: dict[str, int] = {}
    fave_color: list[str] = []
    count_list: list[int] = []
    for keys in inp_dict:
        list_of_colors.append(inp_dict[keys])
    for colors in list_of_colors:
        color_count[colors] = 0
        for i in list_of_colors:
            if colors == i:
                color_count[colors] += 1
    for colors in color_count:
        count_list.append(color_count[colors])
    for colors in color_count:
        if color_count[colors] == max(count_list):
            fave_color.append(colors)
    return fave_color[0]
        

def count(inp_list: list[str]) -> dict[str, int]:
    """Produces a a dictionary of the counts of each of the items in the input list."""
    storage: dict[str, int] = {}
    for i in inp_list:
        if i in storage:
            storage[i] += 1
        else:
            storage[i] = 1
    return storage


def alphabetizer(inp_list: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary of the letters and the lists of words that belong to that letter."""
    output_dict: dict[str, list[str]] = {}
    for i in inp_list:
        if i[0].lower() in output_dict:
            output_dict[i[0].lower()].append(i)
        else:
            output_dict[i[0].lower()] = [i]
    return output_dict


def update_attendance(inp_dict: dict[str, list[str]], day: str, student_attended: str) -> None:
    """Mutates and return that dictionary."""
    if day in inp_dict:
        if student_attended in inp_dict[day]:
            """Do nothing."""
        else:
            inp_dict[day].append(student_attended)
    else:
        inp_dict[day] = [student_attended]