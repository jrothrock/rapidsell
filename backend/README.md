# Backend

Backend uses the Chalice serverless microframework. 

All of the routes launch under the same lambda function, but events are launched under their own.

Uses PynamoDB as an ORM like library for Dyanmo, and Cognito is used for user management.

Serp API is used to pull info from Google lens, but a chromium lambda layer should be used in the future.