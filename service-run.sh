ROOT_PATH='/home/mitro/Documents'

gnome-terminal -- /bin/sh -c 'cd /home/mitro/Documents/bud-service-adjustment/ && mvn spring-boot:run; exec bash'

gnome-terminal -- /bin/sh -c 'cd /home/mitro/Documents/bud-service-common/ && mvn spring-boot:run; exec bash'

gnome-terminal -- /bin/sh -c 'cd /home/mitro/Documents/bud-service-projection/ && mvn spring-boot:run; exec bash'

gnome-terminal -- /bin/sh -c 'cd /home/mitro/Documents/bud-web/ && npm start; exec bash'
