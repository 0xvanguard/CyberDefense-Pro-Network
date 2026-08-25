#!/usr/bin/env python3
"""Entry point for 0xv CLI."""
import os
import sys

# Ensure we're in the right directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

# Import main from 0xv script
import importlib.util
spec = importlib.util.spec_from_file_location("_0xv_main", os.path.join(script_dir, "0xv"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.main()
