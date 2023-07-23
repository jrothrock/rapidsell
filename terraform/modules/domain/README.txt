Note, there's a bit of a chicken before the egg issue here in that, the zone needs to
created, and then the DNS name servers need to be updated on the domain registrar before the
creation of the ACM cerificate.

Running terraform apply once, then updating the DNS name servers, and running again may work.
