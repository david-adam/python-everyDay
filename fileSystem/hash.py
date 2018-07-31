# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import hashlib


# --- CALCULATING HASHES OF FILE CONTENTS ---

def stronghash(text):
    """
    Computes the MD5 hash of a text string
    """
    # print(hashlib.algorithms_guaranteed)
    h = hashlib.sha3_256()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


if __name__ == '__main__':
    import pathlib
    source_file = (pathlib.Path(__file__) / __file__).resolve()
    with source_file.open('r') as handle:
        content = handle.read()

    # Compute MD5 hash of some file content
    original_md5 = stronghash(content)
    print('Original content hash: {}'.format(original_md5))

    # Now let's change the contents and recompute the MD5
    content += 'yohoo'
    modified_hash = stronghash(content)
    print('Modified content hash: {}'.format(modified_hash))

