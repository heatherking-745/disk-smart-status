"""Disk SMART Status — Print a short SMART OK or BAD summary for physical disks Windows exposes."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='disk_smart_status',
        description='Print a short SMART OK or BAD summary for physical disks Windows exposes.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Disk SMART Status')
    print('Is the disk throwing SMART errors.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
