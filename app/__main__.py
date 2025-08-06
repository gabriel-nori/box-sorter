from app.app import App
import argparse
import time
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Application requires 4 parameters from CMD"
    )

    parser.add_argument(
        "--dimensions",
        nargs='+',
        required=True,
        type=float,
        help="Dimensions in the following order, separated by space: width height length mass"
    )

    args = parser.parse_args()
    dim = args.dimensions

    if len(dim) != 4:
        raise

    print("Application is starting...")
    start_time = time.time()
    processor = App()
    processor.start(dim[0], dim[1], dim[2], dim[3])
    print("Application finished in {} seconds".format(time.time() - start_time))