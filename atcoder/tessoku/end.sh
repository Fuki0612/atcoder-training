set -e

if [[ ! "$1" =~ ^([A-Z])([0-9]{2})$ ]]; then
  echo "usage: $0 <問題番号 例: A02, B10>" >&2
  exit 1
fi

cd "$(dirname "$0")"
cur="$1"
next=$(printf "%s%02d" "${BASH_REMATCH[1]}" $((10#${BASH_REMATCH[2]} + 1)))

jj ship "Add:tessoku/$cur"

touch "$next.py"
code "$next.py"
