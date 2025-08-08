#!/bin/bash

# Usage: ./ctime.sh n_times "command"
# Example: ./ctime.sh 5 "python dicedistributions.py < dicedistributions3.in"

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 n_times \"command\""
  exit 1
fi

N=$1
shift
CMD="$@"

echo "Running: $CMD"
echo "Number of runs: $N"
echo

for ((i=1; i<=N; i++)); do
  echo "Run $i:"
  # Try GNU time with formatting
  if command -v time >/dev/null 2>&1 && time --version 2>&1 | grep -q GNU; then
    command time -f "Elapsed Time: %E (real), %U (user), %S (sys)" bash -c "$CMD"
  else
    # Fallback to shell built-in time
    echo "Warning: Custom time formatting not available. Using default time output."
    time bash -c "$CMD"
  fi
  echo
done
