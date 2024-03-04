in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apple": True}
in_stock["milk"] = True
for key in in_stock:
    if in_stock[key]:
        print(key)
