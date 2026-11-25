import logging


def main() -> None:
    logging.basicConfig(
        level=logging.ERROR,
        format="%(levelname)s %(name)s: %(message)s",
    )


if __name__ == "__main__":
    main()
