#!/bin/python3

import sys
import os

if len(sys.argv) != 2:
    print("Usage: python3 add-course.py <COURSE-NAME>")
    sys.exit(1)

course = sys.argv[1]
os.mkdir(course)

readme = f"""# {course}

## General Advise

## Resources
"""

with open(f"{course}/README.md", "w") as ofile:
    ofile.write(readme)
