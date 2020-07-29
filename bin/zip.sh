declare DIR="$(cd "$(dirname "$0")/.." && pwd -P)"
mkdir -p "$DIR/build"

if [[ "$1" =~ ^-?a$ ]]; then
  # for uploading to AnkiWeb
  declare addon_id=''
else
  # for installing myself
  declare addon_id='search_bar'
fi

cd "$DIR"

zip -r "$DIR/build/$addon_id.ankiaddon" \
  "manifest.json" \
  "__init__.py" \
  "src/"*".py" \
  "web/"* \
  "icons/"*
