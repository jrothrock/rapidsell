# About
Take pictures of items to recognize what they are, and find the value of them.

Uses Vue & Ionic for the frontend, Chalice on the backend (an AWS Python serverless microframework), and Terraform for infrastructure provisioning and management.


## Local
In terminal 1, go into the `./app` directory, install the dependencies `yarn install` and run `npm run dev` to start the Vue app.

In terminal 2, go into the `./backend` directory, install the dependecies with `poetry install`, run `source .venv/bin/activate` and `poetry run task dev` to start the app.

## Linting & Formatting
For the app: `npm run verify`

For the backend: `poetry run verify`

## Building IOS app
To build/update the IOS app, run `npx cap sync`, then build in Xcode.

## Deploying
Frontend: `npm run deploy`

Backend: `poetry run task deploy`

Terraform: `terraform apply`
