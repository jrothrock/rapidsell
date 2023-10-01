# Terraform
## Building from scratch
Note, there's a bit of a chicken before the egg issue here in that, the zone needs to
created, and then the DNS name servers need to be updated on the domain registrar before the creation of the ACM cerificate.

Running terraform apply once, then updating the DNS name servers (can be seen with `terraform output`), and running again should work.

The creation of the API gateway has been moved, and is currently handled by chalice. Additionally,
the creation of the CNAME (which is handled by terraform), relies on the dev.json file created by
chalice. This file is created by chalice after running `poetry run task deploy`. Terraform populates chalice's config.json.

It may take some time for DNS propogration and ACM certificate validation. So wait a bit before steps 1 and 1b.

### Steps
From scratch the steps are:
1. Run `terraform apply` (may explode due to DNS settings, or CNAME)

1b. If due to DNS settings: Run `terraform apply` again (this will create the ACM needed for chalice.)

2. Run `poetry run task deploy`

3. Run `terraform apply` again (this will create the CNAME)

