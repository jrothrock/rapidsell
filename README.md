# About
A small Python Lambda starter app using the chalice micro framework, with a Vue frontend, utilzing Terraform on top of AWS.

## Local
In terminal 1, go into the `./app` directory, install the dependencies `yarn install` and run `npm run dev` to start the Vue app.

In terminal 2, go into the `./backend` directory, install the dependecies with `poetry install`, run `source .venv/bin/activate` and `chalice local` to start the app.

## Linting
For the app: `npm run lint`
For the backend: `black .; isort .; flake8 .; mypy .;pydocstyle .  --count`

## Building IOS app
To build/update the IOS app, run `npx cap sync`

## Deploying
Terraform: `terraform apply` (may want to plan first)
Chalice: `chalice deploy`
Frontend: `npm run deploy`

## Adding new packages to backend
Chalice uses the requirements.txt to add new packages. So when adding packages with `poetry`,
run `poetry export -f requirements.txt --output requirements.txt`
