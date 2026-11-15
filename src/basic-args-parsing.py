import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="basic-args-parsing",
        description="Python Template CLI application",
    )

    parser.add_argument(
        "--name",
        type=str,
        required=False,
        help="Name",
        default="Nikolas",
    )

    parser.add_argument(
        "--surname",
        type=str,
        required=False,
        help="Surname",
        default="Steiner",
    )

    parser.add_argument(
        "--age",
        type=str,
        required=False,
        help="Enter the age",
        default="22",
    )

    parser.add_argument(
        "--address",
        type=str,
        required=False,
        help="Enter the address",
        default="Manhattan",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    name = args.name
    surname = args.surname
    age = args.age
    address = args.address

    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Age: {age}")
    print(f"Address: {address}")


if __name__ == "__main__":
    main()
