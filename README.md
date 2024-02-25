# Backend

A service for handling extract text from pdf and check if the student is graduated or not.

## Prerequisite

Run this command to initialize the database and create a table

```sh
python3 init-db.py
```

This will create a file name `courses.db`

## Usage

Upload your transcript to this endpoint

```
https://glow-equal-geometry.glitch.me/api/upload
```

![](https://cdn.discordapp.com/attachments/1205014666145828884/1205016753839808594/Screenshot_2567-02-08_at_12.01.32.png?ex=65e010ce&is=65cd9bce&hm=07c7b2c4cda419c185c76d559c696181b780f2db333ae3ce7a8b7d2e31f438af&)

Api will return the student data with enrolled courses and graduation result

## Contributors

- [Qu1etboy](https://github.com/qu1etboy)
- [NpatsL](https://github.com/npatsl)