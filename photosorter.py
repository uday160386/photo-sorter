import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='select the service')
    parser.add_argument('--service', required=True)
    args = parser.parse_args()
    
    delete_duplicate_images(args.path)
