# Witch App

Load up database

```sh
docker-compose up -d
```

Export requirements

```sh
poetry export --without-hashes > requirements.txt
```

## Notes

### Elastic Beanstalk

```sh
eb create # create/restart an environment
eb deploy # update an environment
```

## Dependencies

- Docker
- postgres docker image

## Ideas

- witch log in
- famous witches
- potions and spells
- speak to the shadow witch

## Technical

- auth
- postgres on AWS
- github copilot
- CI
- CD
- Encrypt

## Done

- postgres

## References

[Running Fastapi on Elastic Beanstalk](https://testdriven.io/blog/fastapi-elastic-beanstalk/)
