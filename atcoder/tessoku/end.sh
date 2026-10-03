set -e

cd "$(dirname "$0")"
cur="$1"
next=$(printf "%s%02d" "${BASH_REMATCH[1]}" $((10#${BASH_REMATCH[2]} + 1)))

jj ship "Add:tessoku/$cur"

touch "$next.py"
code "$next.py"
