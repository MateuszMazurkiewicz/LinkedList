import os
import sys
from pathlib import Path

package_path = str((Path(__file__).parent / "..").resolve())
sys.path.insert(0, package_path)

import linked_list