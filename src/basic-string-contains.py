def check_string_contains(init_string, sub_string) -> None:
    print(f"Checking if: [{init_string}] contains: [{sub_string}]")

    if sub_string in init_string:
        print(f"String: [{init_string}] contains [{sub_string}]")
    else:
        print(f"String [{init_string}] does not contain [{sub_string}]")


def main() -> None:
    init_string = "This is my test string"

    sub_string_upper = "TEST"
    sub_string_lower = sub_string_upper.lower()

    check_string_contains(init_string, sub_string_upper)

    check_string_contains(init_string, sub_string_lower)


if __name__ == "__main__":
    main()
