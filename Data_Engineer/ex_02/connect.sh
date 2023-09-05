#!/bin/bash

password="msp"

# Connect to the PostgreSQL container
docker exec -it postgres bash << EOF
  # Run psql with the -U, -d, -h, -W, and -c options to specify the username, database, host, and command.
  # Use the password variable to provide the password non-interactively.
  psql -U zstenger -d piscineds -h localhost -c "SELECT * FROM your_table;" << EOL
  ${password}
  EOL
EOF