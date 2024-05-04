
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -;
export PATH="/vercel/.local/bin:$PATH";
poetry install;
poetry --version;

# Generate CSS
cd theme/static_src;
npm install;
npm run build;
cd ../..;

# Generate Static files
poetry run python3 manage.py collectstatic --noinput;
