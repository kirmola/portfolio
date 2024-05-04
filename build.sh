
# # Install Poetry
# curl -sSL https://install.python-poetry.org | python3 -;
# export PATH="/vercel/.local/bin:$PATH";
# poetry install;
# poetry --version

# Install requirements

pip install -r requirements.txt

# Generate CSS
cd theme/static_src;
npm install;
npm run build;
cd ../..;

# Generate Static files
python3.12 manage.py collectstatic --noinput;
