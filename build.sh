
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -;
export PATH="/vercel/.local/bin:$PATH";
poetry install;
poetry self add poetry-plugin-export
poetry export --without-hashes > requirements.txt


# Install from requirements.txt
pip install -r requirements.txt

# Generate CSS
cd theme/static_src;
npm install;
npm run build;
cd ../..;

# Generate Static files
poetry run python3 manage.py collectstatic --noinput;
