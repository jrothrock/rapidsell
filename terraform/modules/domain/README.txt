Note, there's a bit of a chicken before the egg issue here in that, the zone needs to
created, and then the DNS name servers need to be updated on the domain registrar before the
creation of the ACM cerificate.

Running terraform apply once, then updating the DNS name servers (`terraform output`), and running again work.
This is applicable to validating the ACM certificate and using it with the API gateway.
