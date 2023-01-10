
if __name__ == "__main__":
    cookie = ""
    result = ""
    for item in cookie.split(" "):
        if item.startswith("pt_key") or item.startswith("pt_pin"):
            result += item
    print(result)
