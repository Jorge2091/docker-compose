from os import system as t
t("sudo docker compose up -d")
t("sudo docker exec -it app5 node seeds/seed.js")