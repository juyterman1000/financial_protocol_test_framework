#!/bin/bash
echo "Running all protocol tests..."
pytest tests/ --disable-warnings -v
