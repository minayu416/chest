import hexdump


def dump_hex(bs: bytes):
    """Convert bytes to hex

    Args:
        bs (bytes):

    Returns:
        TODO string: Return

    """
    return ':'.join('{:02X}'.format(b) for b in bs)


# TODO others function about hex/bytes convert.
