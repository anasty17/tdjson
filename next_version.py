import sys
import requests
import traceback

from packaging import version


def main():
    latest_tdlib_version = version.parse(sys.argv[1])

    try:
        res = requests.get("https://pypi.org/pypi/tdjson/json", timeout=10)
        res.raise_for_status()
        data = res.json()
        current_pypi_version = version.parse(data["info"]["version"])
    except Exception:
        traceback.print_exc()
        sys.exit(1)

    if current_pypi_version.base_version == latest_tdlib_version.base_version:
        next_post_version = (current_pypi_version.post or 0) + 1
        print(f"{current_pypi_version.base_version}.post{next_post_version}", end="")
    else:
        print(latest_tdlib_version, end="")


if __name__ == "__main__":
    main()
