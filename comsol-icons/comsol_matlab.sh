#!/bin/bash

comsol_bin_path=`dirname -z \`readlink -f \\\`which comsol\\\`\``

comsol_path=`dirname ${comsol_bin_path}`


if [ -d "${comsol_path}/mli" ]; then
    comsol_mli_path=${comsol_path}/mli
else
    comsol_mli_path=${comsol_path}/../mli
fi


echo ${comsol_mli_path}


# Create a temporary directory for all comsol related stuff
tmp_dir=`mktemp -d --tmpdir comsol_matlab.XXXXX`

server_out=${tmp_dir}/comsol_server_output
fifo_server_in=${tmp_dir}/comsol_server_input

mkfifo ${fifo_server_in}
#mkfifo ${server_out}

# Make sure the comsol server closes automatically after you close matlab
# default port is 2036
# specify this to an other value if you wish
comsol server -port 2036  < ${fifo_server_in} | tee ${server_out} &

comsol_pid=$!

echo Comsol server pid = ${comsol_pid}

echo tempdir           = ${tmp_dir}
echo server fifo in    = ${fifo_server_in}
echo server out        = ${server_out}

# I don't know why you need this, comsol will halt until something is sent in on the fifo
echo -n > ${fifo_server_in}

while true; do
    # Get the line that tells us exactly what port the comsol server started on
    the_line=`grep "listening on port" -m 1 ${server_out}`

    # Bashism: remove everything before port to get the port number
    the_port=${the_line#*port}
    if [ -n "${the_port}" ]; then break; fi
    # don't keep polling the file too fast
    sleep 0.1
done

echo running on port ${the_port}
# Run matlab, add the comsol path, connect to the server, display the info
matlab -desktop -r "addpath('${comsol_mli_path}'); disp('Running Matlab with Comsol. Connecting to localhost on port ${the_port}'); mphstart(${the_port});"


# Ugly hack, but we will flood the server with close requests
# this is needed for the following reasons:
# 1. Comsol takes a while to notice that matlab has closed the connection
# 2. A user may have opened up the server with a graphical comsol interface
#    Therefore, we will want to keep trying to close it.
while true; do
    echo close > ${fifo_server_in}

    # sleep for 1 second as to not flood it too harshly
    sleep 1
    # send the kill -0 command
    # kill -0 will fail (1) if the process stopped
    kill -s 0 ${comsol_pid}
    RETVAL=$?
    if [ 0 -ne ${RETVAL} ]; then break; fi
done


# now we are safe to remove that temporary directory we created
rm -rf ${tmp_dir}


