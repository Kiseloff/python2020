import requests
import hashlib
import sys


def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res


def get_password_leaks_count(hash_to_check, hashes):
    for line in hashes.text.splitlines():
        if (hash_to_check in line):
            num = line.split(':')[1]
            return num
    return 0


def pwned_api_check(password):
    """Checks password by API and returns the count if it's present in DB

    Args:
        password (str): an item of password to check

    Returns:
       zero or value of the counter

    """
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1password[0:5], sha1password[5:]
    res = request_api_data(prefix)
    num = get_password_leaks_count(suffix, res)
    return num


def main(args):
    """Check input data by https://haveibeenpwned.com/

    Args:
        args (list[string]): a list of passwords to check

    Returns:
        None
    """

    for password in args:
        num = pwned_api_check(password)
        if num:
            print(f'[-] Password \'{password}\' occures {num} times!')
        else:
            print(f'[+] Password \'{password}\' is safe')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))