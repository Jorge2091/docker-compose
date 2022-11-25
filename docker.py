from os import system as t
t("docker compose up -d")
t("docker exec -it app3 node seeds/seed.js")
t("echo jorge is here")
