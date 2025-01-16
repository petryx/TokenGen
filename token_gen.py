
# Author: Marlon Petry
# Date: 2025-16-01
# Description: This script generates a hash for each epoch time between the start and end times.
# License: MIT License
import sys
import hashlib
import argparse
from datetime import datetime, timezone, timedelta

def epoch_gen(timestamp, gmt_offset):
    """
    Converts a datetime string to epoch based on GMT offset.

    :param timestamp: String containing date and time in 'dd-mm-YYYY HH:MM:SS' format.
    :param gmt_offset: Integer representing GMT offset in hours.
    :return: Integer epoch time.
    """
    gmt_timezone = timezone(timedelta(hours=gmt_offset))  # GMT is UTC+0
    epoch = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
    epoch_int = int(epoch.replace(tzinfo=gmt_timezone).timestamp())
    return epoch_int

def generate_hash(token_to_hash, hash_type):
    """
    Generates a hash based on the given token and hash type.

    :param token_to_hash: String to hash.
    :param hash_type: Hash type to use (e.g. 'sha1', 'md5').
    :return: Hashed token.
    """
    if hash_type == 'sha1':
        hash_object = hashlib.sha1(token_to_hash.encode())
    elif hash_type == 'md5':
        hash_object = hashlib.md5(token_to_hash.encode())
    elif hash_type == 'sha256':
        hash_object = hashlib.sha256(token_to_hash.encode())
    elif hash_type == 'sha512':
        hash_object = hashlib.sha512(token_to_hash.encode())
    
    else:
        print("Invalid hash type")
        sys.exit(1)
    return hash_object.hexdigest()


def gen_tokens(start, end, username, gmt_offset,alg_token='md5'):
    """
    Generates a hash for each epoch time between the start and end times.

    """
    start_epoch = epoch_gen(start, gmt_offset)
    end_epoch = epoch_gen(end, gmt_offset)
    aux = start_epoch
    while aux <= end_epoch:
        token_to_hash = str(username+str(aux))
        print(generate_hash(token_to_hash, alg_token))
        aux += 1


def main():
    parser = argparse.ArgumentParser(description='Generate a SHA1 hash from epoch time range')
    parser.add_argument('-s', '--start', help='Start time format d-m-Y H:M:S')
    parser.add_argument('-e', '--end', help='End time  format d-m-Y H:M:S')
    parser.add_argument('-u', help='Username')
    parser.add_argument("-g", type=int, default=0, help="GMT offset in hours")
    parser.add_argument("-a", "--alg", default='md5', help="Hash algorithm to use (md5, sha1, )")
    
    args = parser.parse_args()
    gen_tokens(args.start, args.end, args.u,args.g)

if __name__ == '__main__':
    main()
